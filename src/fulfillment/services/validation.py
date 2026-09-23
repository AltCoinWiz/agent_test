def valid_event(e): return bool(e.event_id and e.shipment_id and e.order_id and e.sku and e.sequence>=0)
