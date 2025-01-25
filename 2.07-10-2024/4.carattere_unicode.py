numero = int(input("Inserisci un codice unicode per visualizzare il carattere (Inserire 0 per uscire dal programma): "))

while numero != 0:
    carattere = chr(numero)
    print(f"Il carattere corrispondente al codice {numero} è {carattere}")
    numero = int(input("Inserisci un codice unicode per visualizzare il carattere (Inserire 0 per uscire dal programma): "))

print("Programma terminato!")