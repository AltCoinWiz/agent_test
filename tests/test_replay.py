from decimal import Decimal
from conftest import event
from ledger.services.replay_service import ReplayService

def test_replay_counts_only_new_events(app):
    service, ledger, _ = app
    replay = ReplayService(service.processor)
    batch = [event("evt-1","pay-1","5"), event("evt-2","pay-2","7")]
    assert replay.replay(batch) == 2
    assert replay.replay(batch) == 0
    assert service.get_balance("acct-1") == Decimal("12.00")
