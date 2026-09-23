from decimal import Decimal
from commerce.api.facade import quote_order

def test_percent_coupon_does_not_reduce_tax_on_non_taxable_merchandise():
    t = quote_order([("KEYBOARD", 1), ("GIFT_CARD", 1)], "CA", coupon="SAVE10")
    assert t.merchandise == Decimal("130.00")
    assert t.discount == Decimal("13.00")
    assert t.taxable_amount == Decimal("72.00")
    assert t.tax == Decimal("5.22")
    assert t.total == Decimal("129.72")

def test_fixed_coupon_applies_to_taxable_merchandise_before_non_taxable_value():
    t = quote_order([("KEYBOARD", 1), ("GIFT_CARD", 1)], "CA", coupon="TAKE20")
    assert t.discount == Decimal("20.00")
    assert t.taxable_amount == Decimal("60.00")
    assert t.tax == Decimal("4.35")
    assert t.total == Decimal("121.85")

def test_gold_loyalty_with_mixed_cart_tax_base():
    t = quote_order([("KEYBOARD", 1), ("BOOK", 1)], "CA", loyalty="gold")
    assert t.discount == Decimal("5.00")
    assert t.taxable_amount == Decimal("76.00")
    assert t.tax == Decimal("5.51")
    assert t.total == Decimal("108.01")
