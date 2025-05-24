from hlib import Block
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


a=HanoiState([ 3, 2, 1 ])
b=HanoiState([ 4, 3, 2, 1 ])
c=HanoiState([ 3, 1, 2 ])
d=HanoiState([ 1, 2, 3 ])

print(a.isValid())
print(b.isValid())
print(c.isValid())
print(d.isValid())

with open("a.svg", "w") as f: f.write(a.generateImage())
with open("b.svg", "w") as f: f.write(b.generateImage())
with open("c.svg", "w") as f: f.write(c.generateImage())
with open("d.svg", "w") as f: f.write(d.generateImage())

# Approved test

class Tree:
    def __init__(self) -> None:
        pass