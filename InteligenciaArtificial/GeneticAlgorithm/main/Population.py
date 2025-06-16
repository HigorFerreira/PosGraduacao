from copy import deepcopy
from random import random
from .Individual import Individual
from toolz import pipe
from .utils import intervals

class Population:
    size: int
    population: list[Individual]

    def __init__(self, size=100, individual_size=100, population: list[Individual] | None = None):
        self.size = size
        if population is None:
            self.population = [
                Individual.from_random(individual_size)
                for _ in range(0, size)
            ]
        else:
            self.population = population

    def selection(self, weigth_constraints: list[int], benefits: list[int], costs: list[list[int]]):
        ppl = deepcopy(self.population)
        ppl_sorted: list[Individual] = []
        fitness_arr = [ el.fitness(weigth_constraints, benefits, costs) for el in ppl ]
        fitness_arr_sorted = sorted(enumerate(fitness_arr), key=lambda x: x[1])
        
        total_fitness = sum([ val for _, val in fitness_arr_sorted ])
        fitness_arr_sorted_percent = [ (i, val/total_fitness) for i, val in fitness_arr_sorted ]

        for i, _ in fitness_arr_sorted:
            ppl_sorted.append(ppl[i])

        new_ppl: list[Individual] = []
        fitness_intervals = intervals([ val for _, val in fitness_arr_sorted_percent ])
        
        for _ in range(self.size):
            r = random()
            for i, itv in enumerate(fitness_intervals):
                inf, sup = itv
                if r >= inf and r < sup:
                    new_ppl.append(deepcopy(ppl_sorted[i]))
                    break

        return Population(size=self.size, population=new_ppl)
