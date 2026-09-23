from decimal import Decimal
from commerce.api.facade import quote_order

def test_oregon_has_no_tax():
    t = quote_order([("KEYBOARD", 1)], "OR")
    assert t.merchandise == Decimal("80.00")
    assert t.shipping == Decimal("7.50")
    assert t.tax == Decimal("0.00")
    assert t.total == Decimal("87.50")

def test_free_shipping_threshold():
    t = quote_order([("KEYBOARD", 2)], "OR")
    assert t.shipping == Decimal("0.00")
    assert t.total == Decimal("160.00")

def test_tax_exempt_customer():
    t = quote_order([("KEYBOARD", 1)], "AZ", tax_exempt=True)
    assert t.tax == Decimal("0.00")
    assert t.total == Decimal("87.50")

def test_unknown_coupon_is_ignored():
    t = quote_order([("MOUSE", 2)], "OR", coupon="NOPE")
    assert t.discount == Decimal("0.00")
    assert t.total == Decimal("57.50")
