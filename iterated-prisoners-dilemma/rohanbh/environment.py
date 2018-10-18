import random
from game import play_iterated_game
from strategy import Strategy

def crossover(parent1, parent2):
    """Do a crossover a return two offsprings"""
    # Choose a crossover point
    i = random.randint(1, len(parent1.encoding))
    offspring1 = Strategy(parent1.encoding[:i] + parent2.encoding[i:])
    offspring2 = Strategy(parent2.encoding[:i] + parent1.encoding[i:])
    return offspring1, offspring2

def mutate(offspring, pm):
    """Mutate the offspring with mutation probability pm at each locus"""
    offspring.encoding = [1 ^ bit if random.random() <= pm else bit for bit in offspring.encoding]
    

class Population:
    """A population represents 20 strategies that evolve together over generations"""

    pc, pm = 0.7, 0.001
    
    def __init__(self):
        self.strategies = [Strategy([random.randint(0,1) for _ in range(70)]) for _ in range(20)]
        self.fitness = [0] * 20

    def evolve(self):
        """Evolves a population by calculating fitness and applying GA operators"""
        for i in range(0, 20):
            for j in range(i, 20):
                x, y = play_iterated_game(self.strategies[i], self.strategies[j])
                if i >= 20: print(i)
                self.fitness[i] += x
                self.fitness[j] += y
        self.fitness = [f/20 for f in self.fitness]

        # Fitness proportionate selection
        parents = random.choices(self.strategies, self.fitness, k = 20)
        self.strategies.clear()
        for i in range(0, 20, 2):
            if random.random() <= self.pc:
                self.strategies += crossover(parents[i], parents[i+1])
            else:
                self.strategies += parents[i:i+2]
            mutate(self.strategies[-2], self.pm)
            mutate(self.strategies[-1], self.pm)

