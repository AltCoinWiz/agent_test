from decimal import Decimal
from commerce.domain.models import Coupon, Customer
from commerce.utils.money import money

def coupon_discount(subtotal: Decimal, coupon: Coupon | None) -> Decimal:
    if coupon is None or subtotal < coupon.minimum_subtotal:
        return Decimal("0.00")
    if coupon.kind == "percent":
        return money(subtotal * coupon.value / Decimal("100"))
    if coupon.kind == "fixed":
        return money(min(coupon.value, subtotal))
    raise ValueError(f"unknown coupon kind: {coupon.kind}")

def loyalty_discount(subtotal_after_coupon: Decimal, customer: Customer) -> Decimal:
    rates = {"standard": Decimal("0"), "silver": Decimal("2"), "gold": Decimal("5")}
    rate = rates.get(customer.loyalty_tier, Decimal("0"))
    return money(subtotal_after_coupon * rate / Decimal("100"))
