from copy import deepcopy
class InMemoryShipments:
    def __init__(self): self.items={}
    def get(self,k):
        v=self.items.get(k); return deepcopy(v) if v else None
    def save(self,v): self.items[v.shipment_id]=deepcopy(v)
class InMemoryProcessedEvents:
    def __init__(self): self.ids=set()
    def contains(self,k): return k in self.ids
    def add(self,k): self.ids.add(k)
class InMemoryInventory:
    def __init__(self): self.reservations=set(); self.reserve_calls=[]; self.release_calls=[]
    def reserve(self,o,s): self.reserve_calls.append((o,s)); self.reservations.add((o,s))
    def release(self,o,s): self.release_calls.append((o,s)); self.reservations.discard((o,s))
    def is_reserved(self,o,s): return (o,s) in self.reservations
class InMemoryNotifications:
    def __init__(self): self.messages=[]
    def send(self,e,s,status): self.messages.append((e,s,status))
    def sent_for(self,e): return any(x[0]==e for x in self.messages)
class InMemoryAudit:
    def __init__(self): self.records=[]
    def append(self,e,s,a): self.records.append((e,s,a))
    def contains(self,e,a): return any(x[0]==e and x[2]==a for x in self.records)
