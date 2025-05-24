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
        # possible_states = []
        
        # # Para cada torre de origem
        # for from_tower in range(3):
        #     if not self.towers[from_tower]:  # Torre de origem vazia
        #         continue
                
        #     # O bloco do topo é o que pode ser movido
        #     block_to_move = self.towers[from_tower][-1]
            
        #     # Para cada torre de destino
        #     for to_tower in range(3):
        #         if from_tower == to_tower:  # Não pode mover para a mesma torre
        #             continue
                    
        #         # Verifica se o movimento é válido:
        #         # Torre de destino está vazia OU o bloco do topo é maior que o bloco a ser movido
        #         if (not self.towers[to_tower]) or (block_to_move < self.towers[to_tower][-1]):
        #             # Cria um novo estado
        #             new_state = HanoiState(*self.towers)
                    
        #             # Remove o bloco da torre de origem
        #             new_state.towers[from_tower] = new_state.towers[from_tower][:-1]
                    
        #             # Adiciona o bloco à torre de destino
        #             new_state.towers[to_tower].append(block_to_move)
                    
        #             # Adiciona o novo estado à lista de possíveis estados
        #             possible_states.append(new_state)
        
        # return possible_states
        pass

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
        if type(value) != HanoiState: return False
        return self.serialize() == value.serialize()
    
    