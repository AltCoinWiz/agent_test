from decimal import Decimal
from commerce.domain.models import Coupon

_COUPONS = {
    "SAVE10": Coupon("SAVE10", "percent", Decimal("10")),
    "TAKE20": Coupon("TAKE20", "fixed", Decimal("20.00"), Decimal("100.00")),
    "VIP15": Coupon("VIP15", "percent", Decimal("15"), Decimal("50.00")),
}

def find_coupon(code: str | None) -> Coupon | None:
    if not code:
        return None
    return _COUPONS.get(code.upper())
