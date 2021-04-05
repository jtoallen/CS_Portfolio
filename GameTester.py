

import unittest
from FocusGame import FocusGame

class TestFocusGame(unittest.TestCase):
    """ test class for FocusGame"""
    #test if game can be initialized

    def test_init_board_setup(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        # print(game._plyr[0])
        # print(game._plyr[2])
        self.assertIsNotNone(game.get_board())
        self.assertEqual(game.show_pieces((0,0)), ['R'])
        self.assertEqual(game.show_pieces((0,1)), ['R'])
        self.assertEqual(game.show_pieces((5,5)), ['G'])
        self.assertEqual(game.get_board()[0][:], [['R'], ['R'], ['G'], ['G'], ['R'], ['R']])
        self.assertEqual(game.get_board()[1][:], [['G'], ['G'], ['R'], ['R'], ['G'], ['G']])
        self.assertEqual(game.get_board()[2][:], [['R'], ['R'], ['G'], ['G'], ['R'], ['R']])
        self.assertEqual(game.get_board()[3][:], [['G'], ['G'], ['R'], ['R'], ['G'], ['G']])
        self.assertEqual(game.get_board()[4][:], [['R'], ['R'], ['G'], ['G'], ['R'], ['R']])
        self.assertEqual(game.get_board()[5][:], [['G'], ['G'], ['R'], ['R'], ['G'], ['G']])
        self.assertIs(game.get_turn(), None)
        self.assertEqual(game._p1_name,'PlayerA')
        self.assertEqual(game._p2_name,'PlayerB')
        self.assertEqual(game._p1_clr,'R')
        self.assertEqual(game._p2_clr,'G')
        self.assertEqual(game._p1_reserve, 0)
        self.assertEqual(game._p2_reserve, 0)
        self.assertEqual(game._captured_by_p1, 0)
        self.assertEqual(game._captured_by_p2, 0)
        self.assertIs(game._num_pcs, None)
        self.assertIs(game._plyr_turn, None)

    def test_player_names_and_colors(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertIs(game.get_p1_name(), "PlayerA")
        self.assertIs(game.get_p2_name(), "PlayerB")
        self.assertIs(game.get_p1_clr(), 'R')
        self.assertIs(game.get_p2_clr(), 'G')

    def test_false_reserved_methods(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.reserved_move("PlayerA", (0,0)), False)
        self.assertEqual(game.reserved_move("PlayerB", (0,0)), False)
        self.assertEqual(game.show_reserve('PlayerA'), 0)

    def test_successive_move_pieces_playerA(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual((game.move_piece('PlayerA', (0,0), (0,1), 1)), 'successfully moved')
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (0, 1), (0, 2), 1), 'successfully moved')
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (0,2), (0,4), 2), 'successfully moved')

    def test_successive_move_pieces_playerB(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        self.assertEqual(game.move_piece('PlayerB', (1, 0), (1, 1), 1), 'successfully moved')
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (1, 1), (1, 2), 1), 'successfully moved')
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (1, 2), (1, 4), 2), 'successfully moved')

    def test_alternate_multiple_moves(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.move_piece('PlayerA', (0, 0), (0, 1), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (1, 0), (1, 1), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (4, 4), (4, 5), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (1, 4), (1, 5), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (5, 2), (5, 1), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (5, 4), (5, 3), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (2, 1), (2, 0), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (2, 3), (2, 2), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (4, 1), (4, 2), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (4, 3), (4, 4), 1), 'successfully moved')

    def test_alternate_player_move_columns(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.move_piece('PlayerB', (4, 3), (3, 3), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (5, 2), (4, 2), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (3, 3), (4, 3), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (4, 2), (5, 2), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (1, 1), (2, 1), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (1, 2), (2, 2), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerB', (1, 4), (0, 4), 1), 'successfully moved')
        self.assertEqual(game.move_piece('PlayerA', (2, 4), (1, 4), 1), 'successfully moved')

    def test_attempt_move_pieces_playerB_multiple_times(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual((game.move_piece('PlayerB', (1, 0), (1, 1), 1)), 'successfully moved')
        self.assertEqual((game.move_piece('PlayerB', (0, 0), (0, 1), 2)), False)
        game.move_piece('PlayerB', (1, 0), (1, 1), 1)
        self.assertEqual(game.move_piece('PlayerB', (1, 0), (1, 1), 1), False)

    def test_invalid_location(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.move_piece('PlayerA', (0, 0), (1, 1), 1), False)
        self.assertEqual(game.move_piece('PlayerB', (5,5), (5,6), 1), False)

    def test_show_pieces_playerA(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.show_pieces((0, 0)), ['R'])
        self.assertEqual(game.show_pieces((0, 1)), ['R'])
        self.assertEqual(game.show_pieces((0, 4)), ['R'])
        self.assertEqual(game.show_pieces((0, 5)), ['R'])
        self.assertEqual(game.show_pieces((1, 2)), ['R'])
        self.assertEqual(game.show_pieces((1, 3)), ['R'])
        self.assertEqual(game.show_pieces((2, 0)), ['R'])
        self.assertEqual(game.show_pieces((2, 1)), ['R'])
        self.assertEqual(game.show_pieces((2, 4)), ['R'])
        self.assertEqual(game.show_pieces((2, 5)), ['R'])
        self.assertEqual(game.show_pieces((3, 2)), ['R'])
        self.assertEqual(game.show_pieces((3, 3)), ['R'])
        self.assertEqual(game.show_pieces((4, 0)), ['R'])
        self.assertEqual(game.show_pieces((4, 1)), ['R'])
        self.assertEqual(game.show_pieces((4, 4)), ['R'])
        self.assertEqual(game.show_pieces((4, 5)), ['R'])
        self.assertEqual(game.show_pieces((5, 2)), ['R'])
        self.assertEqual(game.show_pieces((5, 3)), ['R'])
        game.move_piece('PlayerA', (0,0), (0,1), 1)
        #need this first move to execute before next move has 2 tokens in list
        self.assertEqual(game.show_pieces((0, 1)), ['R','R'])
        game._plyr_turn = "PlayerA"
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        self.assertEqual(game.show_pieces((0,3)), ['G', 'R', 'R'])
        game._plyr_turn = "PlayerA"
        game.move_piece('PlayerA', (0, 3), (3, 3), 3)
        self.assertEqual(game.show_pieces((3,3)), ['R', 'G', 'R', 'R'])

    def test_show_captured_player_defaults(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.show_captured("PlayerA"), 0)
        self.assertEqual(game.show_captured("PlayerB"), 0)
        game._captured_by_p1 = 5
        self.assertEqual(game.show_captured("PlayerA"), 5)
        game._captured_by_p2 = 1024
        self.assertEqual(game.show_captured("PlayerB"), 1024)
        game._captured_by_p1 = -1.423
        self.assertEqual(game.show_captured("PlayerA"), -1.423)

    def test_show_pieces_playerB(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0,0), (0,1), 1)
        #need this first move to execute before next move has 2 tokens in list
        self.assertEqual(game.show_pieces((0, 1)), ['R','R'])
        self.assertEqual(game.show_captured("PlayerA"), 0)

    def test_show_methods_playerB(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerB', (1,1), (1,2), 1)
        #need this first move to execute before next move has 2 tokens in list
        self.assertEqual(game.show_pieces((1, 2)), ['R','G'])
        self.assertEqual(game.show_captured("PlayerB"), 0)
        game._captured_by_p2 = 2
        self.assertEqual(game.show_captured('PlayerB'), 2)

    def test_remove_method_playerA(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game._board[0][5] = ['R', 'R', 'R', 'G', 'G']
        self.assertEqual(game.move_piece('PlayerA', (0,4), (0,5), 1),'successfully moved')
        self.assertEqual(game.show_pieces((0,5)), ['R', 'R', 'G', 'G', 'R'])
        self.assertEqual(game.show_reserve('PlayerA'), 1)

    def test_remove_method_playerB(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game._board[3][5] = ['G', 'G', 'R', 'G', 'G']
        # self.assertEqual() #game show board = to list above
        self.assertEqual(game.move_piece('PlayerB', (3,4), (3,5), 1),'successfully moved')
        self.assertEqual(game.show_pieces((3,5)), ['G', 'R', 'G', 'G', 'G'])
        self.assertEqual(game.show_reserve('PlayerB'), 1)

    def test_successful_reserved_move_playerA(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game._p1_reserve = 1
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move('PlayerA', (5,1)), 'successfully moved')

    def test_reserved_move_first_play_of_game(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertIs(game.reserved_move('PlayerA', (0,0)), False)
        self.assertIs(game.reserved_move('PlayerB', (0,0)), False)

    def test_p1_successive_reserve_moves(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        game._p1_reserve = 4
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (5,4), 1), 'successfully moved')
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        game._p1_reserve = 6
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (5, 4), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 5)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (5, 5), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 4)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (2, 1), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 3)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (1, 2), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 2)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (1, 2), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 1)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (4, 3), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 0)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move("PlayerA", (4, 3), 1), False)
        self.assertEqual(game.show_reserve("PlayerA"), 0)

    def test_p2_successive_reserve_moves(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        game._p2_reserve = 6
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (5,4), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 5)

        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (5, 5), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 4)

        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (2, 1), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 3)

        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (1, 2), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 2)

        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (1, 2), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 1)

        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (4, 3), 1), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 0)

        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move("PlayerB", (4, 3), 1), False)
        self.assertEqual(game.show_reserve("PlayerB"), 0)

    def test_successful_reserved_move_playerB(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game._p2_reserve = 1
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.reserved_move('PlayerB', (0,0)), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerB"), 0)
        game._p1_reserve = 1
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.reserved_move('PlayerA', (5,5)), 'successfully moved')
        self.assertEqual(game.show_reserve("PlayerA"), 0)

    def test_diagonal_move(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (0,0), (1,1), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (1,0), (0,1), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (0,5), (1,4), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (5,5), (4,4), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (0,5), (2,4), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (2,2), (3,1), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (3,2), (2,1), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (4,2), (5,3), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (4,4), (3,5), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (3,1), (2,2), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (3,2), (2,1), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (3,1), (2,0), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (3,2), (2,3), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (3,1), (4,0), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (3,2), (4,3), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece('PlayerB', (3,1), (4,2), 1), False)
        game._plyr_turn = "PlayerA"
        self.assertEqual(game.move_piece('PlayerA', (3,2), (4,1), 1), False)

    def test_get_hgth(self):
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        self.assertEqual(game.get_hght((0,0)),1)
        self.assertEqual(game.get_hght((5,5)),1)
        game.move_piece('PlayerA', (3, 2), (3, 3), 1)
        self.assertEqual(game.get_hght((3,3)),2)
        game._plyr_turn = "PlayerA"
        game.move_piece('PlayerA', (3, 3), (3, 5), 2)
        self.assertEqual(game.get_hght((3, 5)), 3)

    def test_out_of_bounds(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        self.assertEqual(game.move_piece('PlayerA', (0,5), (0,6), 1), False)
        self.assertEqual(game.move_piece('PlayerB', (1,5), (1,6), 1), False)
        self.assertEqual(game.move_piece('PlayerA', (4,5), (6,5), 1), False)
        self.assertEqual(game.move_piece('PlayerB', (5,5), (6,5), 1), False)

    def test_incorrect_number_spaces_to_move(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        self.assertEqual(game.move_piece('PlayerA', (0,0), (0,1), 2), False)
        self.assertEqual(game.move_piece('PlayerB', (5,5), (5,3), 1), False)
        game._plyr_turn = "PlayerB"
        self.assertEqual((game.move_piece('PlayerB', (1,0), (1,1), 2)), False)

    def test_get_turn(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        game.move_piece('PlayerB', (5,0), (5,1), 1)
        self.assertEqual(game.get_turn(), "PlayerA")
        game.move_piece('PlayerA', (0,1), (1,1), 1)
        self.assertEqual(game.get_turn(), "PlayerB")
        game.move_piece('PlayerA', (0,5), (0,4), 1)
        self.assertEqual(game.get_turn(), "PlayerB")
        game.move_piece('PlayerB', (2,2), (2,3), 1)
        self.assertEqual(game.get_turn(), "PlayerA")
        game.move_piece('PlayerA', (5,2), (5,1), 1)
        self.assertEqual(game.get_turn(), "PlayerB")

    def test_player_plays_out_of_turn(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        game.move_piece('PlayerA', (0,1), (0,2), 1) #valid move
        self.assertTrue(game.get_turn(), "PlayerB") #true
        self.assertFalse(game.move_piece('PlayerA', (2,0), (2,1), 1))
        game.move_piece('PlayerB', (3,4), (3,3), 1) #valid move
        self.assertTrue(game.get_turn(), "PlayerA")
        self.assertFalse(game.move_piece('PlayerB', (4,3), (3,3), 1))
        self.assertEqual(game.get_turn(), "PlayerA")
        self.assertEqual(game.get_turn(), "PlayerA")

    def test_show_reserve(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        self.assertEqual(game.show_reserve("PlayerB"), 0)
        self.assertEqual(game.show_reserve("PlayerA"), 0)
        game._p1_reserve = 6
        game._p2_reserve = 8
        self.assertEqual(game.show_reserve("PlayerA"), 6)
        self.assertEqual(game.show_reserve("PlayerB"), 8)

    def test_check_player_wins_after_several_moves(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        self.assertEqual(game.move_piece("PlayerA", (0,0), (1,0), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (5,5), (4,5), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (1,0), (1,2), 2), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (2,2), (2,1), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (4,4), (4,3), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (4,2), (4,3), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (5,2), (4,2), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (5,0), (4,0), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (1, 2), (1, 5), 3), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (4, 0), (4, 2), 2), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (1, 5), (5, 5), 4), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (5, 4), (5, 5), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (5, 3), (5, 4), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (5, 1), (5, 2), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (5, 4), (5, 5), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (4, 3), (4, 5), 2), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (2, 5), (3, 5), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (4, 3), (4, 4), 1), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (3, 5), (5, 5), 2), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerB", (4, 2), (4, 5), 3), 'successfully moved')
        self.assertEqual(game.move_piece("PlayerA", (3, 3), (3, 2), 1), 'successfully moved')
        game._captured_by_p1 = 5
        game._captured_by_p2 = 5
        game._plyr_turn = "PlayerB"
        self.assertEqual(game.move_piece("PlayerB", (4, 5), (5, 5), 1), 'PlayerB Wins')
        game._plyr_turn = 'PlayerA'
        game._board[4][5] = ['B', 'A', 'B', 'A', 'A', 'B']
        game._board[5][5] = ['A']
        self.assertEqual(game.move_piece('PlayerA', (5, 5), (4, 5), 1), 'PlayerA Wins')

    def test_check_p2_wins(self):
        game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
        game._plyr_turn = "PlayerB"
        game._captured_by_p2 = 5
        game._board[0][0] += ['A', 'A', 'A', 'A', 'A']
        self.assertEqual(game.move_piece("PlayerB", (1,0), (0,0), 1), "PlayerB Wins")
        game._plyr_turn = "PlayerB"



game = FocusGame(('PlayerA', 'A'), ('PlayerB', 'B'))
game.print()

if __name__ == "__main__":
    unittest.main()
