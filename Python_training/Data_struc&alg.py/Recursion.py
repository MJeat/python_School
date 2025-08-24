# Recursion: is a technique where a function calls itself to solve smaller instances of the same problem. 
                # apply the result of a procedure, to a procedure
                
                # divide a problem into smaller problems of the same type of the original
                
                # commonly used with advanced soting algorithms and navigating trees





# Recursion does not only call its function from the outside of the function, but also the inside
# Example in the second example, we can see that below the else statement, there is a function to be called. and outside also has one 

import time

def open_doll(dolls):
    if dolls == 1: # Basecase. The end of our search. Cannot further search
        return "You found the smallest doll!"
    else:
        print(f"Opening doll number {dolls}")
        return open_doll(dolls - 1)

# Example usage:
print(open_doll(5))

# so the return open_doll(dolls - 1) continues to execute until it reaches if dolls == 1:, then return "You found the smallest doll!"



#--------------------------------------------------------------------
print('--------------------------------------------------------')

def count_down(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        count_down(n - 1)

# Example usage:
count_down(5)

#--------------------------------------------------------------------
print('--------------------------------------------------------')

#These below are the reasons to use Recursion method: 



#   Factorial Calculation: Used to calculate the factorial of a number.

#   Fibonacci Sequence: Used to generate numbers in the Fibonacci sequence.

#   Tree Traversal: Used to traverse tree-like data structures, visiting each node in a systematic way.

#   Sorting Algorithms: Used to sort a list of elements into a particular order.

#   Backtracking Algorithms: Used to solve problems by trying different options recursively, and backtracking when a dead-end is reached.

#   Directory Traversal: Used to navigate through directory structures on a computer.

#   Graph Traversal: Used to traverse graphs, visiting each vertex or edge in a systematic way.
#-----------------------------------------------------------------------------------
# Example 3: 
# For fibonacci sequences:

def fibonacci(idx):
    if idx <= 1:
        return idx
    else: 
        return fibonacci(idx -1 ) + fibonacci(idx -2)
    
print(fibonacci(8)) # you might be confused why it outputs 21. Just go check fibonacci sequences index and number



#--------------------------------------------------------------------
print('--------------------------------------------------------')
# Iteration vs recursion:



# Recursion: 
def fibonacci(idx):
    if idx <= 1:
        return idx
    else: 
        return fibonacci(idx -1 ) + fibonacci(idx -2)
    
#print(fibonacci(8))



# Iteration:
def Fibonacci(idx):
    seq = [0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

#print(Fibonacci(8))


# Which one is faster? 

print("Iteration")
it = time.time()
print(Fibonacci(8))
print('Speed: ' , str(time.time()-it))

print("Recursion")
rec = time.time()
print(fibonacci(8))
print('Speed: ' , str(time.time()-rec))

#--------------------------------------------------------------------
print('--------------------------------------------------------')
# Additional exercises:

def factorial(nums):
    if nums == 0 or nums == 1:
        return 1
    else:
        return nums* factorial(nums -1)  #So, as you correctly pointed out, the nums value remains the same (5 in this case) throughout the recursive calls, while the factorial(nums - 1) part keeps changing until it reaches the base case. 
                                        #This process allows the function to calculate the factorial of the original number by breaking down the problem into smaller subproblems.
print(factorial(5))

# Recursion works best with large files cuz it can chob the data into smaller chunk for us to easily debug and understand

