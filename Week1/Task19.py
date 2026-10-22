# enumerate function
words = ['The', 'Netsol', 'AI', 'Class']

for index, value in enumerate(words):
    print(index, value)

# using zip function
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# using items function
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(f"{key}: {value}")

# using sorted function
numbers = [5, 2, 9, 1, 5, 6]
for num in sorted(numbers):
    print(num)

# using reversed function
for num in reversed(numbers):
    print(num)