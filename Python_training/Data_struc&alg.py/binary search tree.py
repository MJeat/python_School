# Binary search tree: a tree that it has no more than 2 children nodes.
# left and right child

# The root node should be greater than the left child and lesser than the right child.
# The left most child is the smallest value, whereas the right most child is the largest value.
# The very left and very right child.

# time complexity: O(logn)
# space complexity: O(n)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
        # Ignore duplicate values

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node is not None
        elif value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    def in_order_traversal(self):
        traversal_result = []
        self._in_order_traversal_recursively(self.root, traversal_result)
        return traversal_result

    def _in_order_traversal_recursively(self, node, result):
        if node:
            self._in_order_traversal_recursively(node.left, result)
            result.append(node.value)
            self._in_order_traversal_recursively(node.right, result)


# Example usage
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("In-order traversal:", bst.in_order_traversal())
print("Is 4 in the tree?", bst.search(4))
print("Is 9 in the tree?", bst.search(9))
