from ledger.domain.models import LedgerEntry
from ledger.domain.money import money
from ledger.services.id_factory import ledger_entry_id

class PaymentProcessor:
    def __init__(self, ledger, events):
        self.ledger = ledger
        self.events = events

    def process(self, event):
        if self.events.is_processed(event.event_id):
            return False

        entry = LedgerEntry(
            entry_id=ledger_entry_id(event.payment_id, event.event_id),
            account_id=event.account_id,
            payment_id=event.payment_id,
            amount=money(event.amount),
            entry_type=event.entry_type,
            source_event_id=event.event_id,
        )

        self.ledger.append(entry)
        self.events.mark_processed(event.event_id)
        return True
