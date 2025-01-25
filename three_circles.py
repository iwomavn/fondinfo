import g2d
from random import randrange

g2d.init_canvas((500, 500))
center = (250, 250)

r1 = int(g2d.prompt("1st radius"))
r2 = int(g2d.prompt("2nd radius"))
r3 = int(g2d.prompt("3rd radius"))

r = randrange(256)
g = randrange(256)
b = randrange(256)
g2d.set_color((r, g, b))
g2d.draw_circle(center, r1)

r = randrange(256)
g = randrange(256)
b = randrange(256)
g2d.set_color((r, g, b))
g2d.draw_circle(center, r2)

r = randrange(256)
g = randrange(256)
b = randrange(256)
g2d.set_color((r, g, b))
g2d.draw_circle(center, r3)

g2d.main_loop()
