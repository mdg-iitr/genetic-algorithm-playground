import random
import sys

def assign_score(bit_a, bit_b):
    """assign score corresponding to the set of moves
       chosen by the two players.
       bit value of 1 --> cooperation
       bit value of 2 --> defection"""

    if (bit_a,bit_b)==('1','1'):
        return (3,3)
    elif (bit_a,bit_b)==('1','0'):
        return (0,5)
    elif (bit_a,bit_b)==('0','1'):
        return (5,0)
    else:
        return (1,1)  

def get_strategy(encoding):
    """return the index in the strategy 
       corresponding to the initial memory of the
       3 games"""

    return int(encoding, 2)

def play_game(strategy_a, strategy_b):
    """we have a total of 100 games between two strategies"""
    
    score_a = score_b = 0
    encoding_a = strategy_a[64:70]
    encoding_b = strategy_b[64:70]
    for _ in range (0, 100):
        move_a = strategy_a[get_strategy(encoding_a)]
        move_b = strategy_b[get_strategy(encoding_b)]
        a, b = assign_score(move_a, move_b)
        score_a += a
        score_b += b
        encoding_a = encoding_a[2:]+ move_a + move_b
        encoding_b = encoding_b[2:]+ move_b + move_a
    #averaging the scores over 100 games        
    score_a/=100
    score_b/=100        
    return (score_a, score_b)    
                

def fitness_calculation(strategies, fitness, num_organisms):
    """each strategy plays with all other (num_organisms-1) strategies 
       and with itself i.e. a total of num_organisms games"""

    for i in range(0, num_organisms):
        for j in range(i, num_organisms):
            x, y = play_game(strategies[i], strategies[j])
            fitness[i]+=x
            fitness[j]+=y
    #averaging the fitness values over num_organisms strategies            
    fitness = [f/num_organisms for f in fitness]
    return fitness

def fitness_proportionate_selection(strategies, fitness, num_organisms):
    """choosing parent strategies on the basis of roulette 
       wheel selection, and we perform this process for 'n'
       number of times, where 
       n --> number of strategies, here num_organisms."""

    max_val = sum(fitness)
    parents = []
    for _ in range(num_organisms):
        temp_sum = 0
        rand_val = random.uniform(0, max_val)
        for j in range(num_organisms):
            temp_sum += fitness[j]
            if temp_sum>=rand_val:
                parents+=[strategies[j]]
                break
    return parents

def mutate(offspring_1, pm):
    """simple mutation of the bits of the offspring
       with repsective probability"""

    for i in range(len(offspring_1)):
        if random.random()<=pm:
            offspring_1 = offspring_1[:i]+str(1^int(offspring_1[i]))+offspring_1[i+1:]
    return offspring_1           

def crossover(parent_1, parent_2):
    """a simple crossover between the two parents
       by choosing a random crossover point."""

    size = len(parent_1)

    #choosing a crossover point
    crossover_point = random.randint(0, size)
    offspring_1 = parent_1[:crossover_point]+parent_2[crossover_point:]
    offspring_2 = parent_2[:crossover_point]+parent_1[crossover_point:]
    return [offspring_1, offspring_2]

def evolve(number_of_organisms, generations):
    """main function to facilitate all the evolution functionalities"""

    #crossover and mutation probabilities
    pc, pm = 0.7, 0.001
    strategies = [(''.join(str(random.randint(0,1)) for _ in range(70))) for _ in range(number_of_organisms)]

    #temp list to keep a track of maximum fitness as the generations proceed
    max_fitness_over_generations = []

    #running for certain number of generations
    for gen in range(generations):
        print ('running for generation ', gen)
        fitness = [0]*number_of_organisms
        fitness = fitness_calculation(strategies, fitness, number_of_organisms)
        parents = fitness_proportionate_selection(strategies, fitness, number_of_organisms)
        
        temp_max_fitness = max(fitness)
        max_fitness_over_generations += [temp_max_fitness]
        #displaying results
        print ('Listing the strategies followed by the population for generation number ', gen)
        for i in range(number_of_organisms):
            print ('Stategy followed by organism number %d is %s'%(i, strategies[i]))
        
        strategies.clear()
        for j in range(0, number_of_organisms, 2):
            #crossover between parents
            if random.random()<=pc:
                strategies+=crossover(parents[j], parents[j+1])
            else:
                strategies+=[parents[j], parents[j+1]]
            
            #mutation in the generated offsprings.
            strategies[-2] = mutate(strategies[-2], pm)
            strategies[-1] = mutate(strategies[-1], pm)
    return max_fitness_over_generations            


if len(sys.argv)<3:
    print ('Usage: python3 evolution.py <number_of_organisms> <number_of_generations>')
    sys.exit()
num_organisms = int(sys.argv[1])
num_generations = int(sys.argv[2])
fitness_over_generations = evolve(num_organisms, num_generations)
print ('\n The fitnesses over generations are as follows')
print (fitness_over_generations)