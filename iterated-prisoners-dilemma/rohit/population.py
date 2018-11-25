from random import random, randint, choices
from DNA import DNA

class Population:
    def __init__(self, pc, pm):
        self.pc = pc
        self.pm = pm
        #self.num = num
        self.gen = 0
        self.population = []
        self.fitness = [0] * 20

        for _ in range(20):
            self.population.append(DNA("".join([str(randint(0, 1)) for _ in range(70)])))

        self.calculateFitness()

    def calculateFitness(self):
        for dna in self.population:
            dna.computeFitness(self.population, self.fitness)

    def naturalSelection(self):
        self.fitness = [0] * 20
        self.fitness = DNA("").computeFitness(self.population, self.fitness)

        parents = choices(self.population, self.fitness, k=20)
        self.population = []

        for i in range(0, 20, 2):
            if random() <= self.pc:
                self.population += parents[i].cross(parents[i+1])
            else:
                self.population += parents[i:i+2]

            self.population[-1].mutate(self.pm)
            self.population[-2].mutate(self.pm)
