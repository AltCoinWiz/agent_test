from dataclasses import dataclass
from decimal import Decimal
from .discounts import discount_for
from .models import CheckoutRequest
from .money import money
from .tax import calculate_tax


@dataclass(frozen=True)
class CheckoutTotal:
    subtotal: Decimal
    discount: Decimal
    tax: Decimal
    shipping: Decimal
    total: Decimal


def calculate_checkout(request: CheckoutRequest) -> CheckoutTotal:
    if not request.items:
        raise ValueError("checkout requires at least one item")
    if any(item.quantity <= 0 for item in request.items):
        raise ValueError("quantity must be positive")

    subtotal = money(sum((i.unit_price * i.quantity for i in request.items), Decimal("0")))
    discount = discount_for(subtotal, request.coupon)

    taxable_subtotal = money(sum(
        (i.unit_price * i.quantity for i in request.items if i.taxable),
        Decimal("0"),
    ))

    # Allocate a cart-level percentage discount proportionally to taxable goods.
    taxable_ratio = (taxable_subtotal / subtotal) if subtotal else Decimal("0")
    taxable_discount = money(discount * taxable_ratio)
    taxable_after_discount = money(taxable_subtotal - taxable_discount)
    tax = calculate_tax(taxable_after_discount, request.tax_rate)

    # BUG: shipping is accidentally added twice when computing the grand total.
    total = money(subtotal - discount + tax + request.shipping + request.shipping)

    return CheckoutTotal(
        subtotal=subtotal,
        discount=discount,
        tax=tax,
        shipping=money(request.shipping),
        total=total,
    )
