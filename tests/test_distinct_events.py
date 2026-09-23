from conftest import ev
from fulfillment.domain.models import ShipmentStatus

def test_distinct_lifecycle_events_are_applied(app):
    p,s,_,_,n,_=app
    assert p.process(ev("e1",ShipmentStatus.SHIPPED,3)) is True
    assert p.process(ev("e2",ShipmentStatus.DELIVERED,4)) is True
    assert s.get("ship-1").status==ShipmentStatus.DELIVERED
    assert len(n.messages)==2
