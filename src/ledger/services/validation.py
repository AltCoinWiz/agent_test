from decimal import Decimal

def valid_amount(amount: Decimal) -> bool:
    return amount >= Decimal("0")
