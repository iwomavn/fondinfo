try:
    from __main__ import g2d
except:
    import g2d
from boardgame import BoardGame
from hitori import Hitori  

W, H = 40, 40

class BoardGameGui:
    def __init__(self, game: BoardGame, level_file: str, level_files: list):
        self._game = game
        self._level_file = level_file
        self._level_files = level_files
        self.update_buttons()

    def tick(self):
        game = self._game
        x, y = g2d.mouse_pos()
        bx, by = x // W, y // H
        released = set(g2d.previous_keys()) - set(g2d.current_keys())

        if game.finished():
            g2d.alert("Congrats! You won! :)") 
            self.load_next_level() 
            return  # finisce gioco
        elif "Escape" in released:  
            g2d.close_canvas()
        elif "LeftButton" in released and by < game.rows():
            game.play(bx, by, "")
            self.update_buttons()
        elif "RightButton" in released and by < game.rows():
            game.play(bx, by, "flag")
            self.handle_right_click(bx, by)
            self.update_buttons()
        elif "h" in released:  # automatismi 
            self.apply_automatism(bx, by)
            self.update_buttons()

    def handle_right_click(self, bx, by):
        cell_content = self._game.read(bx, by)
        if cell_content.endswith("#"):  # la cella è nera
            self.circle_numbers(bx, by)
        elif cell_content.endswith("!"):  # la cella è cerchiata
            self.black_same_number_cells(bx, by)

    def circle_numbers(self, bx, by):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # sopra, sotto, sinistra, destra
            nx, ny = bx + dx, by + dy
            if 0 <= nx < self._game.cols() and 0 <= ny < self._game.rows():
                self._game.play(nx, ny, "circle")  
                
    def black_same_number_cells(self, bx, by):
        number = self._game.read(bx, by).strip("!") 
    
        for x in range(self._game.cols()): # riga
            if self._game.read(x, by).strip("!") == number:
                self._game.play(x, by, "black")
    
        for y in range(self._game.rows()): # colonna
            if self._game.read(bx, y).strip("!") == number:
                self._game.play(bx, y, "black")
                
    def apply_automatism(self):
        for y in range(self._game.rows()):
            for x in range(self._game.cols()):
                cell_content = self._game.read(x, y)
                if cell_content.endswith("#"):  # cella nera
                    self.circle_numbers(x, y)
                elif cell_content.endswith("!"):  # cella cerchiata
                    self.black_same_number_cells(x, y)

    def update_buttons(self):
        cols, rows = self._game.cols(), self._game.rows()
        g2d.clear_canvas()  
        wrong_cells = self._game.get_wrong_cells()

        for y in range(rows):
            for x in range(cols):
                cell_content = self._game.read(x, y)
                num = cell_content[:-1] if cell_content[-1] in "#!" else cell_content
                state = cell_content[-1] if cell_content[-1] in "#!" else ""

                cell_x, cell_y = x * W,  y * H 
                cell_w, cell_h= W * 2, H 
                
                if state == "#": # nero
                    g2d.set_color((0, 0, 0))  
                    g2d.draw_rect((cell_x, cell_y), (cell_w, cell_h))
                elif state == "!": # cerchiato
                    g2d.set_color((255, 255, 255)) 
                    g2d.draw_rect((cell_x, cell_y), (cell_w, cell_h))
                    g2d.set_color((0, 0, 0)) 
                    g2d.draw_circle((x * W + W // 2, y * H + H // 2), W // 2.1)
                    g2d.set_color((255, 255, 255))  
                    g2d.draw_circle((x * W + W // 2, y * H + H // 2), W // 2.3)
                    g2d.set_color((0, 0, 0)) 
                    g2d.draw_text(num, (x * W + W // 2, y * H + H // 2), W // 2)
                
                else: # cella bianca
                    g2d.set_color((255, 255, 255)) 
                    g2d.draw_rect((cell_x, cell_y), (cell_w, cell_h))
                    g2d.set_color((0, 0, 0))  
                    g2d.draw_text(num, (x * W + W // 2, y * H + H // 2), W // 2)

                if (x, y) in wrong_cells: # rosso per celle sbagliate
                    g2d.set_color((255, 0, 0))  
                    g2d.draw_rect((cell_x, cell_y), (cell_w, cell_h))
                    g2d.set_color((255, 255, 255))  
                    g2d.draw_text(num, (x * W + W // 2, y * H + H // 2), W // 2)

        g2d.set_color((0, 0, 0)) 
        for y in range(1, rows + 1):
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((x * W, 0), (x * W, rows * H))
            
        status = self._game.status()
        if status == "Wrong!":
            g2d.set_color((255, 0, 0))
        g2d.draw_text(status, (cols * W // 2, rows * H + H // 2), W // 2)

    def load_next_level(self):
        level_index = self._level_files.index(self._level_file)
        
        if level_index >= len(self._level_files) - 1:
            g2d.alert("Bravo! You finished all the levels! ;)")
            g2d.close_canvas()
            return
        
        next_level_file = self._level_files[level_index + 1]
        game = Hitori(next_level_file)
        gui_play(game, next_level_file, self._level_files)  

def _write(text, x, y, w, h):
    fsize = 0.75 * min(h, 2 * w / len(text or " "))
    g2d.draw_text(text, (x + w // 2, y + h // 2), fsize)

def gui_play(game: BoardGame, level_file: str, level_files: list):
    g2d.init_canvas((game.cols() * W, game.rows() * H + H))
    ui = BoardGameGui(game, level_file, level_files)
    g2d.main_loop(ui.tick)