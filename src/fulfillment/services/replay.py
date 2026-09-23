class ReplayService:
    def __init__(self,p): self.processor=p
    def replay(self,events): return sum(1 for e in events if self.processor.process(e))
