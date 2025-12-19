#printing fibonacci numbers upto a given limit(n) using python generator(yield)
n = int(input("enter limit:")) 

def fibonacci_generator(n):
    if n< 0:
        raise ValueError("the fibonacci limit(n) cannot be negative")

    a = 0
    b = 1
    
    while a<= n:
        c = a+b
        yield a
        a, b = b, c

list = [ a for a in fibonacci_generator(n)]
print(list)


