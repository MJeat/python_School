class Student:
    def __init__(self, name, age, id, year_of_birth):
        self.name = name
        self.age = age
        self.id = id
        self.year_of_birth = year_of_birth

    def display_info(self):
        print(f"Student: {self.name}, \nID: {self.id}, \nAge: {self.calculate_age()}\n")

    def calculate_age(self):
        self.year_of_birth = 2025 - self.age
        return self.age   


# Creating the objects
student1 = Student("Bob", 24, "ID123", 2005)
student1.display_info()
#student1.calculate_age()


