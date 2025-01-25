from boardgame import BoardGame

CLEAR, BLACK, CIRCLE = 0, 1, 2  

class Hitori(BoardGame):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file] 
        self._numbers = [int(num) for line in lines for num in line.split(',')] 
        self._h = len(lines)  
        self._w = len(lines[0].split(',')) if lines else 0 
        self._annotations = [CLEAR] * (self._w * self._h)  # inizializza le annotazioni
        self._wrong_cells = []

    def play(self, x, y, action): 
        index = x + y * self._w
        if action == "circle" and self._annotations[index] != BLACK:
            self._annotations[index] = CIRCLE  
        elif action == "black" and self._annotations[index] != CIRCLE:
            self._annotations[index] = BLACK  
        elif action == "":  # click mouse sinistro, CLEAR -> BLACK -> CIRCLE
            self._annotations[index] = (self._annotations[index] + 1) % 3  # ruota gli stati

    def read(self, x, y):
        index = x + y * self._w
        txt = str(self._numbers[index])
        if self._annotations[index] == BLACK:
            txt += "#"
        elif self._annotations[index] == CIRCLE:
            txt += "!"
        return txt

    def finished(self):
        for y in range(self._h):
            if not self.check_row(y) or not self.check_black_row(y): # colonne
                return False
        for x in range(self._w):
            if not self.check_col(x) or not self.check_black_col(x): # righe
                return False
        
        if not self.check_white(): # celle bianche
            return False
        
        return True
    
    def wrong(self):
        self._wrong_cells = []  
        
        for y in range(self._h): # celle nere vicine
            for x in range(self._w - 1):  # orizzontale
                if self._annotations[x + y * self._w] == BLACK and self._annotations[(x + 1) + y * self._w] == BLACK:
                    if (x, y) not in self._wrong_cells:  
                        self._wrong_cells.append((x, y))
                    if (x + 1, y) not in self._wrong_cells:  
                        self._wrong_cells.append((x + 1, y))
                
        for x in range(self._w):
            for y in range(self._h - 1):  # verticale
                if self._annotations[x + y * self._w] == BLACK and self._annotations[x + (y + 1) * self._w] == BLACK:
                    if (x, y) not in self._wrong_cells:  
                        self._wrong_cells.append((x, y))
                    if (x, y + 1) not in self._wrong_cells:
                        self._wrong_cells.append((x, y + 1))

        for y in range(self._h): # numeri cerchiati duplicati orizzontali
            seen = [] 
            for x in range(self._w):
                index = x + y * self._w
                if self._annotations[index] == CIRCLE:
                    value = self._numbers[index]
                    if value in seen:
                        if (x, y) not in self._wrong_cells: 
                            self._wrong_cells.append((x, y))
                        if (seen.index(value), y) not in self._wrong_cells: 
                            self._wrong_cells.append((seen.index(value), y))
                    seen.append(value)
                    
        for x in range(self._w): # numeri cerchiati duplicati verticali
            seen = [] 
            for y in range(self._h):
                index = x + y * self._w
                if self._annotations[index] == CIRCLE:
                    value = self._numbers[index]
                    if value in seen: 
                        if (x, y) not in self._wrong_cells: 
                            self._wrong_cells.append((x, y))
                        if (x, seen.index(value)) not in self._wrong_cells:  
                            self._wrong_cells.append((x, seen.index(value)))
                    seen.append(value)

        # Debug: Verifica cosa è stato aggiunto
        print(f"Wrong cells at: {self._wrong_cells}")

        # Se ci sono celle sbagliate, ritorna True
        if not self.check_white(): 
            return True

        return len(self._wrong_cells) > 0  # Se ci sono errori, ritorna True

    def check_white(self): # verifica che le celle bianche siano connesse
        visited = [] # per tracciare le celle visitate
        for _ in range(self._h):
            visited.append([False] * self._w)

        start = None
        for y in range(self._h):
            for x in range(self._w):
                if self._annotations[x + y * self._w] != BLACK:
                    start = (x, y)
                    break  
            if start:
                break  
            
        if not start:
            return False # nessuna cella bianca trovata

        def mark(x, y):
            if x < 0 or x >= self._w or y < 0 or y >= self._h:
                return
            if self._annotations[x + y * self._w] == BLACK or visited[y][x]:
                return
            visited[y][x] = True
            mark(x, y - 1)  # sopra
            mark(x + 1, y)  # destra
            mark(x, y + 1)  # sotto
            mark(x - 1, y)  # sinistra

        mark(start[0], start[1])

        for y in range(self._h):
            for x in range(self._w):
                if self._annotations[x + y * self._w] != BLACK and not visited[y][x]:
                    return False  # cella bianca non connessa
        return True

    def check_row(self, y):  # controlla che i valori non neri non si ripetano in una riga
        visited = [] 
        for x in range(self._w):
            index = x + y * self._w
            if self._annotations[index] != BLACK:  
                value = self._numbers[index]
                if value in visited:  
                    return False
                visited.append(value)  
        return True
    
    def check_col(self, x):  # controlla che i valori non neri non si ripetano in una colonna
        visited = [] 
        for y in range(self._h):
            index = x + y * self._w
            if self._annotations[index] != BLACK:  
                value = self._numbers[index]
                if value in visited: 
                    return False
                visited.append(value) 
        return True

    def check_black_row(self, y): # controlla che non ci siano celle nere vicine in una riga
        for x in range(self._w - 1): 
            if (self._annotations[x + y * self._w] == BLACK and self._annotations[(x + 1) + y * self._w] == BLACK):
                return False
        return True

    def check_black_col(self, x): # controlla che non ci siano celle nere vicine in una colonna
        for y in range(self._h - 1):  
            if (self._annotations[x + y * self._w] == BLACK and self._annotations[x + (y + 1) * self._w] == BLACK):
                return False
        return True

    def status(self): 
        if self.wrong():
            return "Wrong!"
        return "Playing"

    def cols(self): 
        return self._w

    def rows(self):
        return self._h

    def get_wrong_cells(self):
        return self._wrong_cells
