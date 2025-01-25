import math

def heron(firstSide: float, secondSide: float, thirdSide: float):
    lati = [firstSide, secondSide, thirdSide]
    for lato in lati:
        if lato <= 0:
            raise ValueError("I lati devono essere maggiori di zero!")
    
    if not (firstSide + secondSide > thirdSide and firstSide + thirdSide > secondSide and secondSide + thirdSide > firstSide):
        raise ValueError("I lati forniti non possono formare un triangolo valido!")
    
    perimetro = (firstSide + secondSide + thirdSide) / 2
    area = math.sqrt(perimetro * (perimetro - firstSide) * (perimetro - secondSide) * (perimetro - thirdSide))
    
    return area

def main():
    lato1 = float(input("Inserisci il valore del primo lato: "))
    lato2 = float(input("Inserisci il valore del secondo lato: "))
    lato3 = float(input("Inserisci il valore del terzo lato: "))
    
    try:
        risultato = heron(lato1, lato2, lato3)
        print(f"L'area del triangolo calcolata con la formula di Erone è {risultato}")
    except ValueError as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()  
