from copy import deepcopy
from random import random
from .Individual import Individual
from toolz import pipe

class Population:
    size: int
    population: list[Individual]

    def __init__(self, size=100, population: list[Individual] | None = None):
        self.size = size
        if population is None:
            self.population = [
                Individual.from_random()
                for _ in range(0, size)
            ]
        else:
            self.population = population

    def selection(self, weigth_constraints: list[int], benefits: list[int], costs: list[list[int]]):
        new_popl = []
        popl = deepcopy(self.population)
        fitness = {}
        for i, individual in pipe(
            map(lambda x: x.fitness(weigth_constraints, benefits, costs),popl),
            list,
            enumerate
        ):
            fitness[i] = individual

        return fitness
        
        # popl.sort(key=lambda x: x.fitness(weigth_constraints, benefits, costs))


        # return Population(
        #     size=self.size,
        #     population=popl
        # )
        
    