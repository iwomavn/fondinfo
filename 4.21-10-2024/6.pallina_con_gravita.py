ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x, self._y = x0, y0
        self._dx, self._dy = -4, 0
        self._gravity = 1

    def move(self):
        if self._y + self._dy > ARENA_H - BALL_H:
            self._dy = -self._dy
        else:
            self._dy += self._gravity
        self._y += self._dy
        self._x = (self._x + self._dx) % ARENA_W

    def pos(self) -> (tuple):
        return self._x, self._y


def tick():
    g2d.clear_canvas()  # BG
    g2d.draw_image("ball.png", b1.pos())  # FG
    g2d.draw_image("ball.png", b2.pos())  # FG
    b1.move()
    b2.move()

def main():
    global b1, b2, g2d
    import g2d  # Ball does not depend on g2d
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
