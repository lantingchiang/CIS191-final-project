#!/usr/bin/python3

import argparse
from graph import Graph 


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


def construct_maze(args):
    """
    constructs matrix from data read in 
    -----------
    Parameters:
    args: arguments parsed from parser
    -----------
    Returns:
    2d array representation of maze
    """
    matrix = []

    # length of first row (all rows should have the same length)
    length = len(args.maze_rows[0])

    # check for src and tgt in bounds
    min = min(args.src_x, args.src_y, args.tgt_x, args.tgt_y)
    max_x = max(args.src_x, args.tgt_x)
    max_y = max(args.src_y, args.tgt_y)
    if min < 0 or max_x >= length or max_y >= len(args.maze_rows):
        raise Exception("src/tgt out of maze bounds")

    for s in args.maze_rows:
        if len(s) != length:
            raise Exception("Maze not rectangular")
        row = []
        for char in s:
            if char != 0 and char != 1:
                raise Exception("Illegal maze")
            row.append(int(char))

        matrix.append(row)

    return matrix


def build_graph(matrix):
    """
    constructs graph representation of maze from 2d-array
    --------------
    Parameters:
    matrix: 2d int array representing maze
    --------------
    Returns:
    Graph object of maze, with each cell being a node and an undirected edge existing between
    any two cells that are connected in the up/down/left/right direction. Blocked cells
    cannot be connected to any cells
    """
    rows = len(matrix)
    columns = len(matrix[0])
    # convention of (0, 0) in the top left corner and (columns, rows) in the bottom right corner
    g = Graph(rows * columns)

    # keeps track of the current vertex
    vertex = 0
    for y in range(rows):
        for x in range(columns):
            # determine whether or not to add edges for a particular vertex
            if matrix[y][x] = 0:
                # scan the right side of the vertex for an edge
                if x + 1 < columns:
                    if matrix[y][x + 1] == 0:
                        g.addEdge(vertex, vertex + 1)
                # scan the left side of the vertex for an edge
                if x - 1 >= 0:
                    if matrix[y][x - 1] == 0:
                        g.addEdge(vertex, vertex - 1)
                # scan below the vertex for an edge
                if y + 1 < rows:
                    if matrix[y + 1][x] == 0:
                        g.addEdge(vertex, vertex + columns)
                # scan above the vertex for an edge
                if y - 1 >= 0:
                    if matrix[y - 1][x] == 0:
                        g.addEdge(vertex, vertex - columns)
            vertex += 1

    return g


def solve_maze():
    """
    solves maze with breadth first search
    """
    pass


def draw_solution():
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
    # testing
    # ./maze_solver.py
    # python3 -c 'import maze_solver; maze_solver.parse_args()' 0 0 0 0 01010 00000

    # delete the stuff below later

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
