from boardgame import BoardGame
from random import randrange

def has_repetitions(data: list[int]) -> bool:
    seen = set()
    for val in data:
        if val in seen:
            return True
        seen.add(val)
    return False

w, h = [int(v) for v in input("w h? ").split(" ")]
matrix = [randrange(16) for _ in range(w * h)]

for y in range(h):
    for x in range(w):
        print(matrix[x + y * w], end="\t")
    print()

for y in range(h):
    row = [matrix[x + y * w] for x in range(w)]
    if has_repetitions(row):
        print(f"Repetitions in row {y+1}")
for x in range(w):
    col = [matrix[x + y * w] for y in range(h)]
    if has_repetitions(col):
        print(f"Repetitions in col {x+1}")
