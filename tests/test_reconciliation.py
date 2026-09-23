from decimal import Decimal
from conftest import event
from ledger.services.reconciliation import payment_totals
from ledger.domain.models import EntryType

def test_payment_totals_group_entries(app):
    service, ledger, _ = app
    service.accept(event("evt-1","pay-1","20"))
    service.accept(event("evt-2","pay-2","3",EntryType.DEBIT))
    totals = payment_totals(ledger.entries_for("acct-1"))
    assert totals == {"pay-1": Decimal("20.00"), "pay-2": Decimal("-3.00")}
