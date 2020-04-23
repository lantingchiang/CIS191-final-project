#!/usr/bin/python3

import argparse


def parse_args():
    """
    Parses command line arguments with argparse
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

    # length of first row (all rows should have the same length)
    length = len(args.maze_rows[0])
    # check for src and tgt in bounds
    min = min(args.src_x, args.src_y, args.tgt_x, args.tgt_y)
    max = max(args.src_x, args.src_y, args.tgt_x, args.tgt_y)
    if min < 0 or max >= len(args.maze_rows):
        print("Error: src/tgt out of maze bounds")
        # quit

    for row in args.maze_rows:
        if len(row) != length:
            print("Error: Maze not rectangular")
            # quit
        for char in row:
            if char != '0' and char != '1':
                print("Error: Input consists of characters that are not 0's or 1's")
                # quit
        # row is a string in the list, char is a char in the string row
        # create graph char-by-char, row-by-row

    print(args.src_x)
    print(args.maze_rows)
