def digits(n: int) -> list[int]:
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10
    return result

def main():
    while n := input("n? "):
        print(digits(int(n)))

if __name__ == "__main__":
    main()
