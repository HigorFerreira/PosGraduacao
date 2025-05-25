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
        states = []

        for i, tower in enumerate(self.towers):
            if len(tower) == 0:
                continue
            
            from_towers = set(range(len(self.towers)))
            from_towers.remove(i)

            old_tower = tower.copy()
            popped_block = old_tower.pop()
            for j in list(from_towers):
                new_towers = [
                    self.towers[0].copy(),
                    self.towers[1].copy(),
                    self.towers[2].copy(),
                ]
                new_towers[i] = old_tower
                new_towers[j].append(popped_block)
                states.append(HanoiState(
                    new_towers[0],
                    new_towers[1],
                    new_towers[2],
                ))

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
        
    
    