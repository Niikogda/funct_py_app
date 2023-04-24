
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    try:
        n = int(input("Enter a positive integer: "))
        result = fibonacci(n)
        if result is None:
            print("Invalid input: n must be a positive integer")
        else:
            print(f"The {n}-th element of the Fibonacci sequence is: {result}")
        break
    except ValueError:
        print("Invalid input: n must be a positive integer")
