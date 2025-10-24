# Node class for doubly linked list
class Node:
    def __init__(self, data):
        self.data = data        # store the data
        self.next = None        # pointer to the next node
        self.prev = None        # pointer to the previous node


# Doubly Linked List implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at head
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head  # new node points to current head
        if self.head is not None:
            self.head.prev = new_node  # set prev pointer of current head
        self.head = new_node  # update head to new node

    # 2. Insert at tail
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:  # empty list
            self.head = new_node
            return
        current = self.head
        while current.next:  # go to the last node
            current = current.next
        current.next = new_node  # last node points forward to new node
        new_node.prev = current  # new node points back to last node

    # 3. Delete a specific node
    def delete(self, key):
        current = self.head
        while current:  # search for node
            if current.data == key:
                if current.prev:  # if not head
                    current.prev.next = current.next
                else:  # if it's the head
                    self.head = current.next
                if current.next:  # if not tail
                    current.next.prev = current.prev
                return  # node deleted
            current = current.next

    # 4. Traverse and display all nodes
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


# Example usage
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(5)
dll.insert_at_tail(20)
dll.insert_at_tail(25)

print("Doubly Linked List:", dll.display())

dll.delete(20)
print("After deleting 20:", dll.display())
