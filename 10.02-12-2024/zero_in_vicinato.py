class NeighborZero:
    def __init__(self, filename: str):
        """
        Inizializza la matrice leggendo i dati da un file.
        :param filename: nome del file contenente la matrice
        """
        self.matrix = self.load_matrix_from_file(filename)
    
    def load_matrix_from_file(self, filename: str):
        """
        Carica la matrice da un file.
        :param filename: nome del file contenente la matrice
        :return: matrice di interi
        """
        matrix = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    matrix.append([int(num) for num in line.split()])
        except FileNotFoundError:
            print(f"Errore: il file {filename} non è stato trovato.")
        except ValueError:
            print("Errore: il file contiene dati non validi.")
        return matrix
    
    def has_zero_around(self, x: int, y: int) -> bool:
        """
        Verifica se c'è uno 0 nelle celle adiacenti a (x, y).
        :param x: riga
        :param y: colonna
        :return: True se c'è uno 0 in una delle 4 celle adiacenti, altrimenti False
        """
        # Verifica se le coordinate sono valide
        if x < 0 or x >= len(self.matrix) or y < 0 or y >= len(self.matrix[0]):
            return False
        
        # Verifica le 4 celle adiacenti
        adjacent_positions = [
            (x-1, y),  # sopra
            (x+1, y),  # sotto
            (x, y-1),  # sinistra
            (x, y+1)   # destra
        ]
        
        for i, j in adjacent_positions:
            # Verifica se la posizione è all'interno della matrice
            if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0]):
                if self.matrix[i][j] == 0:
                    return True
        
        return False

def main():
    # Chiedi all'utente il nome del file contenente la matrice
    filename = input("Inserisci il nome del file con la matrice: ")
    
    # Crea l'oggetto NeighborZero
    neighbor_zero = NeighborZero(filename)
    
    while True:
        # Chiedi all'utente una posizione x, y
        input_position = input("Inserisci la posizione (x, y) separata da spazio (o premi Invio per terminare): ")
        
        # Esci se l'input è vuoto
        if input_position == "":
            break
        
        try:
            x, y = map(int, input_position.split())
            if neighbor_zero.has_zero_around(x, y):
                print(f"C'è uno 0 nelle celle adiacenti a ({x}, {y}).")
            else:
                print(f"Non c'è uno 0 nelle celle adiacenti a ({x}, {y}).")
        except ValueError:
            print("Input non valido. Assicurati di inserire due numeri separati da spazio.")
        
if __name__ == "__main__":
    main()
