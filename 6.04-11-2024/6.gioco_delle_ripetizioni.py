from boardgame import BoardGame

def has_repetitions(data: list[int]) -> bool:
    seen = set()
    for val in data:
        if val in seen:
            return True
        seen.add(val)
    return False

class RepetitionGame(BoardGame):
    def __init__(self, w, h):
        self._w, self._h = w, h
        self._n = max(w, h) + 1
        self._bd = [0] * (w * h)

    def read(self, x, y):
        if 0 <= x < self._w and 0 <= y < self._h and self._bd[x + y * self._w]:
            return str(self._bd[x + y * self._w])
        return ""
            
    def play(self, x, y, action=""):
        if 0 <= x < self._w and 0 <= y < self._h:
            self._bd[x + y * self._w] += 1
            self._bd[x + y * self._w] %= self._n
            
    def finished(self):
        for y in range(self._h):
            row = [self._bd[x + y * self._w] for x in range(self._w)]
            if has_repetitions(row):
                return False
        for x in range(self._w):
            col = [self._bd[x + y * self._w] for y in range(self._h)]
            if has_repetitions(col):
                return False
        return all(self._bd)

    def status(self):
        return "Finished" if self.finished() else "Playing" 

    def rows(self):
        return self._h
        
    def cols(self):
        return self._w
    
if __name__ == "__main__":
    from boardgamegui import gui_play
    gui_play(RepetitionGame(3, 3))