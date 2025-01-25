from math import e, exp

class ModelloEsponenziale:
    def __init__(self, a: int, b: int, c: int):
        self._a = a
        self._b = b
        self._c = c
        
    def estimate(self, x: int) -> float:
        return (self._a * e ** (self._b * x)) + self._c
    
def main():
    try:
        a = int(input("Valore coefficiente a? "))
        b = int(input("Valore coefficiente b? "))
        c = int(input("Valore coefficiente c? "))
    except ValueError:
        print("Errore: Inserisci un valore intero valido per i coefficienti.")
        return
    
    modello = ModelloEsponenziale(a, b, c)
    x = input("Valore di x? ")

    while x != "":
        try:
            numero = int(x)
            result = modello.estimate(numero)
            print(f"Il risultato dell'equazione per la x inserita è {result}")
        except ValueError:
            print("Errore: Inserisci un valore intero valido per x.")
        
        x = input("Valore di x? ")
    
    print("Programma terminato")

if __name__ == "__main__":
    main()
