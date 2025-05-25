from hanoi_lib import HanoiState, Tree, Node
import os
import shutil

if not os.path.exists(os.path.join(os.getcwd(), 'path')):
    os.mkdir("path", 0o777)


# test_tower_a = [ 4, 3, 2, 1 ]
# imutable = HanoiState(test_tower_a)
# test_tower_a.pop()
# test_tower_a.pop()
# with open(f"path/test-imutable.svg", "w") as f: f.write(imutable.generateImage())
# input("Type anything to delete path")
# shutil.rmtree(os.path.join(os.getcwd(), "path"), ignore_errors=True)
# exit(0)

test = HanoiState([ 2 ], [ 1 ])
with open(f"path/test-1.svg", "w") as f: f.write(test.generateImage())

for i, case in enumerate(test.generatePossibleWays(), start=1):
    with open(f"path/test-{i+1}.svg", "w") as f: f.write(case.generateImage())

input("Type anything to delete path")
shutil.rmtree(os.path.join(os.getcwd(), "path"), ignore_errors=True)
exit(0)

tree = Tree(Node(HanoiState([ 3, 2, 1 ])))

print("Mounting tree...")
tree.mountTree(tree.root)
print("Tree mountted")

def goalFunction(node: Node):
    towerA = node.get_state().towers[0]
    towerB = node.get_state().towers[1]
    towerC = node.get_state().towers[2]

    return len(towerA) == 0 and len(towerB) == 0 or len(towerA) == 0 and len(towerC) == 0

print("Finding a path...")
sucess, path = tree.dfs(tree.root, lambda node: goalFunction(node))
if sucess: print("Path found")
else: print("No path found")

for i, step in enumerate(path):
    with open(f"path/step-{i+1}.svg", "w") as f:
        f.write(step.get_state().generateImage(label=f"Passo {i+1}"))

input("Type anything to delete path")
shutil.rmtree(os.path.join(os.getcwd(), "path"), ignore_errors=True)