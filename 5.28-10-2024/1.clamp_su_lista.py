def clamp(data: list[float], limit: float):
    for i, v in enumerate(data):
        if v > limit:
            data[i] = limit

def main():
    values = [2, 3, 5, 1, 4]
    clamp(values, 3)
    print(values)

main()

