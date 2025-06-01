import math

def euclidean_distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def split_routes(chromosome, vehicle_count):
    avg = len(chromosome) // vehicle_count
    routes = []
    for i in range(vehicle_count):
        start = i * avg
        end = (i + 1) * avg if i < vehicle_count - 1 else len(chromosome)
        routes.append(chromosome[start:end])
    return routes
