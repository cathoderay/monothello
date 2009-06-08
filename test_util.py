import unittest
from game import *
from util import *


class TestCountPieces(unittest.TestCase):
    def test_10_blacks_2_whites(self):
        board = Board()
        board[(0, 1)] = "B"
        board[(0, 2)] = "B"
        board[(0, 3)] = "B"
        board[(0, 4)] = "B"
        board[(0, 5)] = "B"
        board[(0, 6)] = "B"
        board[(1, 0)] = "B"
        board[(1, 1)] = "B"
        board[(1, 2)] = "B"
        board[(1, 3)] = "B"
        board[(6, 6)] = "W"
        board[(7, 7)] = "W"
        self.assertEqual(count_pieces(board, "B"), 10)
        self.assertEqual(count_pieces(board, "W"), 2)

    def test_20_blacks_5_whites(self):
        board = Board()
        board[(0, 1)] = "B"
        board[(0, 2)] = "B"
        board[(0, 3)] = "B"
        board[(0, 4)] = "B"
        board[(0, 5)] = "B"
        board[(0, 6)] = "B"
        board[(1, 0)] = "B"
        board[(1, 1)] = "B"
        board[(1, 2)] = "B"
        board[(1, 3)] = "B"

        board[(2, 1)] = "B"
        board[(2, 2)] = "B"
        board[(2, 3)] = "B"
        board[(2, 4)] = "B"
        board[(2, 5)] = "B"
        board[(2, 6)] = "B"
        board[(3, 0)] = "B"
        board[(3, 1)] = "B"
        board[(3, 2)] = "B"
        board[(3, 3)] = "B"

        board[(6, 0)] = "W"
        board[(6, 1)] = "W"
        board[(6, 2)] = "W"
        board[(6, 3)] = "W"
        board[(6, 4)] = "W"
        self.assertEqual(count_pieces(board, "B"), 20)
        self.assertEqual(count_pieces(board, "W"), 5)



class TestPlayablePositions(unittest.TestCase):
    def test_6_valid_positions(self):
        board = Board()
        board[(2, 2)] = "B"
        board[(3, 2)] = "W"
        board[(2, 3)] = "W"
        board[(3, 3)] = "B"
        board[(2, 4)] = "B"
        board[(4, 4)] = "W"
        turn = "W"
        self.assertEqual(valid_positions(board, turn), 
                         set([(1, 1), (2, 1), (1, 2), (4, 3), (2, 5), (3, 4)]))

    def test_0_valid_positions(self):
        board = Board()
        board[(0, 0)] = "W"
        board[(0, 1)] = "B"
        board[(0, 5)] = "W"
        turn = "B"
        self.assertEqual(valid_positions(board, turn), set([]))
    

class TestValidPosition(unittest.TestCase):
    def test_invalid_position(self):
        board = Board()
        board[(1, 1)] = "W"
        board[(2, 4)] = "W"
        board[(5, 2)] = "B"
        position = (6, 6)
        turn = "W"
        self.assertEqual(is_valid_position(board, position, turn), False)
           
    def test_valid_west(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(0, 1)] = "W"
        position = (0, 2)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)

    def test_valid_east(self):
        board = Board()
        board[(0, 2)] = "B"
        board[(0, 1)] = "W"
        position = (0, 0)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True) 

    def test_valid_east2(self):
        board = Board()
        board[(1, 1)] = "W"
        board[(1, 2)] = "W"
        board[(1, 3)] = "B"
        position = (1, 0)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)

    def test_valid_north(self):
        board = Board()
        board[(3, 2)] = "B"
        board[(4, 2)] = "W"
        position = (5, 2)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True) 

    def test_valid_south(self):
        board = Board()        
        board[(5, 2)] = "B"
        board[(4, 2)] = "W"
        position = (3, 2)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True) 

    def test_valid_northeast(self):
        board = Board()
        board[(3, 7)] = "B"
        board[(4, 6)] = "W"
        position = (5, 5)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True) 

    def test_valid_southwest(self):
        board = Board()
        board[(5, 5)] = "B"
        board[(4, 6)] = "W"
        position = (3, 7)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True) 
    
    def test_valid_northwest(self):
        board = Board()
        board[(3, 5)] = "B"
        board[(4, 6)] = "W"
        position = (5, 7)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)

    def test_valid_southeast(self):
        board = Board()
        board[(5, 7)] = "B"
        board[(4, 6)] = "W"
        position = (3, 5)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)

    def test_up_left_border(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(1, 1)] = "W"
        position = (2, 2)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)

    def test_up_left_border_2_pieces(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(1, 1)] = "W"
        board[(2, 2)] = "W"
        position = (3, 3)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)       

    def test_up_left_border_6_pieces(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(1, 1)] = "W"
        board[(2, 2)] = "W"
        board[(3, 3)] = "W"
        board[(4, 4)] = "W"
        board[(5, 5)] = "W"
        board[(6, 6)] = "W"
        position = (7, 7)
        turn = "B"
        self.assertEqual(is_valid_position(board, position, turn), True)       

    def test_valid_configuration(self):
        board = Board()
        board[(3, 2)] = "W"
        board[(2, 3)] = "B"
        board[(3, 3)] = "B"
        board[(3, 4)] = "W"
        board[(4, 3)] = "B"
        board[(4, 4)] = "B"
        board[(5, 3)] = "B"
        position = (3, 5)
        turn = "W"
        self.assertEqual(is_valid_position(board, position, turn), False)


