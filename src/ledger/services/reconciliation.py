from collections import defaultdict
from decimal import Decimal
from ledger.domain.models import EntryType
from ledger.domain.money import money

def payment_totals(entries):
    totals = defaultdict(lambda: Decimal("0"))
    for entry in entries:
        sign = Decimal("1") if entry.entry_type == EntryType.CREDIT else Decimal("-1")
        totals[entry.payment_id] += sign * entry.amount
    return {k: money(v) for k, v in totals.items()}
