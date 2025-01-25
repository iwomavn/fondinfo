import g2d

def main():
    larghezza_canvas, altezza_canvas = 500, 500
    g2d.init_canvas((larghezza_canvas, altezza_canvas))
    
    n = int(g2d.prompt("Inserisci il numero di quadrati da disegnare:"))
    lato_min = larghezza_canvas / n

    for i in range(n):
        lato_corrente = larghezza_canvas - (i * lato_min)
        
        verde = int(255 * (i + 1) / n)
        colore = (0, verde, 0)  
        
        g2d.set_color(colore)
        g2d.draw_rect((0, 0), (int(lato_corrente), int(lato_corrente)))

    g2d.main_loop()

if __name__ == "__main__":
    main()
