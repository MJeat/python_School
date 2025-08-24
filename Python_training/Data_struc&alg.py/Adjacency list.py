# Adjacency list: an array/arraylist made of linkedlist.

#               Each linkedlist as a unique node at the head
#               All adjacent neighbors to that node are added to that node's linkedlist



#Exercise: 

Connected_cities = {}


def add_road(Connected_cities, city1, city2):

    if city1 in Connected_cities:

        Connected_cities[city1].append(city2)

    else:

        Connected_cities[city1] = [city2]

    if city2 in Connected_cities:

        Connected_cities[city2].append(city1)
    else: 
        Connected_cities[city2] = [city1]
    

    
def remove_road(Connected_cities, city1, city2):

    if city1 in Connected_cities and city2 in Connected_cities[city1]:
        Connected_cities[city1].remove(city2)
    
    if city2 in Connected_cities and city1 in Connected_cities[city2]:
        Connected_cities[city2].remove(city1)

        
def display_graph(Connected_cities):
    for city in Connected_cities:
        print(f"{city}: {Connected_cities[city]}")


add_road(Connected_cities, "A","B")
add_road(Connected_cities, "C","A")
add_road(Connected_cities, "C","B")
add_road(Connected_cities, "A","D")

print("Initial Graph: ")
display_graph(Connected_cities)



add_road(Connected_cities, "A", "C")
print("Updated list: ")
display_graph(Connected_cities)


remove_road(Connected_cities, "A", "D")
print("Updated remove road list:")
display_graph(Connected_cities)

