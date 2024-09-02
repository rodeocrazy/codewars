"Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5."



def fizzbuzz(i):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        print("Fizz")
        

    if i % 5 == 0:
        print("Buzz")

fizzbuzz(15)