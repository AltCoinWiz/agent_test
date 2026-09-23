from decimal import Decimal
import pytest
from ledger.app import create_app
from ledger.domain.models import PaymentEvent, EntryType

@pytest.fixture
def app():
    return create_app()

def event(event_id, payment_id, amount, kind=EntryType.CREDIT, account="acct-1"):
    return PaymentEvent(
        event_id=event_id,
        account_id=account,
        payment_id=payment_id,
        amount=Decimal(str(amount)),
        entry_type=kind,
    )
