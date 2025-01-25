def main():
    # Inizializza una lista vuota per memorizzare i numeri
    numeri = []

    # Chiedi all'utente di inserire una sequenza di interi, terminata da 0
    print("Inserisci una sequenza di numeri interi (termina con 0):")
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeri.append(numero)  # Aggiungi il numero alla lista

    # Verifica se la lista non è vuota
    if len(numeri) == 0:
        print("Nessun numero è stato inserito.")
        return

    # Calcola la media
    n = len(numeri)
    media = sum(numeri) / n
    print(f"Media (μ) = {media:.2f}")

    # Calcola la varianza
    varianza = sum((x - media) ** 2 for x in numeri) / n
    print(f"Varianza = {varianza:.2f}")

if __name__ == "__main__":
    main()
