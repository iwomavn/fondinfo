class PolynomialModel:
    def __init__(self, coeffs: list[float]):
        self.coeffs = coeffs

    def estimate(self, x: float) -> float:
        y = 0
        for i, coeff in enumerate(self.coeffs):
            y += coeff * (x ** i) 
        return y

def main():
    coeffs = [float(c) for c in input("Inserisci i coefficienti del polinomio separati da spazio: ").split()]
    
    modello = PolynomialModel(coeffs)
    
    while True:
        value = input("Inserisci un valore di x (lascia vuoto per terminare): ")
        if not value:  
            print("Termine del programma.")
            break
        try:
            x = float(value) 
            y = modello.estimate(x) 
            print(f"Per x = {x}, il valore del polinomio è y = {y}")
        except ValueError:
            print("Inserisci un numero valido.")

if __name__ == "__main__":
    main()
