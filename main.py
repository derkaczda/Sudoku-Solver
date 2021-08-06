import argparse
from solver.solver import BackwardSolver
from solver.grid import Grid

import pygame, sys, random
from pygame.locals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default="", type=str,
                        help='path to a board file')

    arguments = parser.parse_args()
    if arguments.file != "":
        grid = Grid.from_file(arguments.file)
        solver = BackwardSolver(grid)
        solver.solve()
        grid.show()


    pygame.init()

    # Background color
    BACKGROUND_COLOR = (255, 255, 255)

    FPS = 60
    fpsClock = pygame.time.Clock()
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Sudoku solver')

    def main():
        looping = True
        while looping:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Process stuff here

            window.fill(BACKGROUND_COLOR)
            pygame.display.update()
            fpsClock.tick(FPS)

    main()
