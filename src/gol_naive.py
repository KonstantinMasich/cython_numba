import os
from drawille import Canvas
from random import randint
from time import sleep


class GameOfLife:
    """Tools for basic Conway's Game Of Life simulation.
    Naive version: no deep optimizations, no NumPy/Cython/Numba, just 2D lists."""

    def __init__(self, n: int = 5, m: int = 5, delay: float = 1., field: list = None):
        """Default constructor.
        :param n: int - amount of rows of the cells field
        :param m: int - amount of columns of the cells field
        :param delay: float, in sec - delay after printing current generation
        :param field: list - initial board state (optional)
        """
        self.delay  = delay
        self.gen_no = 0
        if field:
            self.n, self.m = len(field[0]), len(field)
            self.f = field
        else:
            self.n, self.m = n, m
            self.f = [[bool(randint(0, 1)) for _ in range(m)] for _ in range(n)]

    def run(self):
        """Runs the game."""
        while True:
            self._display_drawille()
            sleep(self.delay)
            self._next_gen()

    def _check_cell(self, row: int, col: int) -> bool:
        """Returns True if cell should be alive in the next
        generation, False otherwise."""
        # 1. Calculate indices (spares the "i==row, j==col" check):
        indices = [(i, j) for i in range(max(0, row-1), min(self.n, row+1+1))
                   for j in range(max(0, col-1), min(self.m, col+1+1))]
        indices.remove((row, col))
        # 2. Count adjacent cells and return "life" value of a cell:
        adj_cells = sum([int(self.f[i][j]) for i, j in indices])
        if adj_cells == 3:
            return True
        if self.f[row][col] and adj_cells == 2:
            return True
        return False

    def _next_gen(self):
        """Calculates the next generation."""
        self.f = [[self._check_cell(i, j) for j in range(self.m)] for i in range(self.n)].copy()
        self.gen_no += 1

    def _display(self):
        """Prints cells field as square ASCII characters."""
        os.system('clear')
        for i in range(self.n):
            s = ''.join([' ■ ' if i else '   ' for i in self.f[i]])
            print(s)
        print(f'\nGeneration {self.gen_no}')

    def _display_drawille(self):
        """Prints cells field on a Drawille Canvas."""
        os.system('clear')
        c = Canvas()
        for i in range(self.n):
            for j in range(self.m):
                if self.f[i][j]:
                    c.set(i, j)
        print(c.frame())
        print(f'\nGeneration {self.gen_no}')
        sleep(self.delay)
