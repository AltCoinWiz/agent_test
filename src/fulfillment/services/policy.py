from fulfillment.domain.models import ShipmentStatus
def should_reserve(s): return s in {ShipmentStatus.CREATED,ShipmentStatus.PACKED}
def should_release(s): return s in {ShipmentStatus.SHIPPED,ShipmentStatus.DELIVERED,ShipmentStatus.CANCELLED}
def should_notify(s): return s in {ShipmentStatus.SHIPPED,ShipmentStatus.DELIVERED,ShipmentStatus.CANCELLED}
