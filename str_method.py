# name="mandy" #Strings are immutable

# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())

# text = "hello world"
# print(text.upper())  # Output: "HELLO WORLD"
# print(text.lower())  # Output: "hello world"
# print(text.title())  # Output: "Hello World"
# print(text.capitalize())  # Output: "Hello world"

text = "  hello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"


text = "Python is fun"
print(text.find("is"))   # Output: 7
print(text.replace("fun", "awesome"))  # Output: "Python is awesome"



text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"