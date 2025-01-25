from lista_di_cifre import digits

def sum_digits(num: int):
    if num < 10:
        return num # Se n è minore di 10, n è il risultato
    tot = sum(digits(num)) # Altrimenti, calcola la somma s delle cifre di n…
    return sum_digits(tot)

def main():
    while n := input("n? "):
        n = int(n)
        print(sum_digits(n))

if __name__ == "__main__":
    main()