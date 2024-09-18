def fibonacci(n):
    fib1=0
    fib2=1
    print(f"the First {n} Fibonacci numbers are")
    print(fib1)
    print(fib2)
    while n>2:
        fib3=fib1+fib2
        if fib3<n:


n=int(input("Enter a number:"))

fibonacci(n)