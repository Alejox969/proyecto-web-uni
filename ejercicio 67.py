def es_primo(n):
    if n < = 1:
        return False
    if n < = 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i= 5
    while i*i < = n:
        if n % i == 0 or n % (i+2) ==0:
            return False
        i += 6
        return True
    def es_capicua(n):
        s=str(n)
        return s == S [::-1]
    def main():
        numero = int(input("Introduce M:"))
        if es_primo(numero):
            print(f"{numero}M es primo")
        else:
            print(f"{numero}M no es primo")
            if es_capicua(numero):
                print(f"{numero}M capicua")
            else:
                print(f"{numero}M no capicua")
                if_name_ == "_main_":
                main()