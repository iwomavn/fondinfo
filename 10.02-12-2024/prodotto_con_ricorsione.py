from random import randint

def multiply_all(data: list[int]) -> int:
    if not data:  
        return 1
    return data[0] * multiply_all(data[1:]) 

def main():
    values = [randint(1, 10) for _ in range(randint(3, 6))]
    result = multiply_all(values)
    
    print("Lista generata:", values)
    print("Prodotto di tutti i numeri:", result)

if __name__ == "__main__":
    main()
