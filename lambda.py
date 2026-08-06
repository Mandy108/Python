square = lambda x: x * x
sum = lambda x,y: x+y
print(square(4))
print(sum(9,7))

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]