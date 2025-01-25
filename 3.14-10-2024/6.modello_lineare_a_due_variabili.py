class LinearModel:
    def __init__(self, a: float, b: float, c: float):
        """
        Inizializza il modello lineare con i coefficienti a, b, c.
        La funzione lineare è del tipo: z = a * x + b * y + c
        """
        self._a = a
        self._b = b
        self._c = c

    def estimate(self, x: float, y: float) -> float:
        """
        Calcola il valore della funzione lineare z = a * x + b * y + c per i valori x e y dati.
        """
        return self._a * x + self._b * y + self._c


def main():
    # Chiedi all'utente i coefficienti del modello lineare
    a = float(input("Inserisci il coefficiente a: "))
    b = float(input("Inserisci il coefficiente b: "))
    c = float(input("Inserisci il coefficiente c: "))

    # Crea un'istanza del modello lineare
    modello = LinearModel(a, b, c)

    print("Inserisci i valori di x e y (lascia vuoto per terminare):")

    while True:
        # Chiedi all'utente il valore di x
        x_input = input("x: ")
        if x_input == "":
            print("Programma terminato.")
            break
        # Chiedi all'utente il valore di y
        y_input = input("y: ")
        if y_input == "":
            print("Programma terminato.")
            break

        # Converti gli input in float e calcola la stima del modello
        try:
            x = float(x_input)
            y = float(y_input)
            risultato = modello.estimate(x, y)
            print(f"Il valore della funzione lineare in ({x}, {y}) è: {risultato:.2f}")
        except ValueError:
            print("Errore: devi inserire numeri validi per x e y.")

if __name__ == "__main__":
    main()
