SUPPORTED_EVENTS = {
    'ProductCreated': [('type', str), ('id', int), ('stock', int), ('timestamp', int), ('parent_id', int)],
    'ProductUpdated': [('type', str), ('id', int), ('stock', int), ('timestamp', int)],
    'ProductEnded': [('type', str), ('id', int), ('timestamp', int)]
}

NULLABLE_FIELDS = ['parent_id']