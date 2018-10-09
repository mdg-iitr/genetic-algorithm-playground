Implement a GA to search for strategies to play the **Iterated Prisoner's Dilemma**, in which the fitness
of a strategy is its average score in playin 100 games with itself and with every other member of the
population. Each strategy remembers the three previous turns with a given player. Use a population of
20 strategies, fitness−proportional selection, single−point crossover with <img src="https://latex.codecogs.com/png.latex?p_c&space;=&space;0.7"/>, and mutation with <img src="https://latex.codecogs.com/png.latex?p_m&space;=&space;0.001"/>.

a. See if you can replicate Axelrod's qualitative results: do at least 10 runs of 50 generationsp
each and examine the results carefully to find out how the best−performing strategies work
and how they change from generation to generation.

b. Turn off crossover (set <img src="https://latex.codecogs.com/png.latex?p_c&space;=&space;0"/>) and see how this affects the average best fitness reached and
the average number of generations to reach the best fitness. Before doing these experiments, it
might be helpful to read Axelrod 1987.

c. Try varying the amount of memory of strategies in the population. For example, try a version
in which each strategy remembers the four previous turns with each other player. How does
this affect the GA's performance in finding high−quality strategies? (This is for the very
ambitious.)

d. See what happens when noise is added—i.e., when on each move each strategy has a small
probability (e.g., 0.05) of giving the opposite of its intended answer. What kind of strategies
evolve in this case? (This is for the even more ambitious.)
