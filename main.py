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
    
    full_red = (255, 0, 0)
    full_green = (0, 255, 0)
    full_blue = (0, 0, 255)
    black = (50, 50, 50)
    # Background color
    BACKGROUND_COLOR = (255, 255, 255)

    FPS = 60
    fpsClock = pygame.time.Clock()
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    grid_size = 9
    width_delta = WINDOW_WIDTH / grid_size
    height_delta = WINDOW_HEIGHT / grid_size

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
            
            line_thickness = 1

            for i in range(1, grid_size + 1):
                new_y = int(i * height_delta)
                new_x = int(i * width_delta)
                pygame.draw.line(window, black, (0, new_y), (WINDOW_WIDTH, new_y), line_thickness)
                pygame.draw.line(window, black, (new_x, 0), (new_x, WINDOW_HEIGHT), line_thickness)

            pygame.display.update()
            fpsClock.tick(FPS)

    main()
