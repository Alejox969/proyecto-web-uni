def fibonacci(n):
    """
    Calcula la secuencia de Fibonacci para el número n.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def serie2(n):
    """
    Calcula la serie 2 (1, 3, 5, 7, 9, ...)
    para el número n de términos.
    """
    lista = []
    for i in range(n):
        lista.append(2 * i + 1)
    return lista


def serie3(n):
    """
    Calcula la serie 3 (1, 4, 9, 16, 25, ...)
    para el número n de términos.
    """
    lista = []
    for i in range(n):
        lista.append((i+1) ** 2)
    return lista
try:
    n = int(input("Ingresa un entero positivo: "))
    print("La secuencia de Fibonacci para", n, "es:")
    for i in range(n):
        print(fibonacci(i))
        print()
    print("La serie 2 para", n, "términos es:", serie2(n))
    print("La serie 3 para", n, "términos es:", serie3(n))
except:
    print("Error: Ingresa un entero positivo.")
