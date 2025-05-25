from hanoi_lib import HanoiState, Tree, Node

tree = Tree(Node(HanoiState([ 3, 2, 1 ])))

tree.mountTree(tree.root)

path = tree.dfs(tree.root, lambda node: len(node.get_state().towers[0]) == 0)
print("\n\nPATH", path)

with open('test.svg', 'w') as f: f.write(path[0].get_state().generateImage())
with open('test1.svg', 'w') as f: f.write(path[-1].get_state().generateImage())