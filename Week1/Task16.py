# while loop
count = 0
while count < 3:
    count = count + 1
    print("Hello World")

# infinite loop
age = 28
while age > 19:
    print('Infinite Loop')

# using continue statement
i = 0
a = 'Hello NAVTTC'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1

# using break statement
i = 0
a = 'Hello NAVTTC'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        break
    print(a[i])
    i += 1