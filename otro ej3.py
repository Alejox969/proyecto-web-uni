def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def mayor_que(num1, num2, num3):
    return max(num1, num2, num3)

def menor_que(num1, num2, num3):
    return min(num1, num2, num3)

def main():
    print("Ingrese tres números para comparar:")
    
    num1 = obtener_numero("Número 1: ")
    num2 = obtener_numero("Número 2: ")
    num3 = obtener_numero("Número 3: ")
    
    mayor = mayor_que(num1, num2, num3)
    menor = menor_que(num1, num2, num3)
    
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

if __name__ == "__main__":
    main()