
import argparse


def parse_args():
    """
    Parses commane line arguments with argparse
    -----------------
    Parameters: None
    _________________
    Returns: object with following attributes (all are required)
    1. args.src_x: int
        x coordinate of starting point in maze
    2. args.src_y: int
        y coordinate of starting point in maze
    3. args.tgt_x: int
        x coordinate of target end point in maze
    4. args.tgt_y: int
        y coordinate of target end point in maze
    5. args.maze_rows: string list
        each entry in the list represents one row of the maze matrix
        strings only contain 0's (empty cell) and 1's (blocked cell)
    """
    parser = argparse.ArgumentParser(description="Process CLAs required for maze solving.")

    parser.add_argument("src_x", type=int, help="x coordinate of starting point in maze")
    parser.add_argument("src_y", type=int, help="y coordinate of starting point in maze")
    parser.add_argument("tgt_x", type=int, help="x coordinate of target end point in maze")
    parser.add_argument("tgt_y", type=int, help="y coordinate of target end point in maze")
    parser.add_argument("maze_rows", nargs='+', help="each row of the maze, separated by space, only 0 1 allowed")

    args = parser.parse_args()
    return args


def construct_maze():
    """
    constructs matrix from data read in 
    """
    pass


def solve_maze():
    """
    solves maze recursively
    """
    pass


def draw_soluion():
    """
    draws out solution maze using pyplot
    """
    pass


def print_solution():
    """
    prints out coordinates of solution path in command line
    """
    pass


def generate_new_maze():
    """
    generate a new maze to output to the user
    """
    pass


if __name__ == "__main__":
    args = parse_args()
    #testing
    print(args.src_x)
    print(args.maze_rows)
