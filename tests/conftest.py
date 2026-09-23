from decimal import Decimal
import pytest
from payments.app import create_app
from payments.domain.models import ProviderEvent,EventKind
@pytest.fixture
def app(): return create_app()
def ev(eid,pid,kind,amount,seq,merchant="m1"):
    return ProviderEvent(eid,pid,merchant,kind,Decimal(str(amount)),seq)
