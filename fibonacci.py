def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

def print_fibonacci_pyramid(levels):
    fib_seq = fibonacci(levels)
    for i in range(1, levels + 1):
        print(' ' * (levels - i) + ' '.join(map(str, fib_seq[:i])))

if __name__ == "__main__":
    levels = int(input("Enter the number of levels for the Fibonacci pyramid: "))
    print_fibonacci_pyramid(levels)
