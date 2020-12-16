from map.elements.node import *
from map.elements.position import Position


class Parking(Position):
    def __init__(self, idParking, latitude, longitude, name):
        Position.__init__(self, latitude, longitude, name)
        self.idParking = idParking
        self.nodes: list[Node] = []

    def setNodes(self, nodes):
        self.nodes = nodes

# useful when we want to guide the user inside the slot
class Slot(Position):
    def __init__(self, idSlot, idNode, latitude, longitude, name = ""):
        Position.__init__(self, latitude, longitude, name)
        self.idSlot = idSlot
        self.idNode = idNode