import g2d
import math

def draw_stars(center: tuple[float, float], r: float, n: int):
    g2d.set_color((255, 255, 255))
    g2d.draw_circle(center, 3)
    
    if r <= 5:
        return

def main():
    size = 600, 600
    g2d.init_canvas(size)
    
    draw_stars((300, 300), 200, 5)
     
    g2d.main_loop()

if __name__ == "__main__":
    main()
