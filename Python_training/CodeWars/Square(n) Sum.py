

def square_sum(numbers): 

    square_sum = 0
    for i in numbers:
        square_sum += i** 2

    return square_sum











# Use this when there are multiple elements to be inserted. For more info, go to pycharm and find lesson "args".
def square_sum(*numbers): 

    square_sum = 0
    for i in numbers:
        square_sum += i** 2

    return square_sum


result = square_sum(1,2,3,4,5,6)
print(result)
