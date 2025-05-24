from .HanoiState import HanoiState

class Node:
    state: HanoiState
    children: list[HanoiState]
    def __init__(self, state: HanoiState):
        self.state = state