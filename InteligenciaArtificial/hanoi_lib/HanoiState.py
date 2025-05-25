from .types import Block
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

    def generatePossibleWays(self) -> list['HanoiState']:
        states: list['HanoiState'] = []
        towers = [
            self.towers[0].copy(),
            self.towers[1].copy(),
            self.towers[2].copy(),
        ]

        for i, tower in enumerate(towers):
            tower_indexes = set(range(3))
            tower_indexes.remove(i)
            for j in tower_indexes:
                target_tower = towers[j]
                if len(tower) == 0: break
                block = tower.pop()
                target_tower.append(block)
                states.append(HanoiState(towers[0], towers[1], towers[2]))

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
        
    
    