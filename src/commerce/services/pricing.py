from decimal import Decimal
from commerce.domain.models import LineItem
from commerce.utils.money import money

def merchandise_total(items: list[LineItem]) -> Decimal:
    return money(sum((i.product.unit_price * i.quantity for i in items), Decimal("0")))

def taxable_merchandise(items: list[LineItem]) -> Decimal:
    return money(sum((i.product.unit_price * i.quantity for i in items if i.product.taxable), Decimal("0")))
