import random
from vga_ga.ga import VRP_GA
from vga_ga.config import VEHICLE_COUNT, POP_SIZE, GENERATIONS, CROSSOVER_RATE, MUTATION_RATE

def generate_customers(n):
    return [(random.randint(0, 100), random.randint(0, 100), 1) for _ in range(n)]

if __name__ == '__main__':
    depot = (50, 50)
    customers = generate_customers(30)

    ga = VRP_GA(
        customers,
        depot,
        vehicle_count=VEHICLE_COUNT,
        pop_size=POP_SIZE,
        generations=GENERATIONS,
        crossover_rate=CROSSOVER_RATE,
        mutation_rate=MUTATION_RATE
    )

    solution, dist = ga.evolve()
    routes = ga.decode(solution)

    print("Routes:", routes)
    print("Total distance:", dist)
