def out_of_range(data: list[float], limit: float) -> bool:
    if not data:
        return False
    if data[0] > limit:
        return True
    return out_of_range(data[1:], limit)

if __name__ == "__main__":
    print(out_of_range([2, 3, 6, 18], 10))
