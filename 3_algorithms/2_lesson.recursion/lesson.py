def factorial(n):
    pro = 1 
    while n > 1 :
        pro *=n
        n-=1
    return pro

print(factorial(4))

def factorial(n):
    if n == 0 :
        return 1 
    else:
        return n * factorial(n-1)

print(factorial(4))

def fib(n):
    a,b = 0 ,1
    while n > 0:
        a,b = b, b+a
        n-=1
    return a 

print(fib(7))

0 1 2 3 5 8 13 21 


def fib(n):
    if n <=1:
        return (n,0)
    else:
        (a,b) = fib(n-1)
        return(a+b,a)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return(fib(n-2)+fib(n-1))

print(fib(7))