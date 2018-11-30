import random
import Strategy
from Strategy import Strategy
from Game import play_iterated_game
import decimal


class DNA:
    def __init__(self):
        arr = [random.randint(0, 1) for _ in range(70)]
        self.genes = Strategy(arr)
        self.fitness = 0

    def get_strategy(self):
        return ''.join(str(x) for x in self.genes.encoding)

    def compute_fitness(self, population):
        score = 0.0
        for i in range(0, len(population)):
            for j in range(i, len(population)):
                x, y = play_iterated_game(population[i].genes, population[j].genes)
                score += x

        self.fitness = score / len(population)

    def crossover(self, partner):
        child = DNA()
        mid = random.randint(1, len(self.genes.encoding))
        child.genes.encoding = self.genes.encoding[:mid] + partner.genes.encoding[mid:]

        return child

    def mutate(self, mut_rate):
        for i in range(0, len(self.genes.encoding)):
            created_ran_num = decimal.Decimal(random.randrange(0, 100)) / 100

            if created_ran_num < mut_rate:
                self.genes.encoding = self.genes.encoding[:i] + [random.randint(0, 1)] + self.genes.encoding[i+1:]
