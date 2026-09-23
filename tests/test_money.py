from decimal import Decimal
from src.money import money


def test_money_rounds_half_up():
    assert money(Decimal("1.005")) == Decimal("1.01")
    assert money(Decimal("1.004")) == Decimal("1.00")
