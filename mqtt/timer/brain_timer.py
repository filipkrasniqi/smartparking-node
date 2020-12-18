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
        self.__keepRunning, self.__isRunning = True, False

    def run(self):
        self.__isRunning = True
        while self.__keepRunning:
            # execute change of status
            self.node.randomOccupancy()
            # read status and send
            self.client.publish("parking/node/occupancy", jsonpickle.encode(self.node.getOccupancyMessage()))
            time.sleep(10)
        self.__isRunning = False

    def stop(self):
        self.__keepRunning = False

    def kill(self):
        self.stop()
        while self.__isRunning:
            time.sleep(1)
