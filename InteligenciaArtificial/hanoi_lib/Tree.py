from hanoi_lib import Node
from typing import Callable

class Tree:
    root: Node
    def __init__(self, root: Node) -> None:
        self.root = root

    def mountTree(self, base: Node, level=1, maxLevel=12):
        if level == maxLevel: return
        ways = base.get_state().generatePossibleWays()
        ways = list(map(lambda x: Node(x), ways))
        base.set_children(ways)
        for child in base.get_children():
            self.mountTree(child, level+1, maxLevel)

    def dfs(self, start_node: Node, check: Callable[['Node'], bool]) -> tuple[bool, list[Node]]:
        counter = 0
        visited: set[str] = set()
        stack: list[Node] = []
        processed_stack: list[Node] = []

        stack.append(start_node)
        
        while True:
            if len(stack) == 0: return False, processed_stack
            node = stack.pop()
            if node.get_state().serialize() in visited: continue
            if not node.get_state().isValid(): continue

            # print(stack)
            visited.add(node.get_state().serialize())
            processed_stack.append(node)
            # print(processed_stack)
            stack = [ *stack, *node.get_children() ]
            # print(stack)
            # return processed_stack
            counter += 1
            if(check(node)): return True, processed_stack

