import g2d

def htree(pos: (tuple), size: (tuple), level: int): # Funzione ricorsiva per disegnare un H-tree
    x, y, w, h = pos + size  # Decomprime posizione (x, y) e dimensioni (w, h) in variabili separate

    if level == 0 or w < 10 or h < 10:  # Esci se il livello è 0 o se le dimensioni sono troppo piccole
        return
    # Calcola i quarti di larghezza e altezza
    w4, h4 = w // 4, h // 4  # 1/4 della larghezza e altezza
    # Calcola le coordinate delle posizioni chiave
    x1, x2, x3 = x + w4, x + 2 * w4, x + 3 * w4  # Tre colonne: 1/4, 2/4, 3/4 lungo la larghezza
    y1, y2, y3 = y + h4, y + 2 * h4, y + 3 * h4  # Tre righe: 1/4, 2/4, 3/4 lungo l'altezza

    # Disegna le linee dell'H attuale
    g2d.draw_line((x1, y1), (x1, y3))  # Linea verticale sinistra dell'H
    g2d.draw_line((x3, y1), (x3, y3))  # Linea verticale destra dell'H
    g2d.draw_line((x1, y2), (x3, y2))  # Linea orizzontale centrale dell'H

    # Richiama ricorsivamente per le quattro regioni più piccole
    for pt in ((x, y), (x2, y), (x, y2), (x2, y2)):  # Quattro sottorettangoli in alto-sinistra, alto-destra, basso-sinistra, basso-destra
        htree(pt, (w // 2, h // 2), level - 1)  # Riduci le dimensioni a metà e il livello di uno

# Funzione principale del programma
def main():
    size = 600, 600  # Dimensione del canvas: 600x600 pixel
    g2d.init_canvas(size)  # Inizializza il canvas grafico con la dimensione specificata
    level = int(g2d.prompt("level? "))  # Prompt per l'input del livello massimo. L'utente digita il valore.
    htree((0, 0), size, level)
    g2d.main_loop()

main()  
