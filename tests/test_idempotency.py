from decimal import Decimal
from conftest import event

def test_exact_duplicate_event_is_idempotent(app):
    service, ledger, _ = app
    e = event("evt-100","pay-100","12.50")
    service.accept(e)
    service.accept(e)
    assert service.get_balance("acct-1") == Decimal("12.50")
    assert len(ledger.entries_for("acct-1")) == 1

def test_distinct_payments_with_same_amount_are_both_applied(app):
    service, ledger, _ = app
    service.accept(event("evt-a","pay-a","10"))
    service.accept(event("evt-b","pay-b","10"))
    assert service.get_balance("acct-1") == Decimal("20.00")
    assert len(ledger.entries_for("acct-1")) == 2
