import random, g2d
from actor import *

ARENA_W, ARENA_H, SIZE, MAX_LEVEL = 480, 360, 16, 5

class Ballom(Actor):
    def __init__(self, x0: int, y0: int):
        self._x = (x0 // SIZE) * SIZE
        self._y = (y0 // SIZE) * SIZE
        self._dx, self._dy = self._random_direction()
        self._w, self._h = SIZE, SIZE
        self._is_dead = False 
        self._death_frame = 0  

    def _random_direction(self):  # scelta casuale della direzione iniziale
        directions = [(0, -4), (0, 4), (4, 0), (-4, 0)]
        return random.choice(directions)

    def move(self, arena=None):
        if self._is_dead:
            self._handle_death_animation()
            return

        next_x, next_y = self._x + self._dx, self._y + self._dy  # calcola la posizione successiva
        collided = False
        
        if not 0 <= self._x + self._dx <= ARENA_W - SIZE:  # rimbalza ai bordi dell'arena
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= ARENA_H - SIZE:
            self._dy = -self._dy

        self._x += self._dx  # movimento
        self._y += self._dy

        if self._x % SIZE == 0 and self._y % SIZE == 0:  # cambia direzione solo se allineato alla griglia
            self._dx, self._dy = self._random_direction()
        
        for other in arena.actors():  # controlla se son avvenute collisioni con i muri
            if isinstance(other, (Wall, BrickWall)) and self._check_collision(next_x, next_y, other):
                collided = True
                break

        if collided:  # se collide, inverte la direzione
            self._dx, self._dy = -self._dx, -self._dy
        else:
            self._x, self._y = next_x, next_y  # aggiorna la posizione solo se non c'è collisione

    def _check_collision(self, next_x, next_y, other) -> bool: 
        return (next_x < other.pos()[0] + other.size()[0] and
                next_x + self._w > other.pos()[0] and
                next_y < other.pos()[1] + other.size()[1] and
                next_y + self._h > other.pos()[1])

    def pos(self) -> Point:
        return self._x, self._y
    
    def size(self) -> Point:
        return self._w, self._h

    def sprite(self):
        if self._is_dead:
            return self._get_death_sprite()
        
        sprite_x, sprite_y = 0, 240
        return sprite_x, sprite_y, self._w, self._h

    def die(self):
        self._is_dead = True
        self._death_frame = 0 

    def _handle_death_animation(self):
        if self._death_frame < 5:
            self._death_frame += 1
        else:
            arena.kill(self)  

    def _get_death_sprite(self):
        death_sprites = [
            (0, 240),  
            (8, 240), 
            (16, 240),
            (24, 240),
            (32, 240) 
        ]
        sprite_x, sprite_y = death_sprites[self._death_sprite_index]
        return sprite_x, sprite_y, self._w, self._h

class Bomberman(Actor):
    def __init__(self, pos, player_id):
        self._x, self._y = pos
        self._w, self._h = SIZE, SIZE
        self._speed = 2
        self._direction = "down" # direzione di default all'inizio
        self._frame = 0
        self._initial_step = True
        self._desired_direction = None
        self._bomba_pos = None
        self._player_id = player_id  
        self._explosion_range = 1  
        self._max_bombs = 2
        self._current_bombs = 0  
        self._dead = False      
        self._death_frame = 0   

    def move(self, arena: Arena):
        keys = arena.current_keys()
        moved = False
        aligned_to_grid = (self._x % SIZE == 0) and (self._y % SIZE == 0)

        if self._player_id == 1:
            controls = {"up": "ArrowUp", "down": "ArrowDown", "left": "ArrowLeft", "right": "ArrowRight", "bomb": "0"}
        elif self._player_id == 2:
            controls = {"up": "w", "down": "s", "left": "a", "right": "d", "bomb": "q"}

        for other in arena.collisions():
            if isinstance(other, Ballom):
                self.hit(arena)
     
        if self._dead:
            self._death_frame += 1
            if self._death_frame > 70: 
                arena.kill(self)  
            return  # non permette movimenti dopo morte

        if aligned_to_grid:
            self._desired_direction = None
            if controls["up"] in keys:
                self._desired_direction = "up"
            elif controls["down"] in keys:
                self._desired_direction = "down"
            elif controls["left"] in keys:
                self._desired_direction = "left"
            elif controls["right"] in keys:
                self._desired_direction = "right"

            if self._desired_direction:
                next_x, next_y = self._x, self._y
                if self._desired_direction == "up":
                    next_y -= self._speed
                elif self._desired_direction == "down":
                    next_y += self._speed
                elif self._desired_direction == "left":
                    next_x -= self._speed
                elif self._desired_direction == "right":
                    next_x += self._speed

                if not any(isinstance(other, (Wall, BrickWall)) and self._check_collision(next_x, next_y, other) for other in arena.actors()):
                    self._direction = self._desired_direction
                    self._initial_step = True

        next_x, next_y = self._x, self._y
        if self._direction == "up":
            next_y -= self._speed
        elif self._direction == "down":
            next_y += self._speed
        elif self._direction == "left":
            next_x -= self._speed
        elif self._direction == "right":
            next_x += self._speed

        if not any(isinstance(other, (Wall, BrickWall)) and self._check_collision(next_x, next_y, other) for other in arena.actors()):
            self._x, self._y = next_x, next_y
            moved = True

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)
        self._y = min(max(self._y, 0), ah - self._h)

        if moved:
            self._frame = 0 if self._initial_step else 1 if self._frame == 2 else 2
            self._initial_step = False

        if controls["bomb"] in keys:
            self.place_bomb(arena)

    def _check_collision(self, next_x, next_y, other) -> bool:
        return (next_x < other.pos()[0] + other.size()[0] and
                next_x + self._w > other.pos()[0] and
                next_y < other.pos()[1] + other.size()[1] and
                next_y + self._h > other.pos()[1])

    def place_bomb(self, arena: Arena):
        bomb_count = 0
        for actor in arena.actors(): 
            if isinstance(actor, Bomb):
                bomb_count += 1
        
        if bomb_count < self._max_bombs: 
            bomb = Bomb(self._x, self._y, self)
            arena.spawn(bomb)

    def sprite(self) -> Point:
        if not self._dead:
            offsets = {
                "down": [(64, 0), (48, 0), (80, 0)],  
                "up": [(64, 16), (48, 16), (80, 16)],
                "left": [(16, 0), (0, 0), (32, 0)],
                "right": [(16, 16), (0, 16), (32, 16)]
            }
            sprite_x, sprite_y = offsets[self._direction][self._frame]
        else:
            death_sprites = [
                (0, 32),  
                (16, 32),  
                (32, 32), 
                (48, 32),  
                (64, 32),  
                (80, 32), 
                (96, 32),  
            ]
            
            sprite_index = min(self._death_frame // 10, len(death_sprites) - 1)
            sprite_x, sprite_y = death_sprites[sprite_index]
            if sprite_index == len(death_sprites)-1:
                arena.set_status(0, "Ballom") 

        return sprite_x, sprite_y, self._w, self._h

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def hit(self, arena: Arena):
        self._dead = True
        self._death_frame = 0
    
    def increase_explosion_range(self, amount: int):
        self._explosion_range += amount
        
    def add_bomb(self):
        self._max_bombs += 1
        
    def get_explosion_range(self) -> int:
        return self._explosion_range

    def get_max_bombs(self) -> int:
        return self._max_bombs

    def get_speed(self) -> int:
        return self._speed
    
    def double_thescore(self) -> int:
        self._score = self._score * 2
        
class Wall(Actor): 
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w, self._h = SIZE, SIZE

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h
    
    def move(self, arena: Arena):
        pass

    def sprite(self) -> Point:
        sprite_x, sprite_y = 48, 48
        return sprite_x, sprite_y, self._w, self._h

class BrickWall(Actor):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w, self._h = SIZE, SIZE
        self._destroyed = False 
        self._destroy_frame = 0 

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def move(self, arena: Arena):
        if self._destroyed:
            self._destroy_frame += 1
            if self._destroy_frame >= 6 * 10: 
                arena.kill(self)

    def destroy(self):
        self._destroyed = True
        self._destroy_frame = 0 

    def sprite(self) -> Point:
        if not self._destroyed:
            sprite_x, sprite_y = 64, 48
        else:
            destruction_sprites = [
                (80, 48),   
                (96, 48), 
                (112, 48),
                (128, 48), 
                (144, 48),
                (160, 48), 
            ]
            sprite_index = min(self._destroy_frame // 10, len(destruction_sprites) - 1)
            sprite_x, sprite_y = destruction_sprites[sprite_index]

        return sprite_x, sprite_y, self._w, self._h

class Bomb(Actor):
    def __init__(self, x: int, y: int, bom: "Bomberman"):
        self._x = (x // SIZE) * SIZE 
        self._y = (y // SIZE) * SIZE
        self._w, self._h = SIZE, SIZE
        self._duration = 100  # durata in frame prima dell'esplosione
        self._bom = bom # bomberman che l'ha piazzata
        self._exploded = False
        self._explosion_frame = 0
        self._range = bom.get_explosion_range()

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def move(self, arena: Arena):
        if not self._exploded:
            self._duration -= 1
            if self._duration <= 0:
                self.explode(arena)

    def explode(self, arena: Arena):
        self._exploded = True
        self._explosion_frame = 0
        if self._range > 1:
            explosion_positions = [
            (self._x, self._y),  # centro
            (self._x - 32, self._y),  # sinistra
            (self._x + 32, self._y),  # destra
            (self._x, self._y - 32),  # sopra
            (self._x, self._y + 32),  # sotto
        ]
        else:
            explosion_positions = [
                (self._x, self._y),  # centro
                (self._x - 16, self._y),  # sinistra
                (self._x + 16, self._y),  # destra
                (self._x, self._y - 16),  # sopra
                (self._x, self._y + 16),  # sotto
            ]
            
        for x, y in explosion_positions:
            for other in arena.actors():
                if isinstance(other, BrickWall) and other.pos() == (x, y):
                    other.destroy()
                    if random.random() < 0.5: # possibilità del 50%
                            boost_type = random.choice(["explosion", "bomb", "speed", "double_score"])
                            arena.spawn(Boost((self._x, self._y), boost_type))
                elif isinstance(other, Bomberman) and other.pos() == (x, y):
                    other.hit(arena)
                elif isinstance(other, Ballom) and other.pos() == (x, y):
                    other.die()

                    alive_ballom = arena.there_are_alive_mobs(Ballom)
                    if not alive_ballom:
                        arena.increase_level()
                        spawn_ballom()
        
        self._x, self._y = self._x - 32, self._y - 16 # per sistemare esplosione bomba        

    def sprite(self) -> Point:
        if not self._exploded:
            return 0, 48, self._w, self._h  # bomba prima dell'esplosione
        else:
            explosion_sprites = [
                (0, 80), 
                (80, 80), 
                (0, 160), 
                (80, 160), ]
            sprite_x, sprite_y = explosion_sprites[self._explosion_frame]
            self._explosion_frame += 1
            if self._explosion_frame >= len(explosion_sprites):
                arena.kill(self)
            return sprite_x, sprite_y, 80, 80

class Boost(Actor):
    def __init__(self, pos: Point, boost_type: str):
        self._x, self._y = pos
        self._w, self._h = SIZE, SIZE 
        self._boost_type = boost_type

    def move(self, arena: Arena):
        for other in arena.collisions(): # controlla collisioni con i giocatori
            if isinstance(other, Wall or BrickWall):
                arena.kill(self)
            elif isinstance(other, Bomberman):
                arena.kill(self)  
                self.apply_boost(other, arena) # applica il boost al bomberman
                
    def apply_boost(self, player: Bomberman, arena: Arena):
        if self._boost_type == "explosion":
            player.increase_explosion_range(1) 
        elif self._boost_type == "bomb":
             if player._max_bombs < 3:
                player._max_bombs += 1
        elif self._boost_type == "speed":
            player._speed =player._speed + 1
        elif self._boost_type == "double_score":
            arena.set_score(arena.get_score() * 2)

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        sprite_map = {
            "explosion": (16, 224),  
            "bomb": (0, 224),      
            "speed": (48, 224),     
            "double_score": (80, 224) 
        }
        return sprite_map.get(self._boost_type, (112, 224)) + (self._w, self._h)

def spawn_ballom():
    if arena.get_level() <= MAX_LEVEL:
        num_balloms = arena.get_level()  
        balloms_spawned = 0

        while balloms_spawned < num_balloms:
            x = random.randint(0, (ARENA_W // SIZE) - 1) * SIZE
            y = random.randint(0, (ARENA_H // SIZE) - 1) * SIZE

            if not any(actor.pos() == (x, y) for actor in arena.actors()):
                new_ballom = Ballom(x, y)
                arena.spawn(new_ballom)
                balloms_spawned += 1

def tick():
    g2d.clear_canvas()
    g2d.set_color((32, 128, 60))
        
    if arena.get_status()[0]:
        g2d.draw_rect((0, 0), (ARENA_W, ARENA_H))
        for actor in arena.actors():
            x, y, w, h = actor.sprite()
            g2d.draw_image("bomberman/img/sprites.png", actor.pos(), clip_pos=(x, y), clip_size=(w, h))
        arena.tick(g2d.current_keys())
    else: 
        g2d.draw_image("bomberman/img/lose.jpg", (0, 0), (0,0), (ARENA_W, ARENA_H))
        arena.kill_alls()
        
def main():
    global arena, current_score
    arena = Arena((ARENA_W, ARENA_H))
    g2d.init_canvas((ARENA_W, ARENA_H))

    num_players = 0
    while num_players not in (1, 2):
        try:
            num_players = int(g2d.prompt("Quanti giocatori? (1 o 2): "))
        except ValueError:
            g2d.alert("Inserisci un numero valido.")

    bomberman1 = Bomberman((224, 160), 1)
    bomberman2 = None

    if num_players == 2:
        bomberman2 = Bomberman((240, 160), 2) 
        
    ballom1 = Ballom(140, 180)
    ballom2 = Ballom(180, 140)
    
    walls = []

    for x in range(0, ARENA_W, SIZE * 2):   # bordi orizzontali (in alto e in basso)
        walls.append(Wall(x, 0))  # bordi superiori
        walls.append(Wall(x, ARENA_H - SIZE))  # bordi inferiori

    for y in range(0, ARENA_H, SIZE * 2):  # bordi verticali (a sinistra e destra)
        walls.append(Wall(0, y))  # bordi sinistri
        walls.append(Wall(ARENA_W - SIZE, y))  # bordi destri

    all_positions = {(wall.pos()) for wall in walls}
    all_positions.add(ballom1.pos())
    all_positions.add(ballom2.pos())
    all_positions.add(bomberman1.pos())
    
    if bomberman2:
        all_positions.add(bomberman2.pos())  
        
    brick_walls_count = 0
    while brick_walls_count < 150:  # genera muri di mattoni in posizioni casuali
        x = random.randint(0, (ARENA_W // SIZE) - 1) * SIZE
        y = random.randint(0, (ARENA_H // SIZE) - 1) * SIZE

        if (x, y) not in all_positions:  # verifica che la posizione sia libera
            brick_wall = BrickWall(x, y)
            walls.append(brick_wall)
            all_positions.add((x, y))  # segna la posizione come occupata
            brick_walls_count += 1

    for wall in walls:
        arena.spawn(wall)

    arena.spawn(ballom1)
    arena.spawn(ballom2)
    arena.spawn(bomberman1)
    
    if bomberman2:
        arena.spawn(bomberman2)

    g2d.main_loop(tick)

if __name__ == "__main__":
    main()