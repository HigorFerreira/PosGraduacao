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
        
    # def __str__(self): return f'Node({self.value})'

    def __repr__(self): return f'Node({self.value})'

    
    # def __ge__(self, value: 'Node'): return self.value >= value.value
    # def __gt__(self, value: 'Node'): return self.value > value.value
    # def __le__(self, value: 'Node'): return self.value <= value.value
    # def __lt__(self, value: 'Node'): return self.value < value.value
    # def __eq__(self, value: 'Node'): return self.value == value.value