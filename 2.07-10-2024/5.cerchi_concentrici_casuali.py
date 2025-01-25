import g2d
from random import randrange

g2d.init_canvas((500, 500))
center = (250, 250)

raggio = 200

while raggio >= 10:
    r, g, b = randrange(256), randrange(256), randrange(256)
    g2d.set_color((r, g, b))
    
    g2d.draw_circle(center, raggio)
    
    if raggio > 10:
        raggio = randrange(10, raggio)
    else:
        break

g2d.main_loop()