class TestMove(unittest.TestCase):
    def test_move_west(self):
        board = Board()
        board[(0, 0)] = "B"
        board[(0, 1)] = "W"
        board[(0, 2)] = "W"
        board[(0, 3)] = "W"
        turn = "B"
        move(board, (0, 4), turn)
        self.assertEqual(board[(0, 0)], "B")
        self.assertEqual(board[(0, 1)], "B")
        self.assertEqual(board[(0, 2)], "B")
        self.assertEqual(board[(0, 3)], "B")
        self.assertEqual(board[(0, 4)], "B")

    def test_move_east(self):
        board = Board()
        board[(0, 2)] = "B"
        board[(0, 1)] = "W"
        turn = "B"
        move(board, (0, 0), turn)
        self.assertEqual(board[(0, 1)], "B")        
    
    def test_move_north(self):
        board = Board()
        turn = "B"
        board[(3, 2)] = "B"
        board[(4, 2)] = "W"
        move(board, (5, 2), turn)
        self.assertEqual(board[(4, 2)], "B")
    
    def test_move_south(self):
        board = Board()
        board[(5, 2)] = "B"
        board[(4, 2)] = "W"
        turn = "B"
        move(board, (3, 2), turn)
        self.assertEqual(board[(3, 2)], "B")

    def test_move_northeast(self):
        board = Board()
        board[(3, 7)] = "B"
        board[(4, 6)] = "W"
        turn = "B"
        move(board, (5, 5), turn)
        self.assertEqual(board[(4, 6)], "B")        
    
    def test_move_southwest(self):
        board = Board()       
        board[(5, 5)] = "B"
        board[(4, 6)] = "W"
        turn = "B"
        move(board, (3, 7), turn)
        self.assertEqual(board[(4, 6)], "B")       
    
    def test_move_northwest(self):
        board = Board()
        board[(3, 5)] = "B"
        board[(4, 6)] = "W"
        turn = "B"        
        move(board, (5, 7), turn)       
        self.assertEqual(board[(4, 6)], "B")        

    def test_move_southeast(self):
        board = Board()
        board[(5, 7)] = "B"
        board[(4, 6)] = "W"
        turn = "B"
        move(board, (3, 5), turn)
        self.assertEqual(board[(4, 6)], "B")  

    def test_move_2_matches(self):
        board = Board()
        board[(2, 2)] = "B"
        board[(3, 3)] = "W"
        board[(1, 2)] = "B"
        board[(1, 3)] = "W"
        turn = "W"
        move(board, (1, 1), turn)
        self.assertEqual(board[(3, 3)], "W")  
        self.assertEqual(board[(1, 3)], "W")          
        self.assertEqual(board[(2, 2)], "W")  
        self.assertEqual(board[(1, 2)], "W")

    def test_move_3_matches(self):
        board = Board()
        board[(2, 2)] = "B"
        board[(3, 3)] = "W"
        board[(1, 2)] = "B"
        board[(1, 3)] = "W"
        board[(2, 1)] = "B"
        board[(3, 1)] = "W"
        turn = "W"
        move(board, (1, 1), turn)
        self.assertEqual(board[(2, 1)], "W")
        self.assertEqual(board[(3, 1)], "W")
        self.assertEqual(board[(3, 3)], "W")
        self.assertEqual(board[(1, 3)], "W")
        self.assertEqual(board[(2, 2)], "W")
        self.assertEqual(board[(1, 2)], "W")


if __name__ == "__main__":
    unittest.main()
