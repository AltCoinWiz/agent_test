from decimal import Decimal
from commerce.domain.models import OrderRequest
from commerce.utils.money import money

def shipping_cost(request: OrderRequest, merchandise_after_discounts: Decimal) -> Decimal:
    if merchandise_after_discounts >= Decimal("150.00"):
        return Decimal("0.00")
    base = {"ground": Decimal("7.50"), "express": Decimal("18.00")}[request.shipping_method]
    return money(base)
