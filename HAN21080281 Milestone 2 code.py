from itertools import permutations
def route_calculator (world_map, city_names, start):
    all_cities = len(world_map)
    optimal_route = []
    destinations = []
    for city in range(all_cities):
        if city != start:
            destinations.append(city)

    shortest_path = 999999999
    next_permutation = permutations(destinations)
    for possible_route in next_permutation:
        current_route = [city_names[start]]
        current_distance = 0
        index = start
        
        for sub_index in possible_route:
            current_distance += world_map[index][sub_index]
            current_route.append(city_names[sub_index])
            index = sub_index
        current_distance += world_map[index][start]
        
        if current_distance < shortest_path:
            optimal_route = current_route
            shortest_path = current_distance
    optimal_route.append (city_names[start])
    
    return optimal_route

start = 0
city_names = []
world_map = []
number_of_cities = int(input("Please enter total number of cities: "))

for times in range (number_of_cities):
    city = input("Please enter your city name in alphabetical order: ")
    city_names.append(city)
    
for times in range (number_of_cities):
    one_city_distances = []
    for sub_times in range (number_of_cities):
        distance = int(input("Please enter distance from {} to {}: ".format(city_names[times], city_names[sub_times])))
        one_city_distances.append(distance)
    world_map.append(one_city_distances)

print("Your optimal route is:", route_calculator (world_map, city_names, start))
