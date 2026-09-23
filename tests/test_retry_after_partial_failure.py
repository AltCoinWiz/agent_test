from decimal import Decimal
from conftest import event
from ledger.infrastructure.in_memory import InMemoryLedgerRepository, InMemoryEventRepository
from ledger.services.payment_processor import PaymentProcessor
from ledger.services.balance_service import BalanceService

class FailOnceEventRepository(InMemoryEventRepository):
    def __init__(self):
        super().__init__()
        self.failed = False

    def mark_processed(self, event_id: str) -> None:
        if not self.failed:
            self.failed = True
            raise RuntimeError("temporary persistence failure")
        super().mark_processed(event_id)

def test_retry_after_event_marker_failure_does_not_duplicate_money():
    ledger = InMemoryLedgerRepository()
    events = FailOnceEventRepository()
    processor = PaymentProcessor(ledger, events)
    e = event("evt-retry","pay-retry","19.95")

    try:
        processor.process(e)
    except RuntimeError:
        pass

    assert BalanceService(ledger).balance("acct-1") == Decimal("19.95")

    processor.process(e)

    assert BalanceService(ledger).balance("acct-1") == Decimal("19.95")
    assert len(ledger.entries_for("acct-1")) == 1
