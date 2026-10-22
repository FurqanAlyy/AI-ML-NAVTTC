import numpy

# Example 1
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

# Example 2
speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

# Example 3 - Variance
x = numpy.var(speed)
print(x)

# Example 4 - Standard deviation revisited
x = numpy.std(speed)
print(x)
