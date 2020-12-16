from enum import Enum

import json
import random

from map.elements.parking import Slot
from map.elements.position import Position
from mqtt.messages.node import OccupancyMessage, SlotMessage


class Node:
    def __init__(self, idNode, idParking):
        self.idNode = idNode
        self.idParking = idParking
        self.slots: list[Slot] = []
        self.status = NodeStatus.TO_CONFIGURE

    def setSlots(self, slots):
        self.slots = slots

    def randomOccupancy(self):
        # randomly assign whether slot is occupied or not
        for slot in self.slots:
            slot.setOccupied(random.choice([False, True]))

    def setReady(self):
        self.status = NodeStatus.READY

    def isReady(self):
        return self.status == NodeStatus.READY

    def getOccupancyMessage(self):
        return OccupancyMessage(self.idNode, self.idNode, [SlotMessage(slot.idSlot, slot.occupied) for slot in self.slots])

class NodeStatus(Enum):
    TO_CONFIGURE = 1
    READY = 2

# useful when we want to guide the user inside the slot
class Slot(Position):
    def __init__(self, idSlot, idNode, latitude, longitude, name = ""):
        Position.__init__(self, latitude, longitude, name)
        self.idSlot = idSlot
        self.idNode = idNode
        self.occupied = False

    def setOccupied(self, occupied: bool):
        self.occupied = occupied