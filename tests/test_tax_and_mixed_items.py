from decimal import Decimal
from commerce.api.facade import quote_order

def test_az_tax_includes_shipping():
    t = quote_order([("MOUSE", 1)], "AZ")
    assert t.taxable_amount == Decimal("32.50")
    assert t.tax == Decimal("2.83")
    assert t.total == Decimal("35.33")

def test_non_taxable_items_remain_non_taxable():
    t = quote_order([("BOOK", 2)], "CA")
    assert t.taxable_amount == Decimal("0.00")
    assert t.tax == Decimal("0.00")
    assert t.total == Decimal("47.50")

def test_mixed_cart_without_discount():
    t = quote_order([("KEYBOARD", 1), ("GIFT_CARD", 1)], "CA")
    assert t.taxable_amount == Decimal("80.00")
    assert t.tax == Decimal("5.80")
    assert t.total == Decimal("143.30")
