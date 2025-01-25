from typing import List, Union

T = Union[float, List["T"]]  

def out_of_range(data: T, limit: float) -> bool:
    if isinstance(data, (int, float)):  # numero
        return data > limit
    elif isinstance(data, list):  # lista
        for item in data:
            if out_of_range(item, limit): 
                return True
    return False  

def main():
    data = [1, [3, [8, 9], 7, 2], [], [4], 5]
    limit = 6
    result = out_of_range(data, limit)
    print(f"Esistono valori superiori a {limit}: {result}")

    limit2 = 7
    result2 = out_of_range(data, limit2)
    print(f"Esistono valori superiori a {limit2}: {result2}")

    limit3 = 9
    result3 = out_of_range(data, limit3)
    print(f"Esistono valori superiori a {limit3}: {result3}")

if __name__ == "__main__":
    main()
