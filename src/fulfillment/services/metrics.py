class Metrics:
    def __init__(self): self.values={}
    def increment(self,n): self.values[n]=self.values.get(n,0)+1
