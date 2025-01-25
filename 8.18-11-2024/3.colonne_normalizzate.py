def normalize(data: list[float], min_, max_):  # Funzione per normalizzare una lista di dati tra 0 e 1
    if max_ == min_:  # Controlla se `max_` e `min_` sono uguali per evitare una divisione per zero
        return  # Se i valori sono tutti uguali, esce senza modificare i dati
    for i, v in enumerate(data):  # Cicla su ogni elemento `v` della lista `data` con il suo indice `i`
        data[i] = (v - min_) / (max_ - min_)  # Normalizza il valore e lo sostituisce nella lista

def main():
    matrix = []  # Inizializza una lista vuota per contenere i valori della matrice
    h = 0  # Variabile per contare il numero di righe nella matrice
    
    with open("_matrix.csv") as infile:  # Apre il file `_matrix.csv` in modalità lettura
        for line in infile:  # Legge ogni riga del file
            h += 1  # Incrementa il numero di righe della matrice
            matrix += [int(v) for v in line.strip().split(",")]  # Converte i valori della riga (separati da virgola) in interi e li aggiunge alla lista `matrix`
    
    if not matrix:  # Controlla se la matrice è vuota
        return  # Se la matrice è vuota, termina il programma
    
    w = len(matrix) // h  # Calcola la larghezza della matrice dividendo il numero totale di elementi per il numero di righe

    for x in range(w):  # Itera su ogni colonna della matrice (indice `x`)
        col = [matrix[x + y * w] for y in range(h)]  # Estrae tutti gli elementi della colonna `x` in una lista
        min_, max_ = min(col), max(col)   # Trova il valore minimo e massimo della colonna
        print(f"Colonna {x}: min={min_}, max={max_}")  # Stampa i valori minimo e massimo della colonna
        normalize(col, min_, max_)  # Normalizza i valori della colonna
        for y in range(h):  # Aggiorna la matrice con i valori normalizzati della colonna
            matrix[x + y * w] = col[y]  

    with open("matrix2.csv", "w") as outfile:  # Scrive la matrice normalizzata in un nuovo file chiamato `matrix2.csv`
        for y in range(h):  # Itera su ogni riga
            for x in range(w):  # Itera su ogni elemento della riga
                end = "\n" if x == w - 1 else ","  # Determina se terminare la riga con "\n" (a capo) o con "," (virgola)
                print(matrix[x + y * w], end=end, file=outfile)  # Scrive l'elemento della matrice normalizzata nel file `matrix2.csv`

if __name__ == "__main__":  
    main()