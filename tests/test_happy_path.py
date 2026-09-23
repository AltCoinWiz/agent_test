from conftest import ev
from fulfillment.domain.models import ShipmentStatus

def test_normal_lifecycle(app):
    p,s,_,i,n,_=app
    p.process(ev("e1",ShipmentStatus.CREATED,1))
    assert i.is_reserved("order-1","sku-1")
    p.process(ev("e2",ShipmentStatus.PACKED,2))
    p.process(ev("e3",ShipmentStatus.SHIPPED,3))
    assert not i.is_reserved("order-1","sku-1")
    assert s.get("ship-1").status==ShipmentStatus.SHIPPED
    assert n.sent_for("e3")

def test_delivered_updates_state(app):
    p,s,*_=app
    p.process(ev("e1",ShipmentStatus.CREATED,1))
    p.process(ev("e2",ShipmentStatus.DELIVERED,2))
    assert s.get("ship-1").status==ShipmentStatus.DELIVERED
