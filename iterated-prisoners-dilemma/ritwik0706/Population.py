from DNA import DNA
from random import randint


class Population:
    def __init__(self, crossover_rate, mut_rate, max_strategies):
        self.crossover_rate = crossover_rate
        self.mut_rate = mut_rate
        self.max_strategies = max_strategies
        self.population = []
        self.mating_pool = []
        self.generations = 0

        for i in range(0, max_strategies):
            self.population.append(DNA())

        self.calc_fitness()

    def calc_fitness(self):
        for i in range(0, len(self.population)):
            self.population[i].compute_fitness(self.population)

    def natural_selection(self):
        self.mating_pool.clear()

        for i in range(0, len(self.population)):
            fitness = int(self.population[i].fitness * 100)

            for j in range(0, fitness):
                self.mating_pool.append(self.population[i])

    def generate(self):
        for i in range(0, len(self.population)):
            a = randint(0, len(self.mating_pool)-1)
            b = randint(0, len(self.mating_pool)-1)
            partner_a = self.mating_pool[a]
            partner_b = self.mating_pool[b]
            child = partner_a.crossover(partner_b)
            child.mutate(self.mut_rate)
            self.population[i] = child

        self.generations += 1

    def get_best_strategy(self):
        max_fit = 0
        index = 0

        for i in range(0, len(self.population)):
            if self.population[i].fitness > max_fit:
                index = i
                max_fit = self.population[i].fitness

        return self.population[index].get_strategy()

    def get_num_of_generations(self):
        return self.generations

    def get_average_fitness(self):
        total = 0

        for i in range(0, len(self.population)):
            total += self.population[i].fitness

        return total / len(self.population)
