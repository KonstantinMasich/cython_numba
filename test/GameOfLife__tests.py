from gol_naive import GameOfLife
import unittest


class GameOfLifeTests(unittest.TestCase):
    gol = GameOfLife(3, 3)

    def test_check_cell(self):
        """A small sanity test."""
        curr_state = [[True, False, False], [False]*3, [False]*3]
        next_state = [[False]*3] * 3
        self.check_field(curr_state, next_state)
        curr_state = [[True, True, False], [False]*3, [False]*3]
        next_state = [[False]*3] * 3
        self.check_field(curr_state, next_state)
        curr_state = [[True]*3, [False]*3, [False]*3]
        next_state = [[False, True, False], [False, True, False], [False]*3]
        self.check_field(curr_state, next_state)
        curr_state = [[False]*3, [True]*3, [False]*3]
        next_state = [[False, True, False], [False, True, False], [False, True, False]]
        self.check_field(curr_state, next_state)

    def check_field(self, curr_state: list, next_state: list):
        self.gol.f = curr_state
        res        = [[self.gol._check_cell(i, j) for j in range(3)] for i in range(3)]
        self.assertEqual(next_state, res)


if __name__ == '__main__':
    unittest.main()
