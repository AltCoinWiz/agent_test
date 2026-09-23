from decimal import Decimal
from .money import money


def calculate_tax(taxable_amount: Decimal, tax_rate: Decimal) -> Decimal:
    if tax_rate < 0:
        raise ValueError("tax rate cannot be negative")
    return money(taxable_amount * tax_rate)
