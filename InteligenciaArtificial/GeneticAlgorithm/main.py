from typing import Literal
from random import random
from copy import deepcopy
import numpy as np

class Individual:
    gens: list[bool]
    def __init__(self, gens: list[bool]):
        self.gens = gens

    
    def mutating(self, factor=0.2) -> 'Literal':
        def mutate_fn(x: bool):
            r = random()
            if r <= factor:
                return not x
            return x
        
        return Individual(list(map(mutate_fn, self.gens)))

    def crossover(self, pair: 'Individual'):
        genome1 = np.array(self.gens)
        genome2 = np.array(pair.gens)

        return Individual([ *genome1[0:int(len(genome1)/2)], *genome2[int(len(genome2)/2):len(genome2)] ])

    def fitness(self, benefit: list[int]):
        if len(benefit) != len(self.gens): raise Exception('Benefit array does not length of gens array')
        pass

    def __repr__(self):
        return " ".join(list(map(lambda x: str(int(x)), self.gens)))



i = Individual([ False, True, True, False, False, False, False, True ])
print(i)
print(i.mutating())