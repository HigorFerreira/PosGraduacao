from hanoi_lib import HanoiState, Tree, Node

a=HanoiState([ 4, 3, 2, 1 ])
b=HanoiState([ 4, 3, 2, 1 ])
print(a.serialize())
print(b.serialize())
print(a == b)
with open("initial.svg", "w") as f: f.write(a.generateImage(label="Initial State"))
for i, state in enumerate(a.generatePossibleWays(), start=1):
    with open(f"child-{i}.svg", "w") as f: f.write(state.generateImage(label=f"Initial > Child[{i}]"))