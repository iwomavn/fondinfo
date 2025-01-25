import g2d

def main():
    larghezza_canvas, altezza_canvas = 500, 500
    margine = 10
    g2d.init_canvas((larghezza_canvas, altezza_canvas))
    
    n = int(g2d.prompt("Inserisci il numero di quadrati da disegnare:"))
    lato_min = (larghezza_canvas - 2 * margine) / n

    for i in range(n):
        lato_corrente = (larghezza_canvas - 2 * margine) - (i * lato_min)
        
        verde = int(255 * (i + 1) / n)
        colore = (0, verde, 0)

        g2d.set_color(colore)
        
        x = larghezza_canvas - margine - lato_corrente
        y = margine
        
        g2d.draw_rect((int(x), int(y)), (int(lato_corrente), int(lato_corrente)))

    g2d.main_loop()

if __name__ == "__main__":
    main()
