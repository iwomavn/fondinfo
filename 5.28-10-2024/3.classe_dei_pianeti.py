from c04_polar import move_around
from random import randrange

ARENA_W, ARENA_H = 480, 360

class Planet:
    def __init__(self, center, distance, angv):
        self._center = center
        self._distance = distance
        self._angle = randrange(360)
        self._angv = angv
        self._color = (randrange(256), randrange(256), randrange(256))

    def move(self):
        self._angle += self._angv

    def pos(self):
        return move_around(self._center, self._distance, self._angle)
        return self._x, self._y
    
    def color(self):
        return self._color
    
def tick():
    g2d.clear_canvas()
    for p in planets:
        g2d.set_color(p.color())
        g2d.draw_circle(p.pos(), 10)
        p.move()

def main():
    global planets, g2d
    import g2d  # Ball does not depend on g2d
    center = (ARENA_W / 2, ARENA_H / 2)
    planets = [Planet(center, 100, 2),
               Planet(center, 130, 1.5),
               Planet(center, 160, 1)]

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
