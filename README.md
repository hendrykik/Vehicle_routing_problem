Vehicle Routing Problem

The objective of the project is to implement genetic algoritm that solve vehicle routing problem.

"""
Explanation:

1. **Representation**: We encode a solution (chromosome) as a permutation of customer indices.  
2. **Decoding**: We split this permutation into `vehicle_count` contiguous segments, each representing one vehicle's route.  
3. **Fitness**: The fitness is inverse of total traveled distance (sum of distances from depot->customers->depot).  
4. **Initial Population**: Random shuffles of the full customer list.  
5. **Selection**: Roulette-wheel (fitness-proportional) selection picking two parents.  
6. **Crossover**: Ordered crossover (OX) exchanges sub-sequences while preserving relative order.  
7. **Mutation**: Swap mutation randomly swaps two customer indices at a low probability.  
8. **Evolution Loop**: Generate new population by selecting, crossing, mutating. Track best solution across generations.  
9. **Result**: Returns the best permutation and its total distance.  

Adjust parameters (population size, generations, rates) based on problem size and computational budget.  
"""