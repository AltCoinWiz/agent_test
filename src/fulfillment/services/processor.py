from fulfillment.domain.models import Shipment
from fulfillment.services.policy import should_reserve,should_release,should_notify
from fulfillment.services.transition import is_newer

class ShipmentProcessor:
    def __init__(self,shipments,processed,inventory,notifications,audit):
        self.shipments=shipments; self.processed=processed; self.inventory=inventory
        self.notifications=notifications; self.audit=audit

    def process(self,event):
        if self.processed.contains(event.event_id):
            return False
        current=self.shipments.get(event.shipment_id)
        if not is_newer(event,current):
            self.processed.add(event.event_id)
            return False

        self.shipments.save(Shipment(event.shipment_id,event.order_id,event.sku,event.status,event.sequence))

        if should_reserve(event.status):
            self.inventory.reserve(event.order_id,event.sku)
        if should_release(event.status):
            self.inventory.release(event.order_id,event.sku)
        if should_notify(event.status):
            self.notifications.send(event.event_id,event.shipment_id,event.status.name)

        self.audit.append(event.event_id,event.shipment_id,f"status:{event.status.name}")
        self.processed.add(event.event_id)
        return True
