import argparse
from grid import Grid
from solver import BackwardSolver

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default="", type=str,
                        help='path to a board file')

    parser.add_argument('--steps', default=1000,
                        type=int, help='number of steps')
    arguments = parser.parse_args()
    if arguments.file != "":
        grid = Grid.from_file(arguments.file)
        solver = BackwardSolver(grid)
        for i in range(arguments.steps):
            solver.step()
            print(f"Step { i + 1 }:")
            grid.print()
