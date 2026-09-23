from conftest import ev
from fulfillment.domain.models import ShipmentStatus

def test_exact_duplicate_event_is_ignored(app):
    p,_,_,i,n,a=app
    e=ev("dup",ShipmentStatus.SHIPPED,3)
    assert p.process(e) is True
    assert p.process(e) is False
    assert len(i.release_calls)==1 and len(n.messages)==1 and len(a.records)==1
