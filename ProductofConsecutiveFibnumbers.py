def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 


def productFib(prod):

    for i in range(prod):
        if Fibonacci(i) * Fibonacci (i+1) == prod:
            return[Fibonacci(i), Fibonacci(i+1), True]
        elif Fibonacci(i) * Fibonacci (i+1) > prod:
            return[Fibonacci(i), Fibonacci(i+1), False]


####Too slow in compiling > 12 seconds, gave up.