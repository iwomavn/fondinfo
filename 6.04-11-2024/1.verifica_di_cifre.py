from lista_di_cifre import digits

def base_ten(digs: list[int]):
    result = 0
    for i, v in enumerate(digs):
        result += v * 10 ** i
    return result

def main():
    while n := input("n? "):
        ds = digits(int(n))
        print(ds, base_ten(ds))

if __name__ == "__main__":
    main()