from Population import Population

crossover_rate = 0.7
mut_rate = 0.001
max_strategies = 20
num_gen = 5

if __name__ == "__main__":
    pop = Population(crossover_rate, mut_rate, max_strategies)

    for i in range(0, num_gen):
        pop.natural_selection()
        pop.generate()
        pop.calc_fitness()
        print(pop.get_best_strategy())
        print(pop.get_average_fitness())
