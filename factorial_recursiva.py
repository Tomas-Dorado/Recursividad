def factorial_recursivo(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def coste_factorial_recursivo(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return 1 + coste_factorial_recursivo(n - 1)

# Ejemplo de uso
if __name__ == "__main__":
    numero = 900
    print(f"El factorial recursivo de {numero} es {factorial_recursivo(numero)}")
    print(f"El coste del factorial recursivo de {numero} es {coste_factorial_recursivo(numero)}")