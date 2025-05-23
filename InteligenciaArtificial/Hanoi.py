
from typing import Literal


Block=Literal[1] | Literal[2] | Literal[3] | Literal[4]

class HanoiState:
    towers: list[list[Block]]
    def __init__(self, towerA: list[Block], towerB: list[Block], towerC: list[Block]):
        self.towers = [
            towerA,
            towerB,
            towerC,
        ]

    def isValid() -> bool:
        
        return True