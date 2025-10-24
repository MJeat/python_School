class Student:
    def __init__(self, name, id, birthdate):
        self.name = name
        self.id = id
        self.birthdate= birthdate
    def display(self):
        print(f"The student name:\n{self.name}\nID: {self.id}\nBirthdate: {self.birthdate}")

student1 = Student("Bob", 12, 2005)
student1.display()