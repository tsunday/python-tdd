from stock.input.file_event_source import FileEventSource
from stock.input.input_handler import InputHandler
from stock.output.FileNotifier import FileNotifier
from stock.products.product_controller import ProductController

if __name__ == '__main__':
    event_source = FileEventSource('../data/input.json')
    input = InputHandler(event_source)
    output = FileNotifier('../data/output.json')
    products = ProductController(input, output)

    event_source.consume()
    products.send_summary()
