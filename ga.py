import random

class Problem_Genetic(object):
    def __init__(self, genes, individuals_length, decode, fitness):
        self.genes = genes
        self.individuals_length = individuals_length
        self.decode = decode
        self.fitness = fitness

    def mutation(self, c, prob):
        cm = list(c)
        for i in range(len(cm)):
            if random.random() < prob:
                j = random.randint(0, len(cm)-1)
                cm[i], cm[j] = cm[j], cm[i]
        return cm

    def crossover(self, c1, c2):
        if self.individuals_length <= 2:
            return [c1, c2]
        pos = random.randint(1, self.individuals_length - 2)
        cr1 = c1[:pos] + [x for x in c2 if x not in c1[:pos]]
        cr2 = c2[:pos] + [x for x in c1 if x not in c2[:pos]]
        return [cr1, cr2]

def genetic_algorithm(problem, pop_size, generations, crossover_prob, mutation_prob, tournament_size):
    population = []
    for _ in range(pop_size):
        ind = random.sample(problem.genes, problem.individuals_length)
        population.append(ind)

    for g in range(generations):
        new_population = []

        while len(new_population) < pop_size:
            t1 = random.sample(population, tournament_size)
            p1 = min(t1, key=problem.fitness)

            t2 = random.sample(population, tournament_size)
            p2 = min(t2, key=problem.fitness)

            if random.random() < crossover_prob:
                children = problem.crossover(p1, p2)
            else:
                children = [p1[:], p2[:]]

            c1 = problem.mutation(children[0], mutation_prob)
            new_population.append(c1)

            if len(new_population) < pop_size:
                c2 = problem.mutation(children[1], mutation_prob)
                new_population.append(c2)

        population = new_population

    best = population[0]
    best_fitness = problem.fitness(best)
    for ind in population:
        f = problem.fitness(ind)
        if f < best_fitness:
            best = ind
            best_fitness = f

    return best, best_fitness

