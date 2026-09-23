from decimal import Decimal
from conftest import ev
from payments.domain.models import EventKind
def test_payments_independent(app):
    p,_,_,b,r,_,_=app
    p.process(ev("c1","p1",EventKind.CAPTURED,"80",1,"m1")); p.process(ev("c2","p2",EventKind.CAPTURED,"50",1,"m2"))
    p.process(ev("r1","p1",EventKind.REFUND,"20",2,"m1"))
    assert b.get("m1")==Decimal("60.00") and b.get("m2")==Decimal("50.00") and r.total_for("p2")==Decimal("0")
