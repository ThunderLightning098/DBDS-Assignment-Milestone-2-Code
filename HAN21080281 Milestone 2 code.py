from itertools import permutations

#Function route calculator
def route_calculator (world_map, city_names, start):

#Store optimal route and list of index
    all_cities = len(world_map)
    optimal_route = []
    destinations = []

#Store list of index
    for city in range(all_cities):
        if city != start:
            destinations.append(city)

#Store shortest path
    shortest_distance = 999999999
    
#Generate all possibilities
    next_permutation = permutations(destinations)

    for possible_route in next_permutation:
#Store starting point, current distance and current index
        current_route = [city_names[start]]
        current_distance = 0
        index = start
        
#Calculate all possible routes
        for sub_index in possible_route:    
#Calculate distance of current route
            current_distance += world_map[index][sub_index]
#Add destinations to current route
            current_route.append(city_names[sub_index])
            index = sub_index
        current_distance += world_map[index][start]
        
#If current distance is smaller than previous shortest distance,
#update current distance as shortest distance and current route as optimal route
        if current_distance < shortest_distance:
            optimal_route = current_route
            shortest_distance = current_distance
#Add starting point as finishing point since driver has to go back to original starting point
    optimal_route.append (city_names[start])

    return optimal_route
#(Singh et al, 2022)

#Store starting index, city names, all distance between cities and total number of cities
start = 0
city_names = []
world_map = []
number_of_cities = int(input("Please enter total number of cities: "))

#Store city names
for times in range (number_of_cities):
    city = input("Please enter your city name in alphabetical order: ")
    city_names.append(city)
    
#Store all distance between cities
for times in range (number_of_cities):
    one_city_distances = []
    for sub_times in range (number_of_cities):
        distance = int(input("Please enter distance from {} to {}: ".format(city_names[times], city_names[sub_times])))
        one_city_distances.append(distance)
    world_map.append(one_city_distances)

print("Your optimal route is:", route_calculator (world_map, city_names, start))

#Test data:

#Inputs:
#City names (in order): "A", "B", "C", "D"
#All distance (in order): 0, 10, 15, 20, 10, 0, 35, 25, 15, 35, 0, 30, 20, 25, 30, 0

#After entering, program inputs should look like this:
#city_names = ["A", "B", "C", "D"]
#world_map = [[0, 10, 15, 20],
#             [10, 0, 35, 25],
#             [15, 35, 0, 30],
#             [20, 25, 30, 0]]

#Outputs:
#Optimal route: ["A", "B", "D", "C", "A"]
