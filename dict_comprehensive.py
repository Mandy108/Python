a = int(input("Give a number: "))
table = {i: a * i for i in range(1,11)}
print(table)

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}