from unittest import TestCase, main  # Importa le classi `TestCase` e `main` dal modulo `unittest`
from somma_ricorsiva_di_cifre import sum_digits  # Importa la funzione `sum_digits` dal file `somma_ricorsiva_di_cifre.py`

class DigitsTest(TestCase):  # Definisce una classe di test che eredita da `unittest.TestCase`
    def test_sum(self):  # Metodo per testare la funzione `sum_digits`
        params = [(4, 4), (45, 9), (86, 5), (686, 2), (9686, 2), (97689, 3)]  # Una lista di tuple (input, expected_output) per testare la funzione
        for x, y in params:  # Itera su ogni coppia (input, expected_output)
            with self.subTest(param=x):  # Crea un sotto-test per ogni caso
                self.assertEqual(sum_digits(x), y) # Verifica che la funzione `sum_digits(x)` restituisca `y`

if __name__ == "__main__": 
    main() 