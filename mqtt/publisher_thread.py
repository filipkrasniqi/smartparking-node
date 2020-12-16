import collections
import socket
import threading
from concurrent.futures import thread
import time
from threading import Thread
import jsonpickle


import paho.mqtt.client as mqtt

from mqtt.log_thread import LogThread


import datetime

from mqtt.timer.brain_timer import BrainTimer
from mqtt.timer.config_timer import ConfigTimer

BROKER_IP = "80.211.69.17"

class MQTTPublisher(LogThread):

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe("parking/#")
        self.client.message_callback_add('parking/brain/configure', self.on_configure)

        # start timer persisting configuration
        if self.configTimer is None:
            self.configTimer = ConfigTimer("ConfigTimer", self.client, self.idNode)
            self.configTimer.start()

    def on_configure(self, client, userdata, msg):
        self.node = jsonpickle.decode(msg.payload)
        self.configTimer.setNode(self.node)
        self.node.setReady()

    def __init__(self, name, node):
        LogThread.__init__(self, name)

        # Initializing architecture stuff
        self.idNode = node.idNode

        # Initializing mqtt protocol
        self.client = mqtt.Client("node_{}".format(node.idNode))

        # self.client.tls_set(ca_certs="../keys/mosquitto.org.crt", certfile="../keys/client.crt",
        #                keyfile="../keys/client.key")

        self.client.username_pw_set(username="node", password="node")

        self.client.connect(BROKER_IP, 1883, 60)

        self.client.on_connect = self.on_connect

    def run(self):
        self.client.loop_forever()
