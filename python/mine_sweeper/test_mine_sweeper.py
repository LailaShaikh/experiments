import unittest
from mine_sweeper import Mine,Player


class TestMine(unittest.TestCase):
    def setUp(self):
        self.obj = Mine()
        self.obj.initiate_mine()
        
    def test_create_grid(self):
        self.assertIsInstance(self.obj.create_grid(), list)

    def test_fill_mine(self):
        self.obj.fill_random_mines()

        for g in self.obj.grid:
            if 'f' in g:
                self.assertTrue('Mine is marked')
                return
        self.assertFalse()

    def test_mark(self):
        self.obj.mark('open', (0,0))
        self.assertEquals(self.obj.grid[0][0], 'O')

    def test_is_game_over(self):
        self.assertFalse(self.obj.is_game_over())

    def test_is_mine(self):
        self.assertFalse(self.obj.is_mine((0,0)))


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
       
    def test_open_the_grid(self):
        p1, p2 = self.player.open_the_grid()
        self.assertIsInstance(p1, int)
        self.assertIsInstance(p2, int)

    def test_process_the_grid(self):
        #self.player.initiate_game()
        #self.player.process_the_grid()
        pass

if __name__ == '__main__':
    unittest.main()
