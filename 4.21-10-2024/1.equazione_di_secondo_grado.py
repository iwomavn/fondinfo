import math

def solve_quadratic(a: int, b: int, c: int):
    delta = (b * b) - 4 * a * c

    if delta < 0:
        raise ValueError("Discriminante negativa")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        return (x1, x2)

def main():
    while True:
        a = input("Valore coefficiente a? (Premi invio per uscire): ")
        if a == "":
            break
        try:
            # Convertiamo 'a', 'b' e 'c' in interi solo dopo che sappiamo che 'a' non è vuoto
            a = int(a)
            b = int(input("Valore coefficiente b? "))
            c = int(input("Valore coefficiente c? "))

            (sol1, sol2) = solve_quadratic(a, b, c)
            print(f"I risultati dell'equazione inserita sono x1 = {sol1} e x2 = {sol2}")

        except ValueError as e:
            print(f"Errore: {e}")
        except Exception as e:
            print("Errore: inserisci solo numeri interi validi per a, b, e c.")
    
    print("Programma terminato")

if __name__ == "__main__":
    main()
