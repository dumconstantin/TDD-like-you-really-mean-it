import unittest

class TicTacToeTestSuite(unittest.TestCase):

    def test_that_a_player_cannot_move_into_an_already_occupied_board_cell(self):
        # Define input
        game_state = {}
        game_state['owned_by_x'] = ['c3']
        game_state['owned_by_zero'] = []
        game_state['who_moves_next'] = 0
        game_state['last_move_was_valid'] = True
        next_move = 'c3'

        # Apply transformation
        occupied_board_positions = game_state['owned_by_x'] + game_state['owned_by_zero']
        game_state['last_move_was_valid'] = next_move not in occupied_board_positions

        # State our expectation about the result of the transformation
        self.assertFalse(game_state['last_move_was_valid'])

