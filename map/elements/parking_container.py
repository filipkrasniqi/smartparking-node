from map.elements.node import Node

from map.elements.parking import Slot, Parking


class ParkingContainer:

    def __init__(self, nodes: list[Node], slots: list[Slot], parking: list[Parking]):
        # add slot to the corresponding node
        for node in nodes:
            currentNodeSlots = [slot for slot in slots if slot.idNode == node.idNode]
            node.setSlots(currentNodeSlots)

        # add node to the corresponding parking
        for park in parking:
            currentParkNodes = [node for node in nodes if node.idParking == park.idParking]
            park.setNodes(currentParkNodes)

        self.parking = parking

    '''
    Search in the parking list the node given the ID
    '''
    def getNodeGivenID(self, idNode):
        idxPark, found = 0, False
        # search in every park
        while not found and idxPark < len(self.parking):
            # search the node
            idxNode = 0
            while idxNode < len(self.parking[idxPark].nodes) and idNode != self.parking[idxPark].nodes[idxNode].idNode:
                idxNode += 1
            found = self.parking[idxPark].nodes[idxNode].idNode == idNode
            if not found:
                idxPark += 1
        assert found, "Wrong node"
        return self.parking[idxPark].nodes[idxNode]

