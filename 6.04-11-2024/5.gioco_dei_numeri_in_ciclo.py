def abstract(): # Definisce un metodo astratto. Solleva un'eccezione se chiamato, indicando che deve essere implementato nelle sottoclassi.
    raise NotImplementedError("Abstract method")  
    
class BoardGame: # Classe base astratta per i giochi da tavolo
    # Definisce metodi astratti che le sottoclassi devono implementare
    def play(self, x: int, y: int, action: str): abstract()  # Metodo per eseguire un'azione sul gioco
    def read(self, x: int, y: int) -> str: abstract()       # Metodo per leggere lo stato di una cella del gioco
    def cols(self) -> int: abstract()                      # Metodo per ottenere il numero di colonne
    def rows(self) -> int: abstract()                      # Metodo per ottenere il numero di righe
    def finished(self) -> bool: abstract()                 # Metodo per verificare se il gioco è finito
    def status(self) -> str: abstract()                    # Metodo per ottenere lo stato del gioco (es. "In corso" o "Finito")

def print_game(game: BoardGame): # Funzione per stampare il gioco sulla console
    # Stampa ogni riga della griglia
    for y in range(game.rows()):  # Itera sulle righe
        for x in range(game.cols()):  # Itera sulle colonne
            print(game.read(x, y) or "·", end="\t")  # Stampa il valore della cella o un punto se vuota
        print()  # Va a capo alla fine di ogni riga
    print(game.status())  # Stampa lo stato attuale del gioco (es. "In corso" o "Finito")

def console_play(game: BoardGame): # Funzione per giocare interattivamente tramite console
    print_game(game)  # Mostra il gioco iniziale

    # Ciclo principale del gioco
    while not game.finished():  # Continua finché il gioco non è finito
        x, y, action = input("x y action?\n").split()  # Chiede all'utente coordinate (x, y) e azione
        game.play(int(x), int(y), action)  # Esegue l'azione specificata dall'utente
        print_game(game)  # Mostra lo stato aggiornato del gioco

class NumberGame(BoardGame): # Implementazione concreta della classe `BoardGame`
    def __init__(self, w: int, h: int):
        self.w = w  # Numero di colonne (larghezza)
        self.h = h  # Numero di righe (altezza)
        self.n = max(w, h)  # Numero massimo utilizzabile (basato sulla dimensione massima della griglia)
        # Inizializza la griglia come una matrice di zeri
        self.board = [[0 for _ in range(w)] for _ in range(h)]

    def play(self, x: int, y: int, action: str): # Metodo per eseguire un'azione sul gioco
        if action == "click":  # Se l'azione è "click"
            self.board[y][x] += 1  # Incrementa il valore della cella
            if self.board[y][x] > self.n:  # Se il valore supera il massimo, lo azzera
                self.board[y][x] = 0

    def read(self, x: int, y: int) -> str:     # Metodo per leggere il valore di una cella
        value = self.board[y][x]  # Legge il valore della cella
        return str(value) if value != 0 else ""  # Ritorna il valore come stringa o vuoto se è 0

    def cols(self) -> int:     # Metodo per ottenere il numero di colonne
        return self.w

    def rows(self) -> int:     # Metodo per ottenere il numero di righe
        return self.h

    def finished(self) -> bool:     # Metodo per verificare se il gioco è finito
        return all(cell != 0 for row in self.board for cell in row)  
        # Ritorna True se tutte le celle hanno un valore diverso da 0
        
    def status(self) -> str:     # Metodo per ottenere lo stato del gioco
        return "Finito" if self.finished() else "In corso"   # Ritorna "Finito" se il gioco è completato, altrimenti "In corso"

if __name__ == "__main__":
    game = NumberGame(3, 3)  # Crea un gioco di dimensione 3x3
    console_play(game)  # Avvia il gioco interattivo tramite console
