import g2d

def draw_circle_grid(n):
    g2d.init_canvas((500, 500))  # Inizializza il canvas
    margin = 5  # Margine attorno al bordo
    grid_size = 500 - 2 * margin  # Dimensione dell'area utile
    cell_size = grid_size / n  # Dimensione di ogni cella della griglia
    radius = cell_size / 2 - 1  # Raggio del cerchio (lasciamo un piccolo spazio)

    for row in range(n):
        for col in range(n):
            # Calcola la posizione del centro del cerchio
            x = margin + col * cell_size + cell_size / 2
            y = margin + row * cell_size + cell_size / 2

            # Calcola il colore del cerchio
            red = int(255 * col / (n - 1)) if n > 1 else 0
            green = int(255 * row / (n - 1)) if n > 1 else 0
            blue = 0  # Componente blu è sempre 0

            # Imposta il colore e disegna il cerchio
            g2d.set_color((red, green, blue))
            g2d.draw_circle((x, y), radius)

    g2d.main_loop()

def main():
    n = int(input("Inserisci il numero di cerchi per lato (n): "))
    draw_circle_grid(n)

if __name__ == "__main__":
    main()
