# defining a function
def fun():
    print("Welcome to GFG")
    
fun()

# function with default argument
def myFun(x, y):
    print("x: ", x)
    print("y: ", y)

myFun(10, 20)

# function using args and kwargs
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Netsol', mid='Institute', last='AI')

# function with return statement
def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-4))

# value pass by reference
def myFun(x):
    print("Value received:", x)
    x[0] = 20
    print("Value changed to:", x)

a=[10, 11, 12, 13, 14, 15]
myFun(a)