tuple1 = (1, 2, 3)

# tuple with mixed datatypes
tuple2 = (1, "Hello", 3.4)

# nested tuple
tuple3 = ("mouse", [8, 4, 6], (1, 2, 3))

# also called tuple packing
my_tuple = 3, 4.6, "dog"
# tuple unpacking is also possible
a, b, c = my_tuple

my_tuple = ("hello",)  # need a comma at the end
type(my_tuple)

# accessing tuple elements
my_tuple = ['p','e','r','m','i','t']
my_tuple[0]

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
n_tuple[0][3]  # nested index

# negative indexing in tuple
print(my_tuple[-1])

# accessing a range of values in tuple
print(my_tuple[1:4])

# return the values from the tuples
print(my_tuple.count('p'))
print(my_tuple.index('l'))

# iterating through a tuple
for name in ('John','Kate'):
  print("Hello",name)