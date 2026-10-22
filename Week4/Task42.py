import pandas
import pandas as pd

# Example 1
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)

# Example 2
myvar = pd.DataFrame(mydataset)
print(myvar)

# Example 3
print(pd.__version__)
