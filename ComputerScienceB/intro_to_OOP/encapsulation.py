
class SchoolMember:
    def __init__(self, name):
        self.name = name # public
        self._age = 18 # protected
        self.__address = "Phnom Penh" # private
    def setAge(self, age):
        self._age = age
    def setAddress(self, address):
        self.__address = address
    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Address:", self.__address)
class Teacher(SchoolMember):
    def __init__(self, name, subjectSpecialization):
        super().__init__(name)
        self.subjectSpecialization = subjectSpecialization
    def teach(self):
        print("Teach:", self.subjectSpecialization)
    
teacher1 = Teacher("Anna", "Software Engineering")
teacher1.showDetails() # will show the default age and address
print()
teacher1.setAge(40) # set age through method since it's protected
teacher1.setAddress("Siem Reap") # set address through since it's private
teacher1.showDetails()
teacher1.name = "New Name" # can directly update name attribute since it's public
print(teacher1.name)
print(teacher1._age)
# print(teacher1.__address) # uncomment this will lead to errors since address is private
