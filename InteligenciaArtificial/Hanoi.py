from hanoi_lib import HanoiState, Tree, Node

tree = Tree(Node(HanoiState([ 3, 2, 1 ])))

tree.mountTree(tree.root)

def goalFunction(node: Node):
    towerA = node.get_state().towers[0]
    towerB = node.get_state().towers[0]
    towerC = node.get_state().towers[0]

    return len(towerA) == 0 and len(towerB) == 0\
        or len(towerA) == 0 and len(towerC) == 0


path = tree.dfs(tree.root, lambda node: goalFunction(node))
print("\n\nPATH", path)

with open('test.svg', 'w') as f: f.write(path[0].get_state().generateImage())
with open('test1.svg', 'w') as f: f.write(path[-1].get_state().generateImage())