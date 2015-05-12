import unittest
from collatz_conj import find_collatz_cycle_len


class TestCollatzConj(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_collatz_cycle_len(self):
        self.assertEqual(8, find_collatz_cycle_len(20))
        
if __name__ == '__main__':
    unittest.main()

