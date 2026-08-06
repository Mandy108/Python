def sum(a,b):
    c = a + b
    z = 8 #local variable only access in where it exists
    print(z)
    return c
z = 0 # global variable
print("z" ,z)
print(sum(4,6))

