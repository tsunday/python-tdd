import json

input_events = []


class OutputEvent:
    def __init__(self, type, id, stock):
        self.type = type
        self.id = id
        self.stock = stock


with open('data/input.json') as input_file:
    for line in input_file:
        input_events.append(json.loads(line))

with open('data/output.json', 'w') as output_file:
    output_file.write(json.dumps(OutputEvent('UpdateProduct', 2, 10).__dict__))
