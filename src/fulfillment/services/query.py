class ShipmentQuery:
    def __init__(self,r): self.repo=r
    def status(self,k):
        x=self.repo.get(k); return x.status if x else None
