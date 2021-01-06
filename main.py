import argparse
from grid import Grid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default="", type=str,
                        help='path to a board file')

    arguments = parser.parse_args()
    if arguments.file != "":
        grid = Grid.from_file(arguments.file)
        print(f"Second row {grid.row(1)}")
        print(f"first column {grid.column(0)}")
        print(f"first cell {grid.cell(1)}")
