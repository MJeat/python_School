# Queue is a FIFO data structure. First-In First-Out. Like those who came in first will be served first. 
#Unlike queue, for stack, those who comes in first will be served last.


#A collection designed for holding elements prior to processing
#Linear data structure


#For stack, when u pop, you pop the latest data.
#For Quere, when you pop, you pop the first data (the head)


Fruits = []

Fruits.insert(0,123)
Fruits.insert(0,"apple")
Fruits.insert(0,'Banana')       #The reason why output is Banana 
                                #cuz it only prints the latest line of code which the system consider the first costumer to be served first.

print(Fruits)

#when you pop, it only takes out the first costumer, not the last costumer, unlike stack.
Fruits.pop()

print(Fruits)                   #This will display the data without the first costumer
print(Fruits.pop())             #This will only display the data that it has popped out


# Note: when you pop out everything in the list, it will out error when you pop out an empty list.
#This below is just another coolder way to use queue


from collections import deque
q = deque()

q.appendleft(5)
q.appendleft(54)
q.appendleft(52)


print(q.pop())          #Now, this pops the first line of the code which is q.appendleft(5). 
                        #Do not get confused with above


#------------------------------------------------------------------------------------------------------
print("--------------------------------------------------------------")
# To fix error, we use the collections technique, which can be used for both stack and queue.


from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):      # Enqueue: is adding into the queue
        self.buffer.appendleft(val)

    def dequeue(self):          # Dequeue: is taking out of the queue
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

# After writing like a structure to store ur data (as shown above), we write the code

stock = Queue()

stock.enqueue({
    'company': 'Walmart',
    'time': '11:21am',
    'price': 123
})

stock.enqueue({
    'company': 'AEON',
    'time': '11:32am',
    'price': 165
})

stock.enqueue({
    'company': '7/11',
    'time': '12pm',
    'price': 312
})

#Now call the every dictionary:

print(stock.buffer)

# Now call the enqueue:

print(stock.dequeue() )

#Checking the size (amount of enqueues)
print(stock.size()) # It displays 2 instead of 3 cuz I dequeue 1 above.



#------------------------------------------------------------------------------------------------------
print("------------------------------------------------------")
#------------------------------------------------------------------------------------------------------

#Exercise:



from collections import deque

class Orders:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    


orders = ['pizza','samosa','pasta','biryani','burger']


orders = Orders()

orders.enqueue(['pizza',
                'samosa',
                'pasta',
                'biryani',
                'burger'])





        