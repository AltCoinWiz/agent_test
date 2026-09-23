import pytest
from conftest import ev
from fulfillment.domain.models import ShipmentStatus
from fulfillment.infrastructure.memory import *
from fulfillment.services.processor import ShipmentProcessor

class FailOnceProcessed(InMemoryProcessedEvents):
    def __init__(self): super().__init__(); self.fail=True
    def add(self,e):
        if self.fail:
            self.fail=False
            raise RuntimeError("processed-event store unavailable")
        super().add(e)

def test_retry_after_processed_marker_failure_has_no_duplicate_side_effects():
    s=InMemoryShipments(); pe=FailOnceProcessed(); i=InMemoryInventory()
    n=InMemoryNotifications(); a=InMemoryAudit()
    p=ShipmentProcessor(s,pe,i,n,a); e=ev("ship-event",ShipmentStatus.SHIPPED,3)
    with pytest.raises(RuntimeError): p.process(e)
    p.process(e)
    assert s.get("ship-1").status==ShipmentStatus.SHIPPED
    assert len(i.release_calls)==1
    assert len(n.messages)==1
    assert len(a.records)==1
