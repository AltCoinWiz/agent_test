from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class LineItem:
    sku: str
    unit_price: Decimal
    quantity: int
    taxable: bool = True


@dataclass(frozen=True)
class Coupon:
    code: str
    percent_off: Decimal


@dataclass(frozen=True)
class CheckoutRequest:
    items: tuple[LineItem, ...]
    tax_rate: Decimal
    coupon: Coupon | None = None
    shipping: Decimal = Decimal("0.00")
