# name = "Mandy"
# print(name[0], name[-1], len(name))

# # Concatenate Two String
# a = "Mandeep"
# b = "Samrat"
# result =f"{a} {b}"
# print(result)

# text = "Python Programming"
# print(text[:6] , text[-6:], len(text), text[::2])

# print(text[::-1])


# a = "  i love python programming  "
# print(a.strip() , a.title(), a.count("o") )

# b = "123abc"
# print(b.isalnum())


#String Formatting and f-Strings
# name = "john"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
# print("My name is {} and I am {} years old.".format(name,age))



# sentence = "Coding in Python is fun"
# sum = 0
# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in sentence.lower(): 
#     if(char in vowels):
#         sum += 1

# print(f"There are {sum} vowels in this sentence")

# str1 = "level"
# if(str1 == str1[::-1]):
#     print("Palindrom")
# else:
#     print("! Palindrom")
    

#String Manipulation Challenges

sentence = "Coding in Python is fun"
print(sentence.replace("fun", "awesome"), sentence.upper(), sentence.index("Python"))
