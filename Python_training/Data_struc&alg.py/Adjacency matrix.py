# Adjancency matrix: a 2D array to store True or False (1/0) to represent edges
    # number of rows = the number of unique nodes
    # number of colomns = the number of unique nodes

# Adjacency matrix: very quick to use when having a lot of edges, but slow cuz space
# Runtime complexity to check edges: O(1)
# space complexity: O(v^2), v or n: number of verticels (nodes)
                # or O(n^2)


# Define the nodes
nodes = ['A', 'B', 'C', 'D', 'E']

# Define the connections
connections = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

# Initialize the adjacency matrix with zeros
adj_matrix = [[0] * len(nodes) for i in range(len(nodes))]

# Fill the adjacency matrix
for i, node in enumerate(nodes):
    for neighbor in connections[node]:
        j = nodes.index(neighbor)
        adj_matrix[i][j] = 1

# Print the adjacency matrix
for row in adj_matrix:
    print(row)




