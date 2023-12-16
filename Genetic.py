import numpy as np


######- Initial Phase -######
def init_pop(pop_size):
    return np.random.randint(8, size=(pop_size, 8))
    # random numbers in range.


######- Fitness Phase -######
def calc_fitness(population):
    fitness_vals = []
    for x in population:
        penalty = 0
        for i in range(8):
            r = x[i]
            for j in range(8):
                if i == j:
                    continue
                d = abs(i - j)
                if x[j] in [r, r - d, r + d]:
                    penalty += 1
        fitness_vals.append(penalty)
    return -1 * np.array(fitness_vals)


######- Selection Phase -######
def selection(population, fitness_vals):
    probs = fitness_vals.copy()
    probs += abs(probs.min()) + 1
    probs = probs / probs.sum()
    n = len(population)
    indices = np.arange(n)
    selected_indices = np.random.choice(indices, size=n, p=probs)
    selected_population = population[selected_indices]
    return selected_population


######- Crossover Phase -######
def Crossover(Parent1, Parent2, pc):
    r = np.random.random()  # {from 0 to 1, exclusive}
    if r < pc:
        m = np.random.randint(1, 8)
        child1 = np.concatenate([Parent1[:m], Parent2[m:]])
        child2 = np.concatenate([Parent2[:m], Parent1[m:]])
    else:
        child1 = Parent1.copy()
        child2 = Parent2.copy()
    return child1, child2


######- Mutation -######
def Mutation(individual, pm):
    r = np.random.random()
    if r < pm:
        m = np.random.randint(8)
        individual[m] = np.random.randint(8)
    return individual


######- crossover_mutation -######
def crossover_mutation(selected_pop, pc, pm):
    n = len(selected_pop)
    new_pop = n.empty((n, 8), dtype=int)
    for i in range(0, n, 2):
        parent1 = selected_pop[i]
        parent2 = selected_pop[i + 1]
        child1, child2 = Crossover(parent1, parent2, pc)
        new_pop[i] = child1
        new_pop[i + 1] = child2
    for i in range(n):
        Mutation(new_pop[i], pm)
    return new_pop


######- Testing part -######
initial_population = init_pop(4)
print(initial_population)

fitnees_vals = calc_fitness(initial_population)
print(fitnees_vals)

selected_population = selection(initial_population, fitnees_vals)
print(selected_population)

Parent1 = selected_population[0]
Parent2 = selected_population[1]
child1, child2 = Crossover(Parent1, Parent2, pc=0.70)
print(Parent1, ": ", child1)
print(Parent2, ": ", child2)
