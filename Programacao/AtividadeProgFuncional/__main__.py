


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

        parent_node = self.walk(
            lambda nd: 'left' if node.value <= nd.value else 'right',
            self.root
        )

        left = node.value <= parent_node.value
        if left:
            parent_node.left
        else:
            parent_node.right = node

        node.parent = parent_node

    def walk(self, callback: Callable[[Node], Literal['right', 'left']], prev_node: Node | None = None, node: Node | None = None):
        if node is None: return self.walk(callback, self.root, self.root)
        
        result = callback(node)
        match result:
            case 'right':
                right = node.right
                if right is None: return prev_node
                return self.walk(callback, prev_node, right)
            case 'left':
                left = node.left
                if left is None: return prev_node
                return self.walk(callback, prev_node, left)
            
a = Node(5)
b = Node(2)
c = Node(5)

print(a)
print(b)
print(a == b)
print()
print(a > b)
print(a < b)
print()
print(a > c)
print(a >= c)