#Big o Notation: 

#Why is Big O Important?
    #Predict Performance: It helps us know if something will take a long time or not as we add more things (like toys).
    #Choose Efficient Ways: Helps us pick the best way to do things so we don’t spend forever on simple tasks.
    #Optimize Activities: Shows us where we might be wasting time and how to fix it.

#Summary
    #O(1): Always the same time, no matter what.
    #O(n): Takes more time as we add more things.
    #O(log n): Takes a little more time, but not too much, as we add more things.
    #O(n^2): Takes a lot more time as we add more things.
    #O(2^n): Takes an incredibly long time as we add more things.

# Big O notation helps us understand and choose the best ways to do things, whether it's in computer programs or everyday tasks!
# By the best way, it means that the fastest and most efficient way. 


box = [1,2,3,4,5,6,7,8,9,0]

for i in range(len(box)):
    if i == 3:
        print("Yes")
    else:
        print('No')
        break

# so you are saying that using range to create an order of number, whereas using len to count the amount of items for the range to create the order
# Yes.



     # CHECK OTHER LESSONS THAT ARE RELATED TO BIG O NOTATION WITHIN THE BIG O NOTATION FOLDER. THIS IS JUST A GUIDE AND THE DEFINITION OF BIG O NOTATION!   