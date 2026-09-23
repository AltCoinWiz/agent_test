from conftest import ev
from fulfillment.domain.models import ShipmentStatus

def test_shipments_are_independent(app):
    p,s,_,_,_,_=app
    p.process(ev("a1",ShipmentStatus.CREATED,1,"A","OA","A1"))
    p.process(ev("b1",ShipmentStatus.CREATED,1,"B","OB","B1"))
    p.process(ev("a2",ShipmentStatus.SHIPPED,2,"A","OA","A1"))
    assert s.get("A").status==ShipmentStatus.SHIPPED
    assert s.get("B").status==ShipmentStatus.CREATED
