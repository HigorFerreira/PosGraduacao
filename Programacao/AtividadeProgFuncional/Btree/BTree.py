from copy import deepcopy
from typing import Callable
from .Node import Node

class BinaryTree:
    root: Node | None = None

    def __init__(self, arr: list[int]):
        for i in arr:
            self.insert(Node(i))

    def insert(self, node: Node, parent: Node | None = None):
        if self.root is None: self.root = node; return deepcopy(node)
        if parent is None: parent = self.root

        if node.value < parent.value:
            if parent.left is None:
                node.parent = parent
                parent.left = node
                return deepcopy(node)
            return self.insert(node, parent.left)
        
        if parent.right is None:
            node.parent = parent
            parent.right = node
            return deepcopy(node)
        return self.insert(node, parent.right)
    
    def inOrderWalk(self, callback: Callable[[Node], None] | None = None):
        def inOrderRecursive(node: Node | None):
            if node is not None:
                inOrderRecursive(node.left)
                if callback: callback(deepcopy(node))
                inOrderRecursive(node.right)

        inOrderRecursive(self.root)