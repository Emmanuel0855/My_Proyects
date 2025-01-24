def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create the generator
fib = fibonacci()

# Get the first 10 Fibonacci numbers using a list comprehension
fib_seq = [next(fib) for _ in range(10)]

print(fib_seq)