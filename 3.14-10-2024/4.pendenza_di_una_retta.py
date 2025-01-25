def slope(p1: tuple, p2: tuple) -> float:
    """
    Calcola la pendenza della retta passante per i punti p1 e p2.
    Solleva un ValueError se i due punti sono allineati verticalmente.
    """
    x1, y1 = p1
    x2, y2 = p2

    # Controllo se i punti sono allineati verticalmente
    if x1 == x2:
        raise ValueError("I due punti sono allineati verticalmente, la pendenza non è definita.")

    # Calcola la pendenza
    return (y2 - y1) / (x2 - x1)

def main():
    while True:
        # Acquisisci i punti dall'utente
        try:
            x1 = float(input("Inserisci la coordinata x1 del primo punto: "))
            y1 = float(input("Inserisci la coordinata y1 del primo punto: "))
            x2 = float(input("Inserisci la coordinata x2 del secondo punto: "))
            y2 = float(input("Inserisci la coordinata y2 del secondo punto: "))

            # Crea le tuple per i due punti
            p1 = (x1, y1)
            p2 = (x2, y2)

            # Calcola e mostra la pendenza
            result = slope(p1, p2)
            print(f"La pendenza della retta che passa per i punti {p1} e {p2} è: {result:.2f}")

        except ValueError as e:
            print(f"Errore: {e}")

        # Chiedi se l'utente vuole continuare
        choice = input("Vuoi calcolare la pendenza per altri punti? (s/n): ").lower()
        if choice != 's':
            print("Programma terminato.")
            break

if __name__ == "__main__":
    main()
