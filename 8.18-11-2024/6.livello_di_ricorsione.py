import g2d  
from random import randrange  

def rand_color(): # Funzione che genera un colore casuale come una tupla (R, G, B)
    return tuple(randrange(256) for _ in range(3))  # Genera tre numeri casuali (tra 0 e 255) per i componenti RGB

def circlex4(x, y, r, palette, level): # Funzione ricorsiva per disegnare cerchi in posizioni diverse
    g2d.set_color(palette[level % len(palette)])   # Imposta il colore corrente in base al livello e alla palette
    g2d.draw_circle((x, y), r)  # Disegna un cerchio con centro (x, y) e raggio `r`
    
    if r < 5 or level == 0: # Condizione di uscita dalla ricorsione: se il raggio è troppo piccolo o il livello è 0
        return
    # Richiama ricorsivamente per disegnare 4 cerchi più piccoli:
    circlex4(x + r / 2, y, r / 2, palette, level - 1)  # Cerchio a destra
    circlex4(x - r / 2, y, r / 2, palette, level - 1)  # Cerchio a sinistra
    circlex4(x, y + r * 2 / 3, r / 3, palette, level - 1)  # Cerchio in basso
    circlex4(x, y - r * 2 / 3, r / 3, palette, level - 1)  # Cerchio in alto

def main():
    level = 4  # Profondità massima della ricorsione
    palette = [rand_color() for _ in range(level + 1)]  # Crea una palette di colori casuali, uno per ogni livello
    g2d.init_canvas((400, 400))
    # Avvia la funzione ricorsiva per disegnare i cerchi partendo dal centro
    circlex4(200, 200, 200, palette, level)  # Primo cerchio: centro (200, 200), raggio 200
    g2d.main_loop()

if __name__ == "__main__":
    main() 
