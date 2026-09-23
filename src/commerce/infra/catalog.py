from decimal import Decimal
from commerce.domain.models import Product

_PRODUCTS = {
    "KEYBOARD": Product("KEYBOARD", Decimal("80.00"), True),
    "MOUSE": Product("MOUSE", Decimal("25.00"), True),
    "GIFT_CARD": Product("GIFT_CARD", Decimal("50.00"), False),
    "BOOK": Product("BOOK", Decimal("20.00"), False),
}

def get_product(sku: str) -> Product:
    return _PRODUCTS[sku]
