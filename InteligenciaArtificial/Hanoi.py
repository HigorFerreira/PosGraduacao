from hanoi_lib import HanoiState, Tree, Node

tree = Tree(Node(HanoiState([ 3, 2, 1 ])))

tree.mountTree(tree.root)

print(tree.root.get_children())
print(tree.root.get_children()[0].get_children())