class ReplayService:
    def __init__(self, processor):
        self.processor = processor

    def replay(self, events):
        applied = 0
        for event in events:
            if self.processor.process(event):
                applied += 1
        return applied
