from copy import deepcopy
from .Node import Node

class BinaryTree:
    root: Node | None = None

    def insert(self, node: Node, parent: Node | None = None):
        if self.root is None: self.root = node; return deepcopy(node)
        if parent is None: parent = self.root

        if node < parent:
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
    
    def dfs(self, node: Node = None, action: Node = None):
        print('N ->', node, '   A ->', action)

        if action:
            print(action)
            if action.right is None: return self.dfs(None, action.parent)
            return

        if node is None: return self.dfs(self.root)
        if node.left is not None: return self.dfs(node.left)
        return self.dfs(None, node)

