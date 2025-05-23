
from typing import Literal


Block=Literal[1, 2, 3, 4]

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
        pass


print(HanoiState([ 3, 2, 1 ]).isValid())
print(HanoiState([ 4, 3, 2, 1 ]).isValid())
print(HanoiState([ 3, 1, 2 ]).isValid())
print(HanoiState([ 1, 2, 3 ]).isValid())

# Approved test

class Tree:
    def __init__(self) -> None:
        pass