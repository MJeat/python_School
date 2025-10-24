# Linked list is like a train that has carts. Each cart is call 'Node' where it carries data. 

# Linked list does carry data the same way as stack and queue, but with linked list, you can add or remove any data from any location or rank.
# unlike stack, where you can only add new data at the top, and queue where you pop data from the head.


# 
#Yes, that's correct! The data within a linked list can be in any order. Unlike an array (or ArrayList in some languages),
# where elements are stored in contiguous memory locations and the order is defined by their position in that contiguous block, a linked list's elements (nodes) are not necessarily stored next to each other in memory.

# When we reach the tail of linked list, it will output: null


# Con: It takes longer to find the data cuz it has no inde, unlike array. Linked list will search randomly until it gets what you want.


#-------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Store the reference to the next node. Reference is referring to a pointer or an address


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def insert_at_beginning(self, data): #When the function (def) is within the class, we need to use self within the function. 
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the old head
        self.head = new_node  # Update the head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node # If the list is empty, sets the new node as the head.
            return
        last = self.head
        while last.next:  # Traverse (travdl across) to the end of the list
            last = last.next
        last.next = new_node  # Link the last node to the new node

    def delete_node(self, key):  # Key here is the same as value that you input in the printing area.
        temp = self.head  # You need to put self.head in order for the system to not get lost while finding ur input key or value

        # If the head node itself holds the key to be deleted. This code below checks whether the head node (which is the first node in the list) contains the key that we're trying to delete. 
        #This is important because it's the first place we should look.
        if temp and temp.data == key:
            self.head = temp.next  # Change head
            temp = None  # Free old head
            return

        # Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If the key was not present in the linked list
        if temp is None:
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None   # After unlinking the node from the list, we no longer need it. 
                      #So, we free up the memory occupied by the node by setting temp to None.

    def search(self, key): 
        current = self.head  # You need to put self.head in order for the system to not get lost while finding ur input key or value
        while current:
            if current.data == key:  # Node found
                return True
            current = current.next
        return False  # Node not found

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


# Calling the functions:

# Create a new LinkedList
llist = LinkedList()

# Insert elements
llist.insert_at_beginning(10)
llist.insert_at_beginning(20)
llist.insert_at_end(30)

# Print the linked list
llist.print_list()  # Output: 20 -> 10 -> 30 -> None

# Search for an element
print(llist.search(10))  # Output: True
print(llist.search(40))  # Output: False

# Delete an element
llist.delete_node(10)
llist.delete_node(320) # This is not in the list that given by us, so it does not display anything cuz we use return after "if temp is None:"

llist.print_list()  # Output: 20 -> 30 -> None

#-----------------------------------------------------------------------------------------------------------------
print('-------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------
#Exercise:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist():
    def __init__(self):
        self.head = None


    def beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node


    def ending(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next 
        last.next = new_node


    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next


        if temp is None:
            return
        
        prev.next = temp.next
        temp = None

    def search_key(self,key):
        current=self.head
        while current:
            if current.data == key:
                return True
            current = current.next
            return False
        

    def print(self):
        current= self.head
        while current:
            print(current.data, end='->')

            current = current.next

        print("None")

    def get_length(self):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next
        return length
    

llist = Linkedlist()
llist.beginning(3)
llist.beginning(2)
llist.beginning(1)
llist.ending(4)



llist.print()
print('Length of linkedlist is: ',
      llist.get_length())




