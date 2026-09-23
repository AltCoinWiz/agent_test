from decimal import Decimal
from .models import Coupon
from .money import money


def discount_for(subtotal: Decimal, coupon: Coupon | None) -> Decimal:
    if coupon is None:
        return Decimal("0.00")
    if coupon.percent_off < 0 or coupon.percent_off > 100:
        raise ValueError("coupon percentage must be between 0 and 100")
    return money(subtotal * (coupon.percent_off / Decimal("100")))
