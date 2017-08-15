import json

class Input:
    def __init__(self, event_source):
        event_source.add(self)

    def translate(self, event):
        return json.loads(event)
