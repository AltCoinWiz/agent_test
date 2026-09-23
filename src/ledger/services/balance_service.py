from decimal import Decimal
from ledger.domain.models import EntryType
from ledger.domain.money import money

class BalanceService:
    def __init__(self, ledger):
        self.ledger = ledger

    def balance(self, account_id: str) -> Decimal:
        total = Decimal("0")
        for entry in self.ledger.entries_for(account_id):
            if entry.entry_type == EntryType.CREDIT:
                total += entry.amount
            else:
                total -= entry.amount
        return money(total)
