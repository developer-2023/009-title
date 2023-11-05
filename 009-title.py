# docs.python.org/3/library/stdtypes.html#string-

# Ask user for their name
name = input("What's your name and surname? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name and surname
name = name.title()

# Say hello to user
print(f"hello, {name}!")