from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

@dataclass(frozen=True)
class Product:
    sku: str
    unit_price: Decimal
    taxable: bool = True

@dataclass(frozen=True)
class LineItem:
    product: Product
    quantity: int

@dataclass(frozen=True)
class Coupon:
    code: str
    kind: str
    value: Decimal
    minimum_subtotal: Decimal = Decimal("0")

@dataclass(frozen=True)
class Customer:
    customer_id: str
    loyalty_tier: str = "standard"
    tax_exempt: bool = False

@dataclass(frozen=True)
class Address:
    state: str
    postal_code: str

@dataclass(frozen=True)
class OrderRequest:
    items: list[LineItem]
    customer: Customer
    ship_to: Address
    shipping_method: str = "ground"
    coupon_code: Optional[str] = None

@dataclass(frozen=True)
class OrderTotals:
    merchandise: Decimal
    discount: Decimal
    shipping: Decimal
    taxable_amount: Decimal
    tax: Decimal
    total: Decimal
    applied_coupon: Optional[str] = None
    metadata: dict = field(default_factory=dict)
