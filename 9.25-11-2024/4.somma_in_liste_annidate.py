from typing import List
T = float

def sum_nested(data) -> float:  
    if isinstance(data, (int, float)):  # caso base: è un numero
        return data
    elif isinstance(data, list):  # caso ricorsivo: è una lista
        return sum(sum_nested(item) for item in data)
    else:
        raise ValueError("Il dato deve essere un numero o una lista annidata.")

example1 = [[1, 2, [3, 4], [5]], 6]
example2 = [1, [3, [8, 9], 7, 2], [], [4], 5]

print(sum_nested(example1))  
print(sum_nested(example2))  