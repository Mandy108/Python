# a = 4 
# b = 4 
# c = 4
# average = (a+b+c)/3
# print(average)

# def average(a,b,c):
#     d =(a + b + c) / 3
#     print(d)

# average(3,5,1)

def average(a,b,c):
    d =(a + b + c) / 3
    return d

o1 = average(3,5,1)
o2 = average(7,5,6)
print(o1,o2)

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))