from random import randint

results = [0] * 13
with open("_results.txt") as infile:
    for line in infile:
        d1, d2 = (int(v) for v in line.split())
        res = d1 + d2
        print(res)
        results[res] += 1

for i, v in enumerate(results):
    print(i, v)