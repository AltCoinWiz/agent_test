class Replay:
    def __init__(self,p): self.processor=p
    def run(self,events): return sum(1 for e in events if self.processor.process(e))
