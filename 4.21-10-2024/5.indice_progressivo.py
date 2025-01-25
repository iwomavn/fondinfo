def main():
    # Chiedi all'utente w (larghezza) e h (altezza)
    w = int(input("Inserisci la larghezza (w): "))
    h = int(input("Inserisci l'altezza (h): "))

    # Genera e stampa la tabella
    print("Tabella degli indici progressivi:")
    for y in range(h):  # Riga
        row = []
        for x in range(w):  # Colonna
            i = x * h + y
            row.append(str(i))  # Aggiungi l'indice progressivo alla riga
        print("   ".join(row))  # Stampa la riga come stringa formattata

if __name__ == "__main__":
    main()
