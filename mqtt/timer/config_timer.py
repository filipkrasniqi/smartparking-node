import time
from threading import Thread

import paho.mqtt.client as mqtt

from map.elements.node import Node
from mqtt.log_thread import LogThread
from mqtt.timer.brain_timer import BrainTimer


class ConfigTimer(LogThread):
    def __init__(self, name, client: mqtt.Client, idNode):
        LogThread.__init__(self, name)
        Thread.__init__(self, target=self.run)
        self.client = client
        self.node = None
        self.idNode = idNode

    def run(self):
        while self.node is None or not self.node.isReady():
            self.log("Attempting configuration...")
            self.client.publish("parking/node/configure", self.idNode)
            time.sleep(5)
        self.log("Configuration OK")
        # start occupancy timer
        brainTimer = BrainTimer("BrainTimer", self.client, self.node)
        brainTimer.start()

    def setNode(self, node):
        self.node = node