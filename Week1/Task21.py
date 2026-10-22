cart = ["T-shirt", "Lamp", "Pen"]
print(cart)

# A list of mixed data types
my_list = [1, "Python", 3.14]
print(my_list)

vowels = "aeiou"
# Convert a string to a list
vowels_list = list(vowels)
print(vowels_list)

# accessing through negative indexing
print('cart[-1] =', cart[-1])

# Update second item to "Shoes"
cart[1] = "Shoes"
print(cart) 

cart.append("Book")  
# add an item to the end of the list
print(cart)


# Add all the items from fav_items to cart
fav_items = ["Headphones", "Phone"]
cart.extend(fav_items)

# Remove the last item
last_item = cart.pop()
print("Removed item:", last_item)

#  Delete the third item (index 2)
del cart[2]
print(cart)

# len()function
print("Length of cart:", len(cart))

