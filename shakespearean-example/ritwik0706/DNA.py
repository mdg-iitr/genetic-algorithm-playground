import random
import decimal


class DNA:
    def __init__(self, num):
        self.genes = ''
        self.fitness = 0

        for i in range(0, num):
            self.genes += chr(random.randint(32, 128))

    def get_phrase(self):
        return self.genes

    def compute_fitness(self, target):
        score = 0.0
        for i in range(0, len(self.genes)):
            if self.genes[i].__eq__(target[i]):
                score += 1

        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        mid = random.randint(1, len(self.genes))
        child.genes = self.genes[:mid] + partner.genes[mid:]

        return child

    def mutate(self, mut_rate):
        for i in range(0, len(self.genes)):
            created_ran_num = decimal.Decimal(random.randrange(0, 100)) / 100

            if created_ran_num < mut_rate:
                self.genes = self.genes[:i] + chr(random.randint(32, 128)) + self.genes[i+1:]
