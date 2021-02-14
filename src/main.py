from gol_naive import GameOfLife

N, M  = 300, 330
SLEEP = 0

if __name__ == '__main__':
    gol = GameOfLife(N, M, delay=SLEEP)
    gol.run()
