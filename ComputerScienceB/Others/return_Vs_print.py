
def add(a, b):
    print(a + b)   # Just shows it

def add_v2(a, b):
    return a + b   # Gives it back

# Now try to use them:
x = add(2, 3)      # prints "5", but x = None
y = add_v2(2, 3)   # y = 5 → you can use it!

print("The value of X is:"+x)  # None
print("The value of Y is:"+ y)  # 5
print(y * 2)  # 10 → useful!

'''

The difference between return and print:
1. print() displays the result on the screen but does not store it for later use.
    Simple: It's like saying "Here's the value, but you can't have it."
Not to mention, print() sometimes outputs ONCE. Like printing in real life. You see it, but it's gone. 
    
2. return sends the result back to the caller, allowing it to be stored in a variable or used in further calculations.
    Simple: It's like saying "Here's the value, you can keep it and use it later."

Use Cases:
-> print() is great for debugging
                    for when you want to show information to the user.
                    for printing ONCE
-> return is essential in functions that perform calculations or data processing
                    when you need to use the result multiple times
                    when you want to chain functions together
                    When you want to store the result in a variable for later use

    Practice: What's the value of "a"? ->
def mystery(x):
    print(x * 2)
    return x + 3

a = mystery(4)
print(a)

'''




