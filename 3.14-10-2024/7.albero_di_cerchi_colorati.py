import g2d
from random import randrange

def draw_circle_tree(n):
    g2d.init_canvas((500, 500))  # Inizializza la finestra
    radius = 20  # Imposta il raggio dei cerchi
    spacing = 5  # Spazio tra i cerchi

    # Dimensione della finestra
    canvas_width = 500
    canvas_height = 500

    # Distanza tra le righe (altezza dei cerchi più lo spazio)
    row_height = radius * 2 + spacing

    # Itera su ciascuna riga
    for row in range(1, n + 1):
        # Calcola la posizione orizzontale iniziale per centrare i cerchi
        total_width_row = row * (radius * 2 + spacing) - spacing
        x_start = (canvas_width - total_width_row) // 2
        y = 50 + row * row_height

        # Disegna 'row' cerchi nella riga
        for col in range(row):
            x = x_start + col * (radius * 2 + spacing)
            
            # Genera un colore casuale
            r, g, b = randrange(256), randrange(256), randrange(256)
            g2d.set_color((r, g, b))
            
            # Disegna il cerchio
            g2d.draw_circle((x, y), radius)

    # Aggiungi l'ultimo cerchio alla base dell'albero
    y = 50 + (n + 1) * row_height
    g2d.set_color((randrange(256), randrange(256), randrange(256)))
    g2d.draw_circle((canvas_width // 2, y), radius)

    g2d.main_loop()

def main():
    n = int(input("Inserisci il numero di righe di cerchi: "))
    draw_circle_tree(n)

if __name__ == "__main__":
    main()
