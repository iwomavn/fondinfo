# Ciclo esterno sulla variabile y
for y in range(1, 6):
    # Ciclo interno sulla variabile x
    for x in range(1, 6):
        # Calcola la distanza assoluta tra x e y
        distanza = abs(x - y)
        # Mostra la distanza per ogni x, con separatore di tabulazione
        print(distanza, end="\t")
    
    # Aggiunge un newline alla fine di ogni riga (una volta completato il ciclo su x)
    print()
