def fibonacci(n):
    fib1=0
    fib2=1
    print(f"the First {n} Fibonacci numbers are")
    print(fib1)
    print(fib2)
    while n>2:
        fib3=fib1+fib2
        print(fib3)
        fib1=fib2
        fib2=fib3
        n-=1


n=int(input("Enter a number:"))

fibonacci(n)