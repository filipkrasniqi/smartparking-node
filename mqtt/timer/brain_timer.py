import time
from threading import Thread

import jsonpickle

from mqtt.log_thread import LogThread
import paho.mqtt.client as mqtt
from map.elements.node import Node


class BrainTimer(LogThread):
    def __init__(self, name, client: mqtt.Client, node: Node):
        LogThread.__init__(self, name)
        Thread.__init__(self, target=self.run)
        self.client = client
        self.node = node

    def run(self):
        while True:
            # execute change of status
            self.node.randomOccupancy()
            # read status and send
            self.client.publish("parking/node/occupancy", jsonpickle.encode(self.node.getOccupancyMessage()))
            time.sleep(10)
