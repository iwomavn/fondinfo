import g2d
from random import randrange

larghezza_canva, altezza_canva = 300, 300
x, y = 150, 150
passi = 0
ultima_pos = (x, y)

def draw_cross(x, y, i):
    c = min(i * (255 // 50), 255) 
    g2d.set_color((c, c, c))    
    g2d.draw_line((x + 3, y), (x - 3, y), 2)  # orizzontale
    g2d.draw_line((x, y + 3), (x, y - 3), 2)  # verticale

def passeggiata(xc, yc, r):
    if r == 0:  
        yc = yc -10
    elif r == 1:  
        xc = xc + 10
    elif r == 2:  
        yc = yc + 10
    else: 
        xc = xc - 10
    
    if xc >= larghezza_canva: #controllo
        xc = 0
    elif xc < 0:
        xc = larghezza_canva - 1

    if yc >= altezza_canva:
        yc = 0
    elif yc < 0:
        yc = altezza_canva - 1
    
    return (xc, yc)

def main():
    global x, y, passi, ultima_pos
    passi = int(g2d.prompt("Numero passi da fare?"))
    g2d.init_canvas((larghezza_canva, altezza_canva))
    
    for i in range(passi):
        while True:
            r = randrange(3)
            nuova_pos = passeggiata(x, y, r) 
            
            if nuova_pos != ultima_pos:  # per non ripetere posizione
                ultima_pos = (x, y) 
                x = nuova_pos[0]
                y = nuova_pos[1]
                break

        draw_cross(x, y, i)  
    
    g2d.main_loop()

if __name__ == "__main__":
    main()
