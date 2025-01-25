from random import choice
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self):
        self._x = ARENA_W // 2
        self._y = ARENA_H // 2
        self._dx = choice((-4, 4))
        self._dy = choice((-4, 4))

    def move(self):
        self._x = (self._x + self._dx) % ARENA_W
        self._y = (self._y + self._dy) % ARENA_H

    def pos(self) -> (tuple):
        return self._x, self._y


def tick():
    g2d.clear_canvas()
    g2d.draw_image("ball.png", b1.pos())
    b1.move()

def main():
    global b1, g2d
    import g2d  # Ball does not depend on g2d
    b1 = Ball()

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
