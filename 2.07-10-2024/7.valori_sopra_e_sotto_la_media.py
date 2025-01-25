numero = int(input("Inserisci un numero intero (0 per terminare): "))
numeri = []

while numero != 0:
    numeri.append(numero)
    numero = int(input("Inserisci un altro numero intero (0 per terminare): "))

if numeri:
    media = sum(numeri) / len(numeri)
    print(f"\nLa media dei numeri inseriti è: {media:.2f}")

    sotto_media = [n for n in numeri if n < media]
    print(f"Valori sotto la media: {sotto_media}")

    sopra_o_uguale_media = [n for n in numeri if n >= media]
    print(f"Valori sopra o uguali alla media: {sopra_o_uguale_media}")
else:
    print("Non sono stati inseriti numeri validi :()")

print("Programma terminato!")
