# Continue Statement
for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")


# another example of continue statement
for char in "navttc":
    if char == 't':
        continue
    print(char, end=" ")