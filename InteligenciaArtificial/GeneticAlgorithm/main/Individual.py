from random import random
import numpy as np
from .types import Gens, GensWithInts

class Individual:
    gens: Gens
    def __init__(self, gens: GensWithInts):
        self.gens = [
            [ bool(gen) for gen in gen_part ]
            for gen_part in gens
        ]

    @staticmethod
    def from_random(amount=100):
        def rand():
            return Individual([
                [ True if random() > 0.5 else False for _ in range(0, amount) ]
                for __ in range(0, 5)
            ])

        return rand()

    
    def mutating(self, factor=0.2) -> 'Individual':
        def mutate_fn(x: bool):
            r = random()
            if r <= factor:
                return not x
            return x  
        
        return Individual([
            [
                mutate_fn(gen)
                for gen in part
            ]
            for part in self.gens
        ])

    def crossover(self, pair: 'Individual'):
        new_genome = []
        for i, gen_part in enumerate(self.gens):
            if len(gen_part) != pair.gens[i]:
                raise Exception('Gen sizes doesn\'t fit pair')
            
        for i, gen_part in enumerate(self.gens):
            pair_part = pair.gens[i]

            genome_part1 = np.array(gen_part)
            genome_part2 = np.array(pair_part)
            
            new_genome.append([
                *genome_part1[0:int(len(genome_part1)/2)],
                *genome_part2[int(len(genome_part2)/2):len(genome_part2)]
            ])

        return Individual(new_genome)

    def fitness(self, weigth_constraints: list[int], benefits: list[int], costs: list[list[int]]) -> int:
        print(dict(weigth_constraints=weigth_constraints))
        print(dict(costs=costs))
        print(dict(benefits=benefits))
        # return
        if len(costs) != len(self.gens): raise Exception('Costs doesn\'t fit gens')
        if len(weigth_constraints) != len(self.gens): raise Exception('weigth_constraint doesn\' fit gen dimensions')
        for i, gen_part in enumerate(self.gens):
            if len(gen_part) != len(costs[i]): raise Exception(f'Cost part {i} doesn\'t fit gen[{i}]')
            if len(gen_part) != len(benefits): raise Exception('Benefits doesn\'t fit gen[{i}]')

        return sum([
            sum([
                int(gen)*benefits[j] * 1 if sum(costs[i]) > weigth_constraints[i] else 0
                for j, gen in enumerate(gen_part)
            ])
            for i, gen_part in enumerate(self.gens)
        ])
        

    def __repr__(self):
        return "\n".join([
            " ".join([
                str(int(gen)) for gen in part
            ])
            for part in self.gens
        ])