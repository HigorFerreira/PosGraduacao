from .HanoiState import HanoiState

class Node:
    state: HanoiState
    children: list['Node'] = []
    def __init__(self, state: HanoiState):
        self.state = state

    def set_children(self, children: list['Node']):
        self.children = children

    def get_children(self): return self.children

    def get_state(self):
        return self.state