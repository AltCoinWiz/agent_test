from decimal import Decimal
from conftest import ev
from payments.domain.models import EventKind,PaymentStatus
def test_capture_moves_balance(app):
    p,ps,_,b,_,n,_=app; p.process(ev("e1","p1",EventKind.CAPTURED,"100",1))
    assert b.get("m1")==Decimal("100.00") and ps.get("p1").captured==Decimal("100.00") and n.contains("e1")
def test_refund_reduces_balance(app):
    p,ps,_,b,r,_,_=app; p.process(ev("c","p1",EventKind.CAPTURED,"100",1)); p.process(ev("r","p1",EventKind.REFUND,"25",2))
    assert (b.get("m1"),r.total_for("p1"),ps.get("p1").refunded)==(Decimal("75.00"),Decimal("25.00"),Decimal("25.00"))
def test_duplicate_capture_safe(app):
    p,_,_,b,_,n,a=app; e=ev("c","p1",EventKind.CAPTURED,"50",1)
    assert p.process(e) is True and p.process(e) is False
    assert b.get("m1")==Decimal("50.00") and len(b.movements)==len(n.rows)==len(a.rows)==1
def test_older_event_no_rollback(app):
    p,ps,_,b,_,_,_=app; p.process(ev("cap","p1",EventKind.CAPTURED,"40",5))
    assert p.process(ev("auth","p1",EventKind.AUTHORIZED,"40",3)) is False
    assert ps.get("p1").status==PaymentStatus.CAPTURED and b.get("m1")==Decimal("40.00")
def test_multiple_partial_refunds(app):
    p,ps,_,b,r,_,_=app; p.process(ev("c","p1",EventKind.CAPTURED,"100",1))
    p.process(ev("r1","p1",EventKind.REFUND,"20",2)); p.process(ev("r2","p1",EventKind.REFUND,"30",3))
    assert r.total_for("p1")==Decimal("50.00") and b.get("m1")==Decimal("50.00")
