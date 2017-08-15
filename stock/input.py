import json

SUPPORTED_TYPES = ['ProductCreated', 'ProductUpdated', 'ProductEnded']


class Input:
    def __init__(self, event_source):
        event_source.add(self)

    def translate(self, event):
        translated_event = json.loads(event)
        self.check_type(translated_event)
        return translated_event

    def check_type(self, event):
        return SUPPORTED_TYPES.index(event['type'])
