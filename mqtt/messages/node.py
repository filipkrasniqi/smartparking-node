class NodeMessage:
    def __init__(self, idNode, idParking):
        self.idNode = idNode
        self.idParking = idParking
class SlotMessage:
    def __init__(self, idSlot, occupied: bool):
        self.idSlot = idSlot
        self.occupied = occupied

class OccupancyMessage(NodeMessage):
    def __init__(self, idNode, idParking, slots):
        NodeMessage.__init__(self, idNode, idParking)
        self.slots = slots