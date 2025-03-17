def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Calcular el número de Fibonacci de 10
resultado = fibonacci_iterativo(10)
print(f"El número de Fibonacci de 10 es: {resultado}")