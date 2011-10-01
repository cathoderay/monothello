import unittest

import minimax
from game import Board


class TestWeak(unittest.TestCase):
    def test_configuration1(self):
        minimax.PLAYER = "W"
        board = Board()
        board[(1, 0)] = "W"
        board[(1, 1)] = "W"
        board[(1, 2)] = "W"        
        board[(1, 3)] = "W"
        board[(1, 4)] = "W"        
        board[(1, 5)] = "W"
        board[(2, 4)] = "B"
        self.assertEqual(minimax.weak(board, minimax.PLAYER), 6-1)

    def test_configuration2(self):
        minimax.PLAYER = "B"
        board = Board()
        board[(1, 0)] = "W"
        board[(1, 1)] = "W"
        board[(1, 2)] = "W"        
        board[(1, 3)] = "W"
        board[(1, 4)] = "W"        
        board[(1, 5)] = "W"
        board[(2, 4)] = "B"
        self.assertEqual(minimax.weak(board, minimax.PLAYER), 1-6)     


class TestPosicional(unittest.TestCase):
    def test_configuration1(self):
        minimax.PLAYER = "W"
        board = Board()
        board[(0, 0)] = "W" #value = 20
        board[(3, 4)] = "B"
        board[(1, 1)] = "W" #value = 0
        board[(7, 7)] = "W" #value = 20
        board[(4, 3)] = "W" #value = 5
        self.assertEqual(minimax.posicional(board, minimax.PLAYER), 45)
    
    def test_configuration2(self):
        minimax.PLAYER = "B"
        board = Board()
        board[(0, 0)] = "B" #value = 20
        board[(3, 4)] = "W"
        board[(1, 1)] = "B" #value = 0
        board[(7, 7)] = "B" #value = 20
        board[(4, 3)] = "B" #value = 5
        self.assertEqual(minimax.posicional(board, minimax.PLAYER), 45)
        
    def test_configuration3(self):
        minimax.PLAYER = "W"
        board = Board()
        board[(5, 4)] = "W" #value = 10
        board[(6, 4)] = "W" #value = 10
        board[(2, 4)] = "W" #value = 10
        board[(1, 4)] = "W" #value = 10
        self.assertEqual(minimax.posicional(board, minimax.PLAYER), 40)


if __name__ == "__main__":
    unittest.main()
