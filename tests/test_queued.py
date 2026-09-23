from decimal import Decimal
from conftest import ev
from payments.domain.models import EventKind
def test_refund_before_capture_applies_after_capture(app):
    p,ps,d,b,r,n,a=app
    assert p.process(ev("r0","p1",EventKind.REFUND,"30",2)) is False
    p.process(ev("c","p1",EventKind.CAPTURED,"100",3))
    assert r.total_for("p1")==Decimal("30.00") and b.get("m1")==Decimal("70.00")
    assert n.contains("r0") and a.contains("r0")
def test_queued_refunds_never_over_refund(app):
    p,ps,_,b,r,_,_=app
    p.process(ev("r1","p1",EventKind.REFUND,"70",2)); p.process(ev("r2","p1",EventKind.REFUND,"60",3))
    p.process(ev("c","p1",EventKind.CAPTURED,"100",4))
    assert r.total_for("p1")<=Decimal("100.00")
    assert ps.get("p1").refunded<=ps.get("p1").captured
    assert b.get("m1")>=Decimal("0.00")
