numero = int(input("Inserisci un numero e ti dirò i suoi divisori: "))

print(f"I divisori di {numero} sono:")
i= 1

while i <= numero:
    if numero % i == 0:
        print (i)
    i=i+1