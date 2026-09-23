from decimal import Decimal
from commerce.api.facade import quote_order

def test_percentage_coupon():
    t = quote_order([("KEYBOARD", 1)], "OR", coupon="SAVE10")
    assert t.discount == Decimal("8.00")
    assert t.total == Decimal("79.50")

def test_fixed_coupon_minimum_not_met():
    t = quote_order([("MOUSE", 2)], "OR", coupon="TAKE20")
    assert t.discount == Decimal("0.00")

def test_fixed_coupon_when_minimum_met():
    t = quote_order([("KEYBOARD", 1), ("MOUSE", 1)], "OR", coupon="TAKE20")
    assert t.discount == Decimal("20.00")
    assert t.total == Decimal("92.50")

def test_coupon_then_gold_loyalty():
    t = quote_order([("KEYBOARD", 1)], "OR", coupon="SAVE10", loyalty="gold")
    assert t.discount == Decimal("11.60")
    assert t.total == Decimal("75.90")
