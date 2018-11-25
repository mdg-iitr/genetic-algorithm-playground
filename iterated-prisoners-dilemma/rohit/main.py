from population import Population

if __name__ == "__main__":
    population = Population(0.7, 0.01)

    population.naturalSelection()
    population.calculateFitness()
