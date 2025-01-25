class Parallelepipedo:
    def __init__(self, larghezza: float, altezza: float, profondita: float):
        self._larghezza = larghezza
        self._altezza = altezza
        self._profondita = profondita

    def superficie(self) -> float:
        return (2*(self._larghezza * self._altezza)+ 2 * (self._larghezza * self._profondita) + 2 * (self._altezza * self._profondita))

    def volume(self) -> float:
       return self._larghezza * self._altezza * self._profondita

def main():
    larghezza = float(input("Inserisci la larghezza del parallelepipedo: "))
    altezza = float(input("Inserisci l'altezza del parallelepipedo: "))
    profondita = float(input("Inserisci la profondità del parallelepipedo: "))

    parallelepipedo = Parallelepipedo(larghezza, altezza, profondita)

    print(f"Superficie del parallelepipedo: {parallelepipedo.superficie():.2f}")
    print(f"Volume del parallelepipedo: {parallelepipedo.volume():.2f}")

if __name__ == "__main__":
    main()
