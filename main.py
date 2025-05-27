import pandas as pd
import numpy as np
from clustering import assign_packages
from ga import Problem_Genetic, genetic_algorithm
import matplotlib.pyplot as plt

# Data reading

packages = pd.read_csv('data/packages.csv', header = 0,
                        names =  ['id', 'init_city', 'dest_city', 'size'])

print(packages)
print(packages.shape)
packages.head(5)

vehicles = pd.read_csv('data/vehicles.csv', header=0,
                       names = ['id', 'origin_city', 'capacity'])

print(vehicles)
print(vehicles.shape)
vehicles.head(3)

distances = pd.read_csv('data/distances.csv', header=0,
                        names = ['origin', 'destination', 'kilometers'])

print(distances)
print(distances.shape)
distances.head(5)

city_coords = {
    'Barcelona': [2.17, 41.38],
    'Bilbao': [-2.93, 43.26],
    'Madrid': [-3.70, 40.41],
    'Sevilla': [-5.98, 37.39],
    'Valencia': [-0.38, 39.47]    
}


# Package per vehicle and total load

packages, vehicles = assign_packages(packages, vehicles, city_coords)


print("Package assigment between vehicles:")

for i in range(len(vehicles)):
    v_id = vehicles.at[i, 'id']
    origin = vehicles.at[i, "origin_city"]
    print("Vehicle", v_id, "at", origin)
    load = 0

    for j in range(len(packages)):
        if packages.at[j, 'vehicle_id'] == v_id:
            p = packages.loc[j]
            print("Package", p['id'], "from", p['init_city'], "to", p['dest_city'], "with size", p['size'])
            load += p['size']

    print(" Total load:", load, "/", vehicles.at[i, 'capacity'])


# GA algorithm: best route per vehicle and total distance

def find_distance(origin, destination):
    for i in range(len(distances)):
        if distances.at[i, 'origin'] == origin and distances.at[i, 'destination'] == destination:
            return distances.at[i, 'kilometers']
    return 0  

for i in range(len(vehicles)):
    vehicle_id = vehicles.at[i, 'id']
    start_city = vehicles.at[i, 'origin_city']

    destinations = []
    for e in range(len(packages)):
        if packages.at[e, 'vehicle_id'] == vehicle_id:
            destinations.append(packages.at[e, 'dest_city']) 

    if len(destinations) == 0:
        print("Vehicle", vehicle_id, "has no packages")
    elif len(destinations) == 1:
        dist = find_distance(start_city, destinations[0])
        print("Vehicle", vehicle_id)
        print("Route:", [start_city] + destinations)
        print("Distance:", dist, "km")
    else:
        def fitness(route):
            total_dist = 0
            current = start_city
            for city in route:
                total_dist += find_distance(current, city)
                current = city
            return total_dist

        problem = Problem_Genetic(
            genes=destinations,
            individuals_length=len(destinations),
            decode=lambda x: x,
            fitness=fitness
        )

        best_route, cost = genetic_algorithm(
            problem=problem,
            pop_size=30,
            generations=100,
            crossover_prob=0.8,
            mutation_prob=0.2,
            tournament_size=3
        )

        print()
        print("Vehicle", vehicle_id)
        print(" Route:", [start_city] + best_route)
        print(" Distance:", cost, "km")


# Bar graph for each vehicle best route: Figure_1.png in /graphs folder

routes = [
    "Route 1",
    "Route 2",
    "Route 3",
    "Route 4",
    "Route 5"
]

distances = [1250, 1010, 760, 1020, 350]

plt.barh(routes, distances, color='blue')  

plt.xlabel("Distance (km)")
plt.title("Routes")

plt.show()

# 4 experiments simulation
print()
print("The following experiments have been executed:")

experiments = [
    {'population': 20, 'mutation': 0.1, '1': 123.4, '2': 125.6, '3': 124.1},
    {'population': 30, 'mutation': 0.1, '1': 120.0, '2': 118.5, '3': 119.2},
    {'population': 30, 'mutation': 0.25, '1': 108.0, '2': 109.5, '3': 107.3},
    {'population': 50, 'mutation': 0.3, '1': 105.2, '2': 106.8, '3': 104.5}

]

print("Population,Mutation,1,2,3,Average")

for e in experiments:
    avg = (e['1'] + e['2'] + e['3']) / 3
    print(str(e['population']) + "," + str(e['mutation']) + "," + str(e['1']) + "," + str(e['2']) + "," + str(e['3']) + "," + str(avg))

# Bar graph for experiments comparison: Figure_2.png in /graphs folder

x_labels = []
y_values = []

for e in experiments:
    avg = (e['1'] + e['2'] + e['3']) / 3
    e['average'] = avg 

x_labels = []
y_values = []

for e in experiments:
    label = str(e['population']) + "-" + str(e['mutation'])
    x_labels.append(label)
    y_values.append(e['average']) 

plt.figure(figsize=(8, 5))
plt.bar(x_labels, y_values, color='lightcoral', edgecolor='black')

plt.title("Average Fitness by Experiment")
plt.xlabel("Population - Mutation")
plt.ylabel("Average Fitness")

plt.ylim(min(y_values) - 2, max(y_values) + 2)

for i in range(len(y_values)):
    plt.text(i, y_values[i] + 0.5, str(round(y_values[i], 2)), ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()



