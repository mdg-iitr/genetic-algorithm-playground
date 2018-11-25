from random import random, randint
from strategy import Strategy
from game import playIteratedGame

class DNA:
    def __init__(self, genes="".join([str(randint(0, 1)) for _ in range(70)])):
        self.genes = Strategy(genes)
        self.fitness = [0] * 20

    def __str__(self):
        return self.genes.encoding

    def cross(self, partner):
        mid = randint(1, len(self.genes.encoding))
        offspring1 = DNA(self.genes.encoding[:mid] + partner.genes.encoding[mid:])
        offspring2 = DNA(self.genes.encoding[mid:] + partner.genes.encoding[:mid])
        return [offspring1, offspring2]

    def mutate(self, rate):
        self.genes.encoding = "".join([str(1 ^ int(bit)) if random() <= rate else bit for bit in self.genes.encoding])

    def computeFitness(self, population, fitness):
        for i in range(0, 20):
            for j in range(i, 20):
                avgScoreI, avgScoreJ = playIteratedGame(population[i].genes, population[j].genes)
                fitness[i] += avgScoreI
                fitness[j] += avgScoreJ

        fitness = [f / 20 for f in fitness]
        return fitness
