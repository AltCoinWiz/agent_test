from decimal import Decimal
from conftest import event
from ledger.domain.models import EntryType

def test_credit_increases_balance(app):
    service, _, _ = app
    assert service.accept(event("evt-1","pay-1","25.00")) == Decimal("25.00")

def test_debit_reduces_balance(app):
    service, _, _ = app
    service.accept(event("evt-1","pay-1","50.00"))
    assert service.accept(event("evt-2","pay-2","10.00",EntryType.DEBIT)) == Decimal("40.00")

def test_accounts_are_isolated(app):
    service, _, _ = app
    service.accept(event("evt-1","pay-1","10.00",account="a"))
    service.accept(event("evt-2","pay-2","7.00",account="b"))
    assert service.get_balance("a") == Decimal("10.00")
    assert service.get_balance("b") == Decimal("7.00")
