


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
        
    def __str__(self): return f'Node({self.value})'

    
    def __ge__(self, value: 'Node'): return self.value >= value.value
    def __gt__(self, value: 'Node'): return self.value > value.value
    def __le__(self, value: 'Node'): return self.value <= value.value
    def __lt__(self, value: 'Node'): return self.value < value.value
    def __eq__(self, value: 'Node'): return self.value == value.value
    



class BinaryTree:
    root: Node | None = None

    def insert(self, node: Node):
        if self.root is None: self.root = node; return None