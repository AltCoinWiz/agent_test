from conftest import ev
from fulfillment.domain.models import ShipmentStatus

def test_older_event_does_not_roll_state_backward(app):
    p,s,_,_,_,_=app
    p.process(ev("new",ShipmentStatus.SHIPPED,3))
    p.process(ev("old",ShipmentStatus.PACKED,2))
    assert s.get("ship-1").status==ShipmentStatus.SHIPPED
    assert s.get("ship-1").sequence==3
