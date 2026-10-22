import cmath
num = eval(input("Enter a number: "))

num_sqrt = cmath.sqrt(num)
print("The square root of {0} is {1} + {2}i".format(num, num_sqrt.real, num_sqrt.imag))