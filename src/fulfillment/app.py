from fulfillment.infrastructure.memory import *
from fulfillment.services.processor import ShipmentProcessor

def create_app():
    s=InMemoryShipments(); p=InMemoryProcessedEvents(); i=InMemoryInventory()
    n=InMemoryNotifications(); a=InMemoryAudit()
    return ShipmentProcessor(s,p,i,n,a),s,p,i,n,a
