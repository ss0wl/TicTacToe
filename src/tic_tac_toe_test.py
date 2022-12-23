import unittest

from tic_tac_toe import TicTacToe

class TTT_Test(unittest.TestCase):
    def test_1_init(self):
        with self.assertRaises(ValueError):
            test_object = TicTacToe('E')
    def test_2_init(self):
        test_object = TicTacToe('X')
        self.assertEqual(test_object.player_symbol, 'X')
    
    def test_3_restart(self):
        to = TicTacToe('X')
        flag = True
        to.edit_field('A1')
        to.restart()
        for item in to.field:
            self.assertEqual(item, " ")
        
    def test_4_check_coord(self):
        to = TicTacToe('X')
        self.assertEqual(to.check_coord('C2'), True)
    
    def test_5_str_coord_to_int(self): 
        to = TicTacToe('X')      
        self.assertEqual(to.str_coord_to_int('A1'), 0)
        self.assertEqual(to.str_coord_to_int('C3'), 8)
        self.assertEqual(to.str_coord_to_int('C2'), 5)
        
    def test_6_edit_field(self):
        to = TicTacToe('X')
        to.edit_field('A1')
        res = to.edit_field('A1')
        self.assertEqual(res, False)
    
    def test_7_edit_field(self):
        to = TicTacToe('X')
        to.edit_field('A1')
        res = to.edit_field('B1')
        self.assertEqual(res, True)
        
    def test_8_update_field(self):
        to1 = TicTacToe('X')
        to2 = TicTacToe('O')
        to1.edit_field('A1')
        to2.edit_field('C1')
        to1.update_field(to2.field)
        
        self.assertEqual(to1.field[2], 'O')
    
    def test_9_update_field(self):
        to = TicTacToe('X')
        test_field = ['X', ' ', 'O']
        with self.assertRaises(ValueError):
            to.update_field(test_field)
    
    def test_10_update_field(self):
        to = TicTacToe('X')
        test_field = TicTacToe('O').field
        test_field[0] = 'T'
        with self.assertRaises(TypeError):
            to.update_field(test_field)

            
    def test_11_is_win(self):
        to1 = TicTacToe('X')
        to2 = TicTacToe('O')
        
        to1.edit_field('A1')
        to1.edit_field('B1')
        to1.edit_field('C1')
        
        to2.update_field(to1.field)
        
        self.assertEqual(to2.is_win('O'), False)
        self.assertEqual(to2.is_win('X'), True)
        
    def test_12_is_full(self):
        to1 = TicTacToe('X')
        to2 = TicTacToe('O')
        to1.edit_field('A1')
        to1.edit_field('B1')
        to2.edit_field('C1')
        to2.edit_field('A2')
        to2.edit_field('B2')
        to1.edit_field('C2')
        to1.edit_field('A3')
        to1.edit_field('B3')
        to2.edit_field('C3')
        to1.update_field(to2.field)
        
        self.assertEqual(to1.is_full(), True)
        

if __name__ == "__main__":
    unittest.main()