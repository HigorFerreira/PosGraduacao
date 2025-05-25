from hanoi_lib import HanoiState, Tree, Node
import os

tree = Tree(Node(HanoiState([ 3, 2, 1 ])))

print("Mounting tree...")
tree.mountTree(tree.root)
print("Tree mountted")

def goalFunction(node: Node):
    towerA = node.get_state().towers[0]
    towerB = node.get_state().towers[0]
    towerC = node.get_state().towers[0]

    return (len(towerA) == 0 and len(towerB) == 0) or (len(towerA) == 0 and len(towerC) == 0)

print("Finding a path...")
path = tree.dfs(tree.root, lambda node: goalFunction(node))
print("Path found")

os.mkdir("path", 0o777)
for i, step in enumerate(path):
    with open(f"path/step-{i+1}.svg", "w") as f:
        f.write(step.get_state().generateImage(label=f"Passo {i+1}"))