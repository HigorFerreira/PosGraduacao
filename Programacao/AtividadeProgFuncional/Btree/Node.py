from typing import Optional

class Node:
    value: int
    parent: Optional['Node']
    right: Optional['Node']
    left: Optional['Node']

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self): return f'Node({self.value})'