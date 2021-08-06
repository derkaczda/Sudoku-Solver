import argparse
from solver.solver import BackwardSolver
from solver.grid import Grid

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
