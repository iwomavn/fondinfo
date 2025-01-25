from boardgamegui import gui_play
from hitori import Hitori  

def main():
    level_files = [
        "../uni_python/hitori/hitori-tables/5-easy.csv", "../uni_python/hitori/hitori-tables/6-medium.csv", "../uni_python/hitori/hitori-tables/8-hard.csv", "../uni_python/hitori/hitori-tables/9-veryhard.csv", "../uni_python/hitori/hitori-tables/12-superhard.csv", "../uni_python/hitori/hitori-tables/15-impossible.csv"
    ]
    
    game = Hitori(level_files[0])
    gui_play(game, level_files[0], level_files) 

if __name__ == "__main__":
    main()
