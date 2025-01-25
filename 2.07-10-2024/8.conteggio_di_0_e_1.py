def contaZerieUni(testo: str):
    nZero, nUno, i= 0, 0, 0
    
    while i < len(testo):
        testoBinario = bin(ord(testo[i]))[2:]
        print(testoBinario)
   
        nZero += testoBinario.count('0')
        nUno += testoBinario.count('1')
        i += 1
    return (nZero, nUno)

def main():
    testoInput = input("Inserisci una riga di testo (Premere invio per terminare il programma): ")
    
    while testoInput != "":
        zeri, uni = contaZerieUni(testoInput)
        print(f"Il testo inserito contiene {zeri} zeri e {uni} uni")
        testoInput = input("Inserisci una riga di testo (Premere invio per terminare il programma): ")
    
    print("Programma terminato!")
    
if __name__ == "__main__":
    main()
    