from hanoi_lib import Block
from image_build import plot_game

class HanoiState:
    towers: list[list[Block]]
    def __init__(self, towerA: list[Block] = [], towerB: list[Block] = [], towerC: list[Block] = []):
        self.towers = [
            towerA,
            towerB,
            towerC,
        ]

    def isValid(self) -> bool:
        for tower in self.towers:
            for i, block in enumerate(tower):
                if i == 0: continue
                if block > tower[i-1]: return False
        return True

    def generatePossibleWays(self):
        pass

    def generateImage(self, x=0, y=0):
        return plot_game(self.towers)
    
    def serialize(self):
        return "\n".join(
            list(map(
                lambda blocks: "".join(list(map(lambda block: f"{block}", blocks))),
                self.towers
            ))
        )
    
    def __eq__(self, value):
        if type(value) != HanoiState: return False
        return self.serialize() == value.serialize()
    
    
class Node:
    state: HanoiState
    children: list[HanoiState]
    def __init__(self, state: HanoiState):
        self.state = state

class Tree:
    def __init__(self) -> None:
        pass



a=HanoiState([ 4, 3, 2, 1 ])
b=HanoiState([ 4, 3, 2, 1 ])
print(a.serialize())
print(b.serialize())
print(a == b)