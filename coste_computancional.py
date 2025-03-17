import time

def numeros_pares_impares(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")

# Ejemplo de uso
numeros_pares_impares(10)
def analizar_coste_computacional():
    n = 10000
    start_time = time.time()
    numeros_pares_impares(n)
    end_time = time.time()
    print(f"Tiempo de ejecución para n={n}: {end_time - start_time} segundos")

# Ejemplo de uso
analizar_coste_computacional()