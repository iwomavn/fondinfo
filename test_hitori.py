import unittest
from hitori import Hitori

class TestHitoriGame(unittest.TestCase):

    def setUp(self):
        self.game = Hitori("../uni_python/hitori/hitori-tables/5-easy.csv") 

    def test_play_action(self):
        self.game.play(1, 1, "circle")
        self.assertEqual(self.game.read(1, 1), '1!') 

    def test_no_duplicate_in_row(self):
        self.assertTrue(self.game.check_row(0)) 

    def test_no_duplicate_in_col(self):
        self.assertTrue(self.game.check_col(0))  

    def test_no_adjacent_black_cells_in_row(self):  
        self.assertTrue(self.game.check_black_row(0))

    def test_no_adjacent_black_cells_in_col(self):
        self.assertTrue(self.game.check_black_col(0)) 

    def test_check_white_cells_connected(self):
        self.assertTrue(self.game.check_white())

    def test_wrong_cells(self):  
        self.game.play(0, 0, "black")
        self.game.play(1, 0, "black")
        self.assertTrue(self.game.wrong())  

    def test_finished(self):
        self.assertFalse(self.game.finished())  

        self.game.play(0, 0, "black")
        self.game.play(1, 0, "black")
        self.assertTrue(self.game.finished())  

    def test_game_status(self):
        self.assertEqual(self.game.status(), "Playing") 

        self.game.play(0, 0, "black")
        self.game.play(1, 0, "black")
        self.assertEqual(self.game.status(), "Wrong!")  

if __name__ == '__main__':
    unittest.main()
