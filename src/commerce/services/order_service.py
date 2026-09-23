from decimal import Decimal
from commerce.domain.models import OrderRequest, OrderTotals
from commerce.infra.coupons import find_coupon
from commerce.services.pricing import merchandise_total, taxable_merchandise
from commerce.services.promotions import coupon_discount, loyalty_discount
from commerce.services.shipping import shipping_cost
from commerce.services.tax import calculate_tax
from commerce.utils.money import money

class OrderService:
    def calculate(self, request: OrderRequest) -> OrderTotals:
        merchandise = merchandise_total(request.items)
        taxable_merch = taxable_merchandise(request.items)
        coupon = find_coupon(request.coupon_code)

        coupon_amount = coupon_discount(merchandise, coupon)
        after_coupon = money(merchandise - coupon_amount)
        loyalty_amount = loyalty_discount(after_coupon, request.customer)
        discount = money(coupon_amount + loyalty_amount)
        discounted_merchandise = money(merchandise - discount)

        shipping = shipping_cost(request, discounted_merchandise)

        # Promotions are order-level, so allocate the total discount proportionally
        # across merchandise before computing the taxable portion.
        if merchandise == Decimal("0.00"):
            allocated_taxable_discount = Decimal("0.00")
        else:
            allocated_taxable_discount = money(discount * (taxable_merch / merchandise))

        taxable_amount = money(taxable_merch - allocated_taxable_discount)

        # Shipping is taxable in states where this service's tax table applies.
        if request.ship_to.state.upper() in {"AZ", "TX"}:
            taxable_amount = money(taxable_amount + shipping)

        tax = calculate_tax(taxable_amount, request.ship_to.state, request.customer)
        total = money(discounted_merchandise + shipping + tax)

        return OrderTotals(
            merchandise=merchandise,
            discount=discount,
            shipping=shipping,
            taxable_amount=taxable_amount,
            tax=tax,
            total=total,
            applied_coupon=coupon.code if coupon and coupon_amount else None,
            metadata={"loyalty_discount": str(loyalty_amount)},
        )
