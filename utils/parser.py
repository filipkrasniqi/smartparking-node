from utils.node import Node


class Parser:
    class __Parser:
        def __init__(self, data_dir):
            self.data_dir = data_dir

        def parse_node(self, idx, node):
            splits = list(filter(lambda x : x != "", node.replace("\n", "").split(" ")))
            assert len(splits) == 1, "Wrong init of node"
            return Node(idx, int(splits[0]))

        def read_node(self):
            with open(self.data_dir+"node.txt", "r") as nodes_data:
                for i, data in enumerate(nodes_data):
                    idNode = int(data.replace("\n", ""))
                    node = Node(idNode)
            return node

    __instance = None

    def __init__(self, data_dir):
        if not Parser.__instance:
            Parser.__instance = Parser.__Parser(data_dir)
        else:
            Parser.__instance.data_dir = data_dir

    def __getattr__(self, name):
        return getattr(self.__instance, name)

    def getInstance(self):
        return Parser.__instance