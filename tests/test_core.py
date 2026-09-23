from conftest import ev
from fulfillment.domain.models import ShipmentStatus
def test_normal_lifecycle(app):
    p,s,_,i,n,_=app
    p.process(ev("e1",ShipmentStatus.CREATED,1))
    p.process(ev("e2",ShipmentStatus.PACKED,2))
    p.process(ev("e3",ShipmentStatus.SHIPPED,3))
    assert not i.is_reserved("order-1","sku-1")
    assert s.get("ship-1").status==ShipmentStatus.SHIPPED
    assert n.sent_for("e3")
def test_duplicate_is_ignored(app):
    p,_,_,i,n,a=app; e=ev("dup",ShipmentStatus.SHIPPED,3)
    assert p.process(e) is True; assert p.process(e) is False
    assert (len(i.release_calls),len(n.messages),len(a.records))==(1,1,1)
def test_older_does_not_rollback(app):
    p,s,_,i,n,a=app
    p.process(ev("new",ShipmentStatus.SHIPPED,3))
    before=(len(i.reserve_calls),len(i.release_calls),len(n.messages),len(a.records))
    assert p.process(ev("old",ShipmentStatus.PACKED,2)) is False
    assert before==(len(i.reserve_calls),len(i.release_calls),len(n.messages),len(a.records))
    assert s.get("ship-1").status==ShipmentStatus.SHIPPED
def test_distinct_lifecycle_events_apply(app):
    p,s,_,_,n,_=app
    assert p.process(ev("e1",ShipmentStatus.SHIPPED,3)) is True
    assert p.process(ev("e2",ShipmentStatus.DELIVERED,4)) is True
    assert s.get("ship-1").status==ShipmentStatus.DELIVERED
    assert len(n.messages)==2
