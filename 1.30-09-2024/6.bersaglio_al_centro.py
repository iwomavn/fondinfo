import g2d
from random import randrange
import time

g2d.init_canvas((500, 500))
x, y = 400, 400
center = (x, y)

while abs(x - 250) > 20 or abs(y - 250) > 20:
    r, g, b = randrange(256), randrange(256), randrange(256)
    
    x, y = randrange(500), randrange(500)
    center = (x, y)
    
    g2d.set_color((r, g, b))
    g2d.draw_circle(center, 20)
    
    g2d.update_canvas() 
    time.sleep(0.1)  

g2d.main_loop()
