import time
from threading import Thread

import paho.mqtt.client as mqtt

from map.elements.node import Node
from mqtt.log_thread import LogThread
from mqtt.timer.brain_timer import BrainTimer


class ConfigTimer(LogThread):
    def __init__(self, name, client: mqtt.Client, idNode, node: Node = None):
        LogThread.__init__(self, name)
        Thread.__init__(self, target=self.run)
        self.client = client
        self.node = node
        self.idNode = idNode
        self.brainTimer = None
        self.__keepRunning, self.__isRunning = True, False
        self.start()

    def run(self):
        self.__isRunning = True
        while self.__keepRunning:
            if self.node is None or not self.node.isReady():
                self.endOccupancyTimer()
                self.log("Attempting configuration...")
                self.client.publish("parking/node/configure", self.idNode)
                time.sleep(10)
            else:
                if self.brainTimer is None:
                    self.log("Configuration OK. Starting timer.")
                    # start occupancy timer
                    self.brainTimer = BrainTimer("BrainTimer", self.client, self.node)
                    self.brainTimer.start()
        self.__isRunning = False

    def setNode(self, node):
        self.node = node

    def endOccupancyTimer(self):
        if self.brainTimer is not None:
            self.brainTimer.kill()
            self.brainTimer = None