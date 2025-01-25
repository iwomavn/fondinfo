import g2d
from random import randrange

g2d.init_canvas((500, 500))
center = (250, 250)

r1 = int(g2d.prompt("Valore primo raggio?"))
r2 = int(g2d.prompt("Valore secondo raggio?"))
r3 = int(g2d.prompt("Valore terzo raggio?"))

raggi = [r1, r2, r3]

for raggio in raggi:
    r, g, b = randrange(256), randrange(256), randrange (256)
    g2d.set_color((r, g, b))
    g2d.draw_circle(center, raggio)

g2d.main_loop()
