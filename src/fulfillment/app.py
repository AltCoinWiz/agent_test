from fulfillment.infrastructure.memory import *
from fulfillment.services.processor import ShipmentProcessor
def create_app():
    s=InMemoryShipments(); pe=InMemoryProcessedEvents(); i=InMemoryInventory()
    n=InMemoryNotifications(); a=InMemoryAudit()
    return ShipmentProcessor(s,pe,i,n,a),s,pe,i,n,a
