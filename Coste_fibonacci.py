def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_cost(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_cost(n-1) + fibonacci_cost(n-2) + 1

n = 10  # Example value
print(f"Fibonacci({n}) = {fibonacci(n)}")
print(f"Cost of Fibonacci({n}) = {fibonacci_cost(n)}")

# The time complexity of the fibonacci function is O(2^n)
# The time complexity of the fibonacci_cost function is also O(2^n)