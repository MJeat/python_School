# Depth first search: a search algorithm for traversing a tree or graph data structure

# first, When navigating a route, we pick a route
# keep going till u reach dead end or previously visited node
# If we do, we backtrack to the last node that has unvisited adjacent neighbors

# DFS is useful for tasks that involve visiting all nodes of a graph, such as finding connected components, topological sorting, or solving puzzles like mazes
# DFS can be implemented using both recursive and iterative approaches. Here's how you can do it.

# Easiest way:
# Recursive: using call stack

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_recursive(node):
    if node:
        print(node.value, end=' ')  # Visit the current node
        dfs_recursive(node.left)    # Recursively visit left subtree
        dfs_recursive(node.right)   # Recursively visit right subtree

# Example binary tree
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.left.right = TreeNode(4), TreeNode(5)
root.right.left, root.right.right = TreeNode(6), TreeNode(7)

print("Recursive DFS:",  end=" ")
dfs_recursive(root)





#--------------------------------------------------------------------
# Iterative: harder, but faster 


def dfs_iterative(root):
    if root is None:
        return
    
    stack = [root]  # Initialize stack with the root node
    
    while stack:
        node = stack.pop()  # Pop the top node from the stack
        print(node.value, end=' ')  # Visit the current node
        
        # Push right child to stack first so that it's visited after the left child
        if node.right:
            stack.append(node.right)
        
        # Push left child to stack
        if node.left:
            stack.append(node.left)

# Example binary tree
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Iterative DFS:", end=" ")
dfs_iterative(root)




# so using depth first search is to merely return all the values within the tree with a lot of branches or children
# This method ensures that you visit every part of the tree and find all the values it contains. It's a handy way to thoroughly search through a complex structure and make sure you don't miss anything..