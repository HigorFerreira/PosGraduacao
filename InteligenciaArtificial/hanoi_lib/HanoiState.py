from .types import Block
from image_build import plot_game

class HanoiState:
    towers: list[list[Block]]
    def __init__(self, towerA: list[Block] = [], towerB: list[Block] = [], towerC: list[Block] = []):
        self.towers = [
            towerA.copy(),
            towerB.copy(),
            towerC.copy(),
        ]

    def isValid(self) -> bool:
        for tower in self.towers:
            for i, block in enumerate(tower):
                if i == 0: continue
                if block > tower[i-1]: return False
        return True

    def generatePossibleWays(self) -> list['HanoiState']:
        states: list['HanoiState'] = []

        for i in range(len(self.towers)):
            towers = list(map(lambda tower: tower.copy(), self.towers))
            indexes = set(range(len(self.towers)))
            indexes.remove(i)
            if len(towers[i]) == 0: continue
            block = towers[i].pop()
            for j in indexes:
                towers[j].append(block)
                states.append(HanoiState(
                    towers[0],
                    towers[1],
                    towers[2],
                ))
                # towers[j].pop()
                # towers[i].append(block)

        return states

    def generateImage(self, x=0, y=0, label=""):
        return plot_game(self.towers, label=label)
    
    def serialize(self):
        return "\n".join(
            list(map(
                lambda blocks: "".join(list(map(lambda block: f"{block}", blocks))),
                self.towers
            ))
        )
    
    def __eq__(self, value):
        if type(value) == HanoiState: return self.serialize() == value.serialize()
        elif type(value) == str: return self.serialize() == value
        else: return False
        
    
    