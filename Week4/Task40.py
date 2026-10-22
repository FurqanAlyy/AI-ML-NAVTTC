# Random Numbers in NumPy

from numpy import random
x = random.randint(100)

print(x)

# Generate Random Float

x = random.rand()
print(x)

# Generate Random Array

x=random.randint(100, size=(5))
print(x)

# example

x = random.rand(5)
print(x)

# Generate Random Number From Array

x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)