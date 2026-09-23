from decimal import Decimal
from commerce.domain.models import Customer
from commerce.utils.money import money

_RATES = {
    "AZ": Decimal("0.087"),
    "CA": Decimal("0.0725"),
    "TX": Decimal("0.0625"),
    "OR": Decimal("0"),
}

def calculate_tax(taxable_base: Decimal, state: str, customer: Customer) -> Decimal:
    if customer.tax_exempt:
        return Decimal("0.00")
    return money(taxable_base * _RATES.get(state.upper(), Decimal("0")))
