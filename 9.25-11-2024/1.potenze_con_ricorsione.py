def power_recursive(x: float, n: int) -> float:
    if n == 0:  # qualsiasi numero alla potenza 0 è 1
        return 1
    elif n > 0:  # caso ricorsivo per n positivo
        return x * power_recursive(x, n - 1)

if __name__ == "__main__":
    x = float(input("Inserisci la base (x): "))
    n = int(input("Inserisci l'esponente (n): "))
    
    risultato = power_recursive(x, n)
    print(f"{x} elevato alla potenza di {n} è: {risultato}")
