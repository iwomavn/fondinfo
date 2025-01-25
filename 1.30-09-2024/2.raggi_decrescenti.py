import g2d

g2d.init_canvas((500, 500))
center = (250, 250)

r1 = int(g2d.prompt("Valore primo raggio?"))
r2 = int(g2d.prompt("Valore secondo raggio?"))
r3 = int(g2d.prompt("Valore terzo raggio?"))

if r1 > r2 and r2 > r3: # se sono decrescenti
    g2d.set_color((255, 0, 255))
    g2d.draw_circle(center, r1)
    g2d.set_color((255, 255, 0))
    g2d.draw_circle(center, r2)
    g2d.set_color((0, 255, 255))
    g2d.draw_circle(center, r3)
    g2d.main_loop()
else:
    print("Errore!")