def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(4))

''' Fibonacci series'''

a = 0
b = 1
def fib(n):
    # base case of recursion
    if(n == 0 or n == 1):
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(9))