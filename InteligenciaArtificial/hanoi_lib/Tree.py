from hanoi_lib import Node

class Tree:
    root: Node
    def __init__(self, root: Node) -> None:
        self.root = root

    def mountTree(self, base: Node, level=1, maxLevel=10):
        if level == maxLevel: return
        ways = base.get_state().generatePossibleWays()
        ways = list(map(lambda x: Node(x), ways))
        base.set_children(ways)
        for child in base.get_children():
            self.mountTree(child, level+1, maxLevel)