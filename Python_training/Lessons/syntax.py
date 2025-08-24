
#THIS IS ABOUT FUNCTION.
#--------------------------------------------------------------------------
def time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours,minutes,remaining_seconds


hours,minutes, remaining_seconds = time(5000)
print(hours,minutes,remaining_seconds)


def greeting(name):
    print("Welcome, ", name)

x= greeting("John")

print(x)



def lucky_number(name):
    names = len(name)*9
    print("Hello ", name, ". Your lucky number is ", str(names))
    return names

lucky_number("Jeat")
lucky_number("Bob")


def circle_area(radius):
    pi = 3.14
    area = pi * (radius**2)
    print(area)

circle_area(5)


def rectangle_area(area,b):
    a = area/b
    print(a)

rectangle_area(23,32)




while True:
    def login_username(username):
        if len(username) < 3:
            print("Invalid. The length is too short.")
        elif len(username) > 15:
            print("The length is too long.")
        else:
            print("Hello, ", username)


    login_username(input("Enter Your Username: "))

#--------------------------------------------------------------------------
    
    