from hanoi_lib import HanoiState, Tree, Node

a=HanoiState([ 4, 3, 2, 1 ])
b=HanoiState([ 4, 3, 2, 1 ])
print(a.serialize())
print(b.serialize())
print(a == b)