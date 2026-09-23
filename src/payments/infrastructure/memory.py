from copy import deepcopy
from decimal import Decimal
class Payments:
    def __init__(self): self.items={}
    def get(self,k):
        v=self.items.get(k); return deepcopy(v) if v else None
    def save(self,p): self.items[p.payment_id]=deepcopy(p)
class Processed:
    def __init__(self): self.ids=set()
    def contains(self,e): return e in self.ids
    def add(self,e): self.ids.add(e)
class Balances:
    def __init__(self): self.values={}; self.movements=[]
    def move(self,e,m,a):
        self.movements.append((e,m,a)); self.values[m]=self.values.get(m,Decimal("0"))+a
    def get(self,m): return self.values.get(m,Decimal("0"))
    def has_event(self,e): return any(x[0]==e for x in self.movements)
class Refunds:
    def __init__(self): self.rows=[]
    def add(self,e,p,a): self.rows.append((e,p,a))
    def contains(self,e): return any(x[0]==e for x in self.rows)
    def total_for(self,p): return sum((x[2] for x in self.rows if x[1]==p),Decimal("0"))
class Notifications:
    def __init__(self): self.rows=[]
    def send(self,e,p,msg): self.rows.append((e,p,msg))
    def contains(self,e): return any(x[0]==e for x in self.rows)
class Audit:
    def __init__(self): self.rows=[]
    def append(self,e,p,a): self.rows.append((e,p,a))
    def contains(self,e): return any(x[0]==e for x in self.rows)
