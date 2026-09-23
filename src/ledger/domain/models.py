from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

class EntryType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"

@dataclass(frozen=True)
class PaymentEvent:
    event_id: str
    account_id: str
    payment_id: str
    amount: Decimal
    entry_type: EntryType

@dataclass(frozen=True)
class LedgerEntry:
    entry_id: str
    account_id: str
    payment_id: str
    amount: Decimal
    entry_type: EntryType
    source_event_id: str
