class SchoolMember:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

class Teacher(SchoolMember):
    def __init__(self, name, age, address, subjectSpecialization):
        super().__init__(name, age, address)
        self.subjectSpecialization = subjectSpecialization
    def teach(self):
        print("Teach:", self.subjectSpecialization)


# TODO: Implement Student and Staff
# Creating the objects
teacher1 = Teacher("Anna", 32, "Phnom Penh", "Software Engineering")
teacher1.showDetails()
teacher1.teach()
