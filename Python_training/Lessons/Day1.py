#Day 1 of Python
#Using ''#'' called comment to note in python only.
#this is variables. Anything within " " are called values. variable stores value.
First_Name = "Bro "
Second_name = "Code"
#you can combine variables like shown below.
Full_name = First_Name + Second_name
print(Full_name)
Age = "21"
age = 21
#or. a shortcut. Can only for int ( interger ) not str ( string ).
#Basically, a string cant use with interger ( int )
age +=1
print(age)

print(type(Age))

print(type(age))

print("your age is: "+ str(age))
#age is interger or int so when putting in print, it wont work cuz of different data type ( above is a string + int which doesnt work).
#To convert int into string just put:     str(...)
#Age is string or str so when putting in print, it works cuz the same data type ( string + string ) Age = "21" called string value


#float data type for decimal numbers, whereas int for a whole number only
height = 20.2
print(type(height))
