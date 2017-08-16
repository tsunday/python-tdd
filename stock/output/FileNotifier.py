import json

from stock.output.Notifier import Notifier


class FileNotifier(Notifier):
    def __init__(self, filepath):
        self.filepath = filepath

    def notify(self, message_obj):
        with open(self.filepath, 'w') as output_file:
            output_file.write(json.dumps(message_obj.__dict__))