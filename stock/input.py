import json

SUPPORTED_EVENTS = {
    'ProductCreated': ['type', 'id', 'stock', 'timestamp', 'parent_id'],
    'ProductUpdated': ['type', 'id', 'stock', 'timestamp'],
    'ProductEnded': ['type', 'id', 'timestamp']
}


class Input:
    def __init__(self, event_source):
        event_source.add(self)

    def translate(self, event):
        translated_event = json.loads(event)
        self.check_type(translated_event)
        self.check_fields(translated_event)
        return translated_event

    def check_type(self, event):
        return list(SUPPORTED_EVENTS.keys()).index(event['type'])

    def check_fields(self, event):
        for key in SUPPORTED_EVENTS[event['type']]:
            list(event.keys()).index(key)
