def main():
    print("Inserisci una sequenza di numeri terminata da 0:")
    numbers = []  # Lista per memorizzare i numeri
    while True:
        num = float(input("Inserisci un numero: "))
        if num == 0:
            break
        numbers.append(num)
    
    if len(numbers) == 0:
        print("Nessun numero inserito.")
        return

    # Calcola minimo e massimo
    vmin = min(numbers)
    vmax = max(numbers)
    print(f"Valore minimo: {vmin}, valore massimo: {vmax}")

    # Calcola e mostra i valori normalizzati
    print("Valori normalizzati:")
    for v in numbers:
        if vmax != vmin:  # Evita divisioni per zero
            vnorm = (v - vmin) / (vmax - vmin)
        else:
            vnorm = 0.0  # Se tutti i numeri sono uguali, la normalizzazione dà 0
        print(f"Valore originale: {v}, Valore normalizzato: {vnorm:.2f}")

if __name__ == "__main__":
    main()
