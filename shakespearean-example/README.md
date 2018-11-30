# Genetic-Algorithm

## 1. Shakespearean Monkey Example
A monkey is typing on a keyboard randomly, What is the probability that he will be able to type the all the works of Shakespeare?? Probably 0. But what if he is typing for an infinite time.

### Implementation
In our implementation a target phrase(eg. One for all, All for one) is generated from random characters on the keyboard using genetic algorithm. 
 1. Population consists of a particular number of DNA which evolve according to the algorithm. (We have taken a population of 1000 DNA)
 2. A DNA is a string of randomly generated characters whose length is equal to the length of target string.
 3. Fitness is the no. of alphabets which are same in both target and dna.
 4. Mutation Rate (p<sub>m</sub>) is taken 0.001
 5. Roulette Wheel is Used for Natural Selection.
