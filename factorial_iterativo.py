import time

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
    def calcular_coste_factorial(n):
        start_time = time.time()
        factorial_iterativo(n)
        end_time = time.time()
        return end_time - start_time

    # Ejemplo de uso
    if __name__ == "__main__":
        numero = 900
        print(f"El factorial de {numero} es {factorial_iterativo(numero)}")
        tiempo = calcular_coste_factorial(numero)
        print(f"El tiempo de ejecución para calcular el factorial de {numero} es {tiempo} segundos")
