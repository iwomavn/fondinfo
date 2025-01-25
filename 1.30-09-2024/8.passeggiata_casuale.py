from random import randrange

n = int(input("Scegli un numero (minore di 50): "))

while n >= 50 :
    n = int(input("Il numero deve essere minore di 50! Scegli un numero: "))

x, y = 0, 0

for i in range(n):
    r = randrange(3)
    if r == 0:
        y = y - 10  
    elif r == 1:
        x = x + 10 
    elif r == 2:
        y = y + 10
    elif r == 3:
        x = x - 10 

distanza = abs(x) + abs(y)
print (f"Le coordinate finali sono: {x}, {y}")
print(f"La distanza di Manhattan dall'origine e': {distanza}")
