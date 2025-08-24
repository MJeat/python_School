

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

#('+', 4, 7) --> 11
#('-', 15, 18) --> -3
#('*', 5, 5) --> 25
#('/', 49, 7) --> 7
# Mine
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '/':
        return value1 / value2
    elif operator == '*':
        return value1 * value2



# ChatGPT:
import operator
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def basic_op(operator, value1, value2):
    return operations[operator](value1, value2)     # ohhhh so like the operations[operator] is the value which is used to operate the (value1, value2) 


# Others code:
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

