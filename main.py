from mqtt.publisher_thread import MQTTPublisher
from utils.parser import Parser


def start():
    # initializing nodes
    data_path = "assets/"
    parser = Parser(data_path).getInstance()
    node = parser.read_node()
    subscriberThread = MQTTPublisher("MQTT", node)
    subscriberThread.start()

if __name__ == "__main__":
    start()