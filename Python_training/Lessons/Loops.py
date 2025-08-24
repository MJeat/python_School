s = "learn"

for i in s:
    print(i,end="")



print("")

#use for loop in a list

programming = ["java", "python","ruby"]
for j in programming:
    print(j)


#----------------------------------
#find the avg of a list of numbs.


list_num = [20,25,10,50,45]
sum = 0 #everythime we do the calculation pr start counting in a loop, we must give a variable a value of zero for the starting point. Otherwise, it will give error cuz it does not know where to start.
for z in list_num:
    sum = sum + z
print("Sum=" , sum)
print("Average = ", sum/len(list_num))

#We put sum = sum + z because the first sum in the line is constantly updating itself
#after each iteration in z 
#if we use summ to replace the first sum, then we only get the last value within the list 
#because it is not updated and the original sum outside the loop remains zero.



name_list = [23,34,23,12,53]
sum = 0 

for u in name_list:
    sum = sum + u

print(round(sum/len(name_list)))

#----------------------------------

#for loop using tuple
num = [23,23,43,12,54,8]
sum = 0

for i in num:
    sum = sum + i
    print(sum) #This print within the loop and above the sum = sum + i is like
    # a visualization of the sum = sum + i bcuz it will show u the summing each value

print("This is", sum)


#----------------------------------

#range function

for i in range(1,11,2):
    print(i)

#program to print table of a given number

#If what we need to calculate is summing or decreasing, we can use starting point like sum = 0
#But, if we want to calcuate is multipying and diving, we dun need to use the starting point
#This method does not need to have input to execute

n = int(input("Enter Number: "))
for i in range(1,11):
    mul = n*i 
    print(n,"*",i,"=",mul)


print("----------")

list2 = ['C','PYTHON','R']

for i in range(len(list2)):
    print("Hello", list2[i])

#---------------------------------
#Nested loop

companies = ["giii", 'syu','aty']
for i in companies:
    print("We will display each letter of " , i)

    for letter in i:
        print(letter)

#---------------------------------
#for loop with else clause

for i in range(1,4):
    
    print(i)
       

print("Done") 




#---------------------------------
print("----------")
#---------------------------------
players = "w"
goals = {"E": 21,
         'd':2,
         'w':3}

for player in goals:
    if player == players:
        print(goals[player])
        break
        
else: 
    print('No player with that name found')


#---------------------------------
print("----------")
#---------------------------------


n = int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(0, i+1):
        print("*",end="")
    print()


#BIG ASSSSSSSSSSSSSSSSSSSSSSSSSSSS
#While Loops: used to iterate over a part of code till the specified condition is True

#Syntax:
#while expression:
    #statement(s)

# while True: (to keep codes in a loop). If False, exit while loop

i = 0  #everythime we do the calculation pr start counting in a loop, we must give a variable a value of zero for the starting point. 
        #Otherwise, it will give error cuz it does not know where to start.

while i < 10:
    i = i + 1
    print(i, end="")
    print()    
    

count = 0
while count <=5:
    count += 1
    print("True")
    break
    

#while True:
 #   print(input("Enter Name: "))
  #  name = input()
   # if name == "Gilly":
    #    break


   
#print("Thanks! ")


#---------------------------------
print("----------")
#---------------------------------

#Nested Loops: a loop in another loop
#syntax: out loop: 
        # Inner loop:
                #statement of inner loop
            #statement of outer loop

#you can put out loop or inner loop as for loop or while loop together as a nested loop


list_fruits = ['mango','apple', 'banana']
for fruit in list_fruits:
    for i in fruit:
        print(i,end=" ")
    print()



list_fruits = ['mango','apple', 'banana']
for fruit in list_fruits:
    print(fruit, end=" ")



print(" ")

#---------------------------------
print("----------")
#---------------------------------

color = ['red','blue']
item= ['apple','ball']

for x in color:
    for y in item:
        print(x,y)
        print('')


list1 = [12,32,35,65]
list3 = [21,55,65,78]
result=[]

for i in list1:
    for j in list3:
        result.append(i+j) #is to add the numbers tgt into the original list which is the result = []

print(result)