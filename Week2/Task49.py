import numpy
from scipy import stats

# Example 1 - Mean
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

# Example 2 - Median with an odd number of values
x = numpy.median(speed)
print(x)

# Example 3 - Median with an even number of values
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

# Example 4 - Mode
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)
