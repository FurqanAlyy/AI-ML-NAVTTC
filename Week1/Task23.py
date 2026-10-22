# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)

model = 'ChatGPT'
# Access the first character
print(model[0])    

#  Access the fourth last character
print(model[-4])  

# String are immuatable, so we cannot change the characters of a string
model[0] = 'W'
print(model)

model = 'Opus'
version = '5'
model = model + " " + version
print(model)   

# Replace Text
text = "ChatGPT is great."
new_text = text.replace("ChatGPT", "Claude")
print(new_text) 

print(len(model)) 

# Escape characters
# escape double quotes
example = "He said, \"What's there?\""

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)
