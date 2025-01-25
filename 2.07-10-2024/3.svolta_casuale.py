import random

ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20  # Canvas 400x400

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 2, 0  # Inizialmente verso destra (dx=2, dy=0)

    def move(self):
        # Cambio di direzione casuale se x e y sono multipli di 8
        if self._x % 8 == 0 and self._y % 8 == 0:
            self.change_direction()

        # Movimento della pallina
        self._x += self._dx
        self._y += self._dy

        # Controllo dei bordi, no rimbalzi
        if not 0 <= self._x <= ARENA_W - BALL_W:
            self._x = max(0, min(self._x, ARENA_W - BALL_W))
        if not 0 <= self._y <= ARENA_H - BALL_H:
            self._y = max(0, min(self._y, ARENA_H - BALL_H))

    def change_direction(self):
        # Direzioni possibili: alto, basso, sinistra, destra
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]  # Destra, Sinistra, Basso, Alto
        # Escludi la direzione opposta (inverti dx e dy)
        opposite_direction = (-self._dx, -self._dy)
        directions.remove(opposite_direction)

        # Scelta casuale di una nuova direzione
        self._dx, self._dy = random.choice(directions)

    def pos(self) -> (tuple):
        return self._x, self._y


def tick():
    g2d.clear_canvas()  # Pulisci la canvas
    g2d.set_color((255, 0, 0))  # Colore rosso per la pallina
    g2d.draw_circle((b1.pos()), BALL_W // 2)  # Disegna la pallina
    b1.move()  # Muovi la pallina

def main():
    global b1, g2d
    import g2d  # Ball non dipende da g2d
    b1 = Ball(200, 200)  # Posizione iniziale al centro della canvas

    g2d.init_canvas((ARENA_W, ARENA_H))  # Inizializza la canvas
    g2d.main_loop(tick)  # Avvia il ciclo principale

if __name__ == "__main__":
    main()
