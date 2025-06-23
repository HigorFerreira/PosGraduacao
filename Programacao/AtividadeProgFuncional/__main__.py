from copy import deepcopy
from typing import Callable, Literal, Optional


class Node(int):
    value: int
    parent: Optional['Node']
    right: Optional['Node']
    left: Optional['Node']

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
    # def __str__(self): return f'Node({self.value})'

    def __repr__(self): return f'Node({self.value})'

    
    def __ge__(self, value: 'Node'): return self.value >= value.value
    def __gt__(self, value: 'Node'): return self.value > value.value
    def __le__(self, value: 'Node'): return self.value <= value.value
    def __lt__(self, value: 'Node'): return self.value < value.value
    def __eq__(self, value: 'Node'): return self.value == value.value
    



class BinaryTree:
    root: Node | None = None

    def insert(self, node: Node, parent: Node | None = None):
        if self.root is None: self.root = node; return deepcopy(node)
        if parent is None: parent = self.root

        if node < parent:
            if parent.left is None:
                parent.left = node
                return deepcopy(node)
            return self.insert(node, parent.left)
        
        if parent.right is None:
            parent.right = node
            return deepcopy(node)
        return self.insert(node, parent.right)
    
    def dfs(self, node: Node = None):
        if node is None: return self.dfs(self.root)
        if node.left is not None: return self.dfs(node.left)
        print(node)
        if node.right is not None: return self.dfs(node.right)
        print(node)

