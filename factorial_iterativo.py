def factorial_iterativo(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    numero = 900
    print(f"El factorial de {numero} es {factorial_iterativo(numero)}")