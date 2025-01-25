import g2d

def draw_squares(x, y, s):
    if s <= 16: 
        half_s = s / 2

        g2d.set_color((255, 0, 0))  
        g2d.draw_rect((x - half_s, y), (half_s, half_s))
        g2d.set_color((0, 255, 0)) 
        g2d.draw_rect((x, y), (half_s, half_s))
        g2d.set_color((0, 0, 255)) 
        g2d.draw_rect((x - half_s / 2, y - half_s), (half_s, half_s))

    else: 
        half_s = s / 2
        draw_squares(x - half_s / 2, y, half_s)  
        draw_squares(x + half_s / 2, y, half_s) 
        draw_squares(x, y - half_s / 2, half_s) 

def main():
    g2d.init_canvas((640, 480))  

    def tick():
        g2d.clear_canvas()
        draw_squares(320, 240, 128) 
        g2d.update_canvas()

    g2d.main_loop(tick)

if __name__ == "__main__":
    main()