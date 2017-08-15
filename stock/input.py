import json

SUPPORTED_EVENTS = {
    'ProductCreated': [('type', str), ('id', int), ('stock', int), ('timestamp', int), ('parent_id', int)],
    'ProductUpdated': [('type', str), ('id', int), ('stock', int), ('timestamp', int)],
    'ProductEnded': [('type', str), ('id', int), ('timestamp', int)]
}

NULLABLE_FIELDS = ['parent_id']


class Input:
    def __init__(self, event_source):
        event_source.add(self)

    def translate(self, event):
        translated_event = json.loads(event)
        self.verify_event(translated_event)
        return translated_event

    def verify_event(self, event):
        self.check_event_type(event)
        self.check_fields(event)

    def check_event_type(self, event):
        return list(SUPPORTED_EVENTS.keys()).index(event['type'])

    def check_fields(self, event):
        for key, expected_type in SUPPORTED_EVENTS[event['type']]:
            list(event.keys()).index(key)
            if self.check_none(key, event[key]):
                continue
            self.check_value_type(event[key], expected_type)

    def check_value_type(self, value, expected_type):
        if type(value) is not expected_type:
            raise TypeError

    def check_none(self, key, value):
        return value is None and key in NULLABLE_FIELDS
