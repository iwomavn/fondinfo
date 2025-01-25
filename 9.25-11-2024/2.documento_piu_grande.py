from math import inf  # importa il valore "infinito" dalla libreria math, che sarà usato per confronti di grandezza

class Node: # definizione della classe astratta Node
    def size(self) -> int:  
        raise NotImplementedError("Abstract method")

    def largest(self) -> tuple[int, str]:  
        raise NotImplementedError("Abstract method")
    
    def print(self, indent: int):  
        raise NotImplementedError("Abstract method")

class Document(Node): 
    def __init__(self, name: str, text: str):  # Costruttore che prende il nome e il testo del documento
        self._name = name  # Nome del documento
        self._text = text  # Testo contenuto nel documento

    def size(self) -> int:  # Restituisce la lunghezza del testo come dimensione del documento
        return len(self._text)
    
    def largest(self):  # Restituisce la dimensione del documento e il suo nome come una tupla
        return self.size(), self._name

    def print(self, indent: int):  # Stampa il nome del documento con un'indentazione specificata
        print(" " * indent + self._name)

class Folder(Node): # Definizione della classe Folder che estende la classe astratta Node
    def __init__(self, name: str, subnodes: list[Node]):  # Costruttore che prende il nome della cartella e una lista di nodi (Document o Folder)
        self._name = name  # Nome della cartella
        self._subnodes = subnodes  # Sottocartelle o documenti contenuti nella cartella

    def size(self) -> int: # Calcola la dimensione totale della cartella sommando le dimensioni di tutti i nodi figli
        total_size = 0
        for n in self._subnodes:  # Itera attraverso tutti i sottoggetti della cartella
            total_size += n.size()  # Aggiunge la dimensione di ogni sottoggetto
        return total_size

    def largest(self):  # Trova il nodo più grande fra i sottoggetti della cartella
        result = (-inf, "")  # Inizializza il risultato con una dimensione molto piccola
        size, path = max((n.largest() for n in self._subnodes), default=result)  # Usa max per trovare il nodo con la dimensione massima fra tutti i sottoggetti
        return size, self._name + "/" + path  # Restituisce la dimensione massima e il percorso relativo del nodo

    def print(self, indent: int):  # Stampa il nome della cartella con l'indentazione specificata
        print(" " * indent + self._name)
        for n in self._subnodes:  # Per ogni nodo sottostante, chiama il metodo print ricorsivamente con un'indentazione maggiore
            n.print(indent + 4)

def main():
    prod = Document("prod.csv", "1,2,3,4")  # Creazione di oggetti Document con nome e testo
    data = Folder("data", [prod]) # Creazione di una cartella "data" contenente il documento "prod.csv"
    a1_0 = Document("a1.txt", "bla bla 0") # Creazione di un documento "a1.txt" con del testo
    work = Folder("Work", [a1_0, data])  # Creazione di una cartella "Work" contenente "a1.txt" e la cartella "data"
    a1_1 = Document("a1.txt", "a different file")   # Creazione di un altro documento "a1.txt" con testo diverso
    personal = Folder("Personal", [a1_1])   # Creazione di una cartella "Personal" contenente il secondo documento "a1.txt"
    desktop = Folder("Desktop", [work, personal]) # Creazione di una cartella principale "Desktop" che contiene le cartelle "Work" e "Personal"

    print(desktop.size())  # Stampa la dimensione totale della cartella "desktop" (somma delle dimensioni dei nodi figli)
    print(desktop.largest()) # Stampa il nodo più grande in "desktop" (percorso e dimensione del nodo più grande)
    print()
    desktop.print(0)   # Stampa l'intera struttura di cartelle e documenti con l'indentazione appropriata

if __name__ == "__main__":
    main()