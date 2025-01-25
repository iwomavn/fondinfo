anno = int(input("Inserisci un anno per vedere se è bisestile! (Inserire 0 per uscire dal programma): "))

while anno != 0:
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        print(f"L'anno {anno} è bisestile!")
    else:
        print(f"L'anno {anno} non è bisestile!")
    
    anno = int(input("Inserisci un anno e ti dirò se è bisestile! (Inserire 0 per uscire dal programma): "))

print("Programma terminato!")
