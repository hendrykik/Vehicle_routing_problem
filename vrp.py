import random
import math

class VRP_GA:
    def __init__(self, customers, depot, vehicle_count, pop_size=100, generations=500,
                 crossover_rate=0.8, mutation_rate=0.02):
        self.customers = customers  # list of (x, y, demand)
        self.depot = depot          # (x, y)
        self.vehicle_count = vehicle_count
        self.pop_size = pop_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = []

    def distance(self, a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    def total_distance(self, route):
        dist = 0
        prev = self.depot
        for cust in route:
            dist += self.distance(prev, self.customers[cust][:2])
            prev = self.customers[cust][:2]
        dist += self.distance(prev, self.depot)
        return dist

    def decode(self, chromosome):
        # split chromosome into vehicle_count routes
        avg = len(chromosome) // self.vehicle_count
        routes = []
        for i in range(self.vehicle_count):
            start = i*avg
            end = (i+1)*avg if i < self.vehicle_count-1 else len(chromosome)
            routes.append(chromosome[start:end])
        return routes

    def fitness(self, chromosome):
        routes = self.decode(chromosome)
        total = sum(self.total_distance(route) for route in routes)
        return 1.0 / (total + 1e-6)

    def initial_population(self):
        base = list(range(len(self.customers)))
        for _ in range(self.pop_size):
            chromo = base[:]
            random.shuffle(chromo)
            self.population.append(chromo)

    def select(self):
        weights = [self.fitness(chromo) for chromo in self.population]
        return random.choices(self.population, weights=weights, k=2)

    def crossover(self, p1, p2):
        if random.random() > self.crossover_rate:
            return p1[:], p2[:]
        a, b = sorted(random.sample(range(len(p1)), 2))
        child1 = [-1]*len(p1)
        child2 = [-1]*len(p2)
        # ordered crossover
        child1[a:b] = p1[a:b]
        child2[a:b] = p2[a:b]
        fill1 = [c for c in p2 if c not in child1]
        fill2 = [c for c in p1 if c not in child2]
        for i in range(len(p1)):
            if child1[i] == -1:
                child1[i] = fill1.pop(0)
            if child2[i] == -1:
                child2[i] = fill2.pop(0)
        return child1, child2

    def mutate(self, chromosome):
        for i in range(len(chromosome)):
            if random.random() < self.mutation_rate:
                j = random.randint(0, len(chromosome)-1)
                chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

    def evolve(self):
        self.initial_population()
        best, best_fit = None, 0
        for gen in range(self.generations):
            new_pop = []
            for _ in range(self.pop_size//2):
                p1, p2 = self.select()
                c1, c2 = self.crossover(p1, p2)
                self.mutate(c1)
                self.mutate(c2)
                new_pop.extend([c1, c2])
            self.population = new_pop
            gen_best = max(self.population, key=self.fitness)
            gen_fit = self.fitness(gen_best)
            if gen_fit > best_fit:
                best, best_fit = gen_best, gen_fit
        return best, 1.0/best_fit

if __name__ == '__main__':
    # Example usage:
    depot = (50, 50)
    customers = [(random.randint(0,100), random.randint(0,100), 1) for _ in range(30)]
    ga = VRP_GA(customers, depot, vehicle_count=5)
    solution, dist = ga.evolve()
    routes = ga.decode(solution)
    print('Routes:', routes)
    print('Total distance:', dist)  
