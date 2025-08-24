# Stack: a LIFO data structure. LIFO means Last-In First-Out

# uses to store objects into a sort of vertical tower like a stack of books
# uses push() method to add objects to the top (Java)
# uses pop() method to remove objects from the top (Java)


#------------------------------------------------------------------
s = []

s.append(3)
s.append(4)
s.pop() #This guy remove the latest item, which is s.append(4)

print(s)


#Using list as a stack is not recommended. Because if the list needs to grow extra space, it's gonna be an issue.
#It is recommened to use collection.deque (double-ended queue) or queue.LifoQueue
#------------------------------------------------------------------

from collections import deque 
stack = deque()

stack.append("Hello")
stack.append(4)

stack.pop() #If you put this and print stack, it will only display 'Hello'

print(stack)
print(stack.pop()) #But if you put stack.pop() in the print, it will display the item that you pop out of the stack which is 4

#------------------------------------------------------------------

#Quiz:
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"









