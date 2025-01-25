from random import randint

n = int(input("n? "))

with open("_results.txt", "w") as outfile:
    for _ in range(n):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        print(d1, d2, file=outfile)
