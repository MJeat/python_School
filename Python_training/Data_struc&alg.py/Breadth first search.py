# Breadth first search: a search algorithm for traversing a tree or graph data structure
# Breadth = broad/wide
# This is done one "Level" at a time, rather than one "branch" at a time 


# time complexity: O(V+E)
# This method is used with queue, whereas depth first search uses stack

# BFS explores level by level: It looks at all the nearby spots before moving further away.
# it's like playing hide and seek. You look at the closet spot first before running to further spot.




def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)    # These 2 as the first letter or node to be visited and put in the queue
    queue.append(node)

    while queue:  # This starts a loop that continues as long as there are nodes in the queue to be processed.
        m = queue.pop(0)    # This removes the first element from the queue (FIFO order) and assigns it to the variable m. 
                                #This is the current node being processed.
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

bfs(graph, "A")
#------------------------------------------------------
print("------------------------------------------------------")
# Exercise 1: 

def bfs1(graph, node):

    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue: 
        s = queue.pop(0)
        print(s,end=" ")


        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)



graph1 = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2'],
    '5': ['2'],
    '6': ['3'],
    '7': ['3']
}

bfs(graph1, "1")