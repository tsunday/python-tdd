class Observer:
    def __init__(self):
        self.update_counter = 0

    def update(self, body):
        self.update_counter += 1
        print('callback called')
