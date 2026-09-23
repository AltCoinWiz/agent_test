from commerce.domain.models import Address, Customer, LineItem, OrderRequest
from commerce.infra.catalog import get_product
from commerce.services.order_service import OrderService

def quote_order(lines: list[tuple[str, int]], state: str, *, coupon: str | None = None,
                loyalty: str = "standard", shipping: str = "ground", tax_exempt: bool = False):
    items = [LineItem(get_product(sku), qty) for sku, qty in lines]
    request = OrderRequest(
        items=items,
        customer=Customer("api-user", loyalty, tax_exempt),
        ship_to=Address(state, "00000"),
        shipping_method=shipping,
        coupon_code=coupon,
    )
    return OrderService().calculate(request)
