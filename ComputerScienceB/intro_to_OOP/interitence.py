class SchoolMember:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

# Child classes
class Teacher(SchoolMember):
    def __init__(self, name, age, address, subjectSpecialization):
        super().__init__(name, age, address) # Inheritance here
        self.subjectSpecialization = subjectSpecialization
    def teach(self):
        print("Teach:", self.subjectSpecialization)

class Student(SchoolMember):
    def __init__(self, name, age, address, mainMajor):
        super().__init__(name, age, address) # Inheritance here
        self.mainMajor= mainMajor
    def major(self):
        print(f"Major: {self.mainMajor}")

# TODO: Implement Student and Staff
# Creating the objects
print("===Teacher Details===")
teacher = Teacher("Anna", 32, "Phnom Penh", "Software Engineering\n")
teacher.showDetails()
teacher.teach()

print("===Student Details===")
student= Student("bob", 22, "Australia", "Cybersecurity")
student.showDetails()
student.major() 
