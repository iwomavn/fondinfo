import random, g2d

def draw_special_circle(center, radius, color):
    g2d.set_color(color)
    g2d.draw_circle(center, radius)
    
    if radius > 5:
        random_color = tuple(random.randint(0, 255) for _ in range(3)) # Colore casuale
        
        child_radius1 = radius / 2   # Cerchi tangenti a destra e sinistra
        offset1 = radius / 2
        draw_special_circle((center[0] + offset1, center[1]), child_radius1, random_color)
        draw_special_circle((center[0] - offset1, center[1]), child_radius1, random_color)
        
        child_radius2 = radius / 3         # Cerchi tangenti in alto e in basso
        offset2 = (2 / 3) * radius
        draw_special_circle((center[0], center[1] - offset2), child_radius2, random_color)
        draw_special_circle((center[0], center[1] + offset2), child_radius2, random_color)

def main():
    g2d.init_canvas((640, 480))
    center = (320, 240)  # Centro del canvas
    radius = 100  # Raggio iniziale
    color = (0, 0, 255)  # Colore iniziale (blu)
    
    def tick():
        g2d.clear_canvas()
        draw_special_circle(center, radius, color)
        g2d.update_canvas()
    
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()