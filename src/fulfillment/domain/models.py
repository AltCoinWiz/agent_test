from dataclasses import dataclass
from enum import IntEnum

class ShipmentStatus(IntEnum):
    CREATED=10
    PACKED=20
    SHIPPED=30
    DELIVERED=40
    CANCELLED=90

@dataclass(frozen=True)
class ShipmentEvent:
    event_id:str
    shipment_id:str
    order_id:str
    sku:str
    status:ShipmentStatus
    sequence:int

@dataclass
class Shipment:
    shipment_id:str
    order_id:str
    sku:str
    status:ShipmentStatus
    sequence:int
