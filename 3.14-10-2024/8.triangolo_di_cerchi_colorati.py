import g2d
from random import randrange

def draw_circle_triangle(n):
    g2d.init_canvas((500, 500))  # Inizializza la finestra
    radius = 20  # Imposta il raggio dei cerchi
    spacing = 5  # Spazio tra i cerchi

    # Itera su ciascuna riga
    for row in range(1, n + 1):
        # Disegna 'row' cerchi nella riga
        for col in range(row):
            # Calcola la posizione x, y del cerchio
            x = 50 + col * (radius * 2 + spacing)  # Allineamento a sinistra, con uno spazio tra i cerchi
            y = 50 + row * (radius * 2 + spacing)
            
            # Genera un colore casuale
            r, g, b = randrange(256), randrange(256), randrange(256)
            g2d.set_color((r, g, b))
            
            # Disegna il cerchio
            g2d.draw_circle((x, y), radius)
    
    g2d.main_loop()

def main():
    n = int(input("Inserisci il numero di righe di cerchi: "))
    draw_circle_triangle(n)

if __name__ == "__main__":
    main()
