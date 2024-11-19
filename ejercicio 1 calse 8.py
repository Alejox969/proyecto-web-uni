
def es_primo(x):

    c=0

    for d in range(2, x//2, 1):

        if x % d == 0:

            c=c+1

    if c == 0:

        return True

    else:

        return False


def es_capicua(x):

    c=x

    inv=0

    while c > 0:

        d = c % 10

        inv = inv * 10 + d

        c =c// 10

    if c == x:

        return True

    else:

        return False


def main():

    # Leer un número del usuario

    m = int(input("Ingresa un número: "))


    # Verificar si el número es primo

    if es_primo(m)==True:
        print(f"El número {m} es primo.")

    else:

        print(f"El número {m} no es primo.")


    # Verificar si el número es capícua

    if es_capicua(m)==True:
        print(f"El número {m} es capícua.")

    else:

        print(f"El número {m} no es capícua.")


if __name__ == "__main__":

    main()