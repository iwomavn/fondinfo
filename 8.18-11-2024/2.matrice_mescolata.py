from random import shuffle  # Importa la funzione shuffle dal modulo random per mescolare liste.

w = int(input("w? "))  # Chiede all'utente di inserire la larghezza (numero di colonne) della matrice e la converte in intero.
h = int(input("h? "))  # Chiede all'utente di inserire l'altezza (numero di righe) della matrice e la converte in intero.

matrix = list(range(1, w * h + 1))  # Crea una lista con numeri consecutivi da 1 a w*h (inclusi).
shuffle(matrix)  # Mescola casualmente gli elementi della lista `matrix`.

with open("_matrix.csv", "w") as outfile:  # Apre (o crea) un file `_matrix.csv` in modalità scrittura.
    for y in range(h):  # Cicla su ogni riga della matrice (totale h righe).
        for x in range(w):  # Cicla su ogni colonna della riga corrente (totale w colonne).
            end = "\n" if x == w - 1 else "," # Determina l'ultimo carattere da stampare: "\n" per l'ultima colonna della riga, altrimenti ",".
            print(matrix[x + y * w], end=end, file=outfile)  # Scrive nel file il valore corrispondente dalla matrice mescolata, separandolo con una virgola o andando a capo.