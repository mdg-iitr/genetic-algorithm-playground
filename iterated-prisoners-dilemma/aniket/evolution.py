import random

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
    for i in range (0, 100):
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
                

def fitness_calculation(strategies, fitness):
    """each strategy plays with all other 19 strategies 
       and with itself i.e. a total of 20 games"""

    for i in range(0, 20):
        for j in range(i, 20):
            x, y = play_game(strategies[i], strategies[j])
            fitness[i]+=x
            fitness[j]+=y
    #averaging the fitness values over 20 strategies            
    fitness = [f/20 for f in fitness]
    return fitness

def fitness_proportionate_selection(strategies, fitness):
    """choosing parent strategies on the basis of roulette 
       wheel selection, and we perform this process for 'n'
       number of times, where 
       n --> number of strategies, here 20."""

    max_val = sum(fitness)
    parents = []
    size = len(fitness)
    for i in range(size):
        temp_sum = 0
        rand_val = random.uniform(0, max_val)
        for j in range(size):
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
    crossover_point = random.randint(0, size-1)
    if crossover_point==0:
        return [parent_2, parent_1]
    elif crossover_point==size-1:
        return [parent_1, parent_2]
    else:    
        offspring_1 = parent_1[:crossover_point]+parent_2[crossover_point:]
        offspring_2 = parent_2[:crossover_point]+parent_1[crossover_point:]
    return [offspring_1, offspring_2]   

def evolve():
    """main function to facilitate all the evolution functionalities"""

    #crossover and mutation probabilities
    pc, pm = 0.7, 0.001
    strategies = [(''.join(str(random.randint(0,1)) for _ in range(70))) for _ in range(20)]
    generations = 10

    #running for certain number of generations
    for _ in range(generations):
        fitness = [0]*20
        fitness = fitness_calculation(strategies, fitness)
        parents = fitness_proportionate_selection(strategies, fitness)

        strategies.clear()
        for j in range(0, 20, 2):
            #crossover between parents
            if random.random()<=pc:
                strategies+=crossover(parents[j], parents[j+1])
            else:
                strategies+=[parents[j], parents[j+1]]
            
            #mutation in the generated offsprings.
            strategies[-2] = mutate(strategies[-2], pm)
            strategies[-1] = mutate(strategies[-1], pm)    

evolve()