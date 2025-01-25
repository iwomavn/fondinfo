from datetime import date

class Persona:
    def __init__(self, nome: str, anno_nascita: int, mese_nascita: int, giorno_nascita: int):
        self.__nome = nome
        self.__data_nascita = date(anno_nascita, mese_nascita, giorno_nascita)

    def is_maggiorenne(self, anno: int, mese: int, giorno: int) -> bool:
        data_verifica = date(anno, mese, giorno)
        eta = (data_verifica - self.__data_nascita).days // 365
        if eta > 18:
            return True
        elif eta < 18:
            return False
        else:
            return (mese, giorno) >= (self.__data_nascita.month, self.__data_nascita.day)

if __name__ == "__main__":
    nome = input("Inserisci il nome della persona: ")
    anno_nascita = int(input("Inserisci l'anno di nascita: "))
    mese_nascita = int(input("Inserisci il mese di nascita: "))
    giorno_nascita = int(input("Inserisci il giorno di nascita: "))

    persona = Persona(nome, anno_nascita, mese_nascita, giorno_nascita)

    print("\nInserisci una serie di date per verificare la maggiore età della persona.")
    print("Digita 'fine' per terminare.")
    
    while True:
        data_input = input("Inserisci una data (formato AAAA-MM-GG): ")
        if data_input.lower() == "fine":
            break

        try:
            anno, mese, giorno = map(int, data_input.split("-"))
            if persona.is_maggiorenne(anno, mese, giorno):
                print(f"{persona._Persona__nome} è maggiorenne alla data {data_input}.")
            else:
                print(f"{persona._Persona__nome} NON è maggiorenne alla data {data_input}.")
        except ValueError:
            print("Formato della data non valido. Riprova.")
