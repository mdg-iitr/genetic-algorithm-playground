from Population import Population

target = 'one for all, all for one'
pop_max = 1000
mut_rate = 0.001
all_phrases = ""


if __name__ == "__main__":
    pop = Population(target, mut_rate, pop_max)

    while not pop.get_best().__eq__(target):
        if pop.is_finished():
            break
        pop.natural_selection()
        pop.generate()
        pop.calc_fitness()
        print(pop.get_average_fitness())
        print(pop.get_best())

    print(pop.get_num_of_generations())
