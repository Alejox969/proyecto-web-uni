def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def serie2(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result

def serie3(n):
    result = 0
    for i in range(1, n+1):
        result += i**3
    return result

def main():
    while True:
        print("Seleccione una opción:")
        print("1. Calcular n-ésimo número de la serie de Fibonacci")
        print("2. Calcular la suma de los cuadrados de los primeros n números")
        print("3. Calcular la suma de los cubos de los primeros n números")
        print("4. Salir")

        opcion = input("> ")
        if opcion == "1":
            n = int(input("Ingrese un número entero positivo: "))
            resultado = fibonacci(n)
            print(f"El n-ésimo número de la serie de Fibonacci es {resultado}")
        elif opcion == "2":
            n = int(input("Ingrese un número entero positivo: "))
            resultado = serie2(n)
            print(f"La suma de los cuadrados de los primeros {n} números es {resultado}")
        elif opcion == "3":
            n = int(input("Ingrese un número entero positivo: "))
            resultado = serie3(n)
            print(f"La suma de los cubos de los primeros {n} números es {resultado}")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente de nuevo.")