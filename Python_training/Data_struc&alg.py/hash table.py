# Hash table is a collection of pair key values.
# Hash table is a data structure that stores key-value pairs and allows for fast retrieval of values based on their associated keys.

# Yes, that's a good analogy! Just like linked lists are often used to implement arrays or lists in programming, hash tables are commonly used to implement dictionaries or associative arrays, where each element has a unique key associated with its value. 
    # Hash tables excel at providing fast access to values based on keys, making them ideal for storing and retrieving key-value pairs efficiently.



# Hash table can do insert/Delete/Search. Best is to search cuz runtime complexity is average: O(1), worst: O(n)

#A hash table (or dictionary in Python) is like a more efficient and organized version of a list of dictionaries when you need to quickly find items by their keys.
# first is the key and second is the value
#-------------------------------------------------------------------------------------


class StudentRecord:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"StudentRecord(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade})"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key already exists
                return
        self.table[index].append([key, value])  # Append new key-value pair

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return value if key is found
        raise KeyError(f"Key '{key}' not found")


# Example usage
hash_table = HashTable(10)  # Create a hash table with size 10

# Insert student records
hash_table.insert(101, StudentRecord(101, "John Doe", "A"))
hash_table.insert(102, StudentRecord(102, "Jane Smith", "B"))
hash_table.insert(103, StudentRecord(103, "Alice Johnson", "C"))
hash_table.insert(104, StudentRecord(104, "Bob Brown", "A"))
hash_table.insert(105, StudentRecord(105, "Emma Davis", "B"))

# Retrieve student records
print(hash_table.get(101))  # Output: StudentRecord(ID: 101, Name: John Doe, Grade: A)
print(hash_table.get(104))  # Output: StudentRecord(ID: 104, Name: Bob Brown, Grade: A)

# Update student record
hash_table.insert(101, StudentRecord(101, "John Smith", "A-"))
print(hash_table.get(101))  # Output: StudentRecord(ID: 101, Name: John Smith, Grade: A-)

# Try to retrieve a non-existing student record
# print(hash_table.get(106))  # This would raise a KeyError
