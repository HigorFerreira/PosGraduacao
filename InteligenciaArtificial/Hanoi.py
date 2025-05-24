from hanoi_lib import HanoiState, Tree, Node

a=HanoiState([ 4, 3 ], [], [ 2, 1 ])
with open("initial.svg", "w") as f: f.write(a.generateImage(label="Initial State"))
generated_ways = a.generatePossibleWays()
print(generated_ways)
for i, state in enumerate(generated_ways, start=1):
    with open(f"child-{i}.svg", "w") as f: f.write(state.generateImage(label=f"Initial > Child[{i}]"))