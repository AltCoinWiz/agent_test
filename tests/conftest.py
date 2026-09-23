import pytest
from fulfillment.app import create_app
from fulfillment.domain.models import ShipmentEvent,ShipmentStatus

@pytest.fixture
def app(): return create_app()

def ev(eid,status,seq,shipment="ship-1",order="order-1",sku="sku-1"):
    return ShipmentEvent(eid,shipment,order,sku,status,seq)
