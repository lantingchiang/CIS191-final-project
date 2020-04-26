#!/usr/bin/python3

import argparse
from graph import Graph
import tkinter as tk
import turtle


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
    parser.add_argument(
        "maze_rows", nargs="+", help="each row of the maze, separated by space, only 0 1 allowed"
    )

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
    min_of_all = min(args.src_x, args.src_y, args.tgt_x, args.tgt_y)
    max_x = max(args.src_x, args.tgt_x)
    max_y = max(args.src_y, args.tgt_y)
    if min_of_all < 0 or max_x >= length or max_y >= len(args.maze_rows):
        raise Exception("src/tgt out of maze bounds")

    for s in args.maze_rows:
        if len(s) != length:
            raise Exception("Maze not rectangular")
        row = []
        for char in s:
            if char != "0" and char != "1":
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
            if matrix[y][x] == 0:
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


def solve_maze(g):
    """
    solves maze with breadth first search
    -----------
    Parameters:
    g: Graph
    -----------
    Returns:
    list of 2-element tuples, i.e. coordinates, (x, y) along path from source to target
    """
    path = []

    # TODO

    return path


def draw_solution(matrix, path):
    """
    draws out solution maze using
    -----------
    Paramters:
    matrix: 2d int array
    path: list of coordinates(tuples) along path from source to target
    """
    rows = len(matrix)
    cols = len(matrix[0])
    # width of each cell drawn; window is a bit larger than 600 * 600
    width = 600 / max(rows, cols)

    # DRAW MAZE
    turtle.tracer(0)  # turnoff animation
    turtle.hideturtle()
    for r in range(rows):
        for c in range(cols):
            x_pos = -300 + width * c
            y_pos = 300 - width * r
            turtle.penup()  # doesn't draw when moving pen
            turtle.goto(x_pos, y_pos)
            turtle.pendown()

            # draw filled shape if cell is blocked
            if matrix[r][c] == 1:
                turtle.fillcolor("black")
                turtle.begin_fill()
            # draw square
            for i in range(4):
                turtle.forward(width)
                turtle.right(90)
            turtle.end_fill()
    turtle.update()  # show drawings

    # DRAW PATH
    # start at middle of first cell in path
    turtle.tracer(1, 10)
    turtle.penup()
    turtle.goto(-300 + width * path[0][0] + width / 2, 300 - width * path[0][1] - width / 2)
    turtle.pendown()
    turtle.pencolor("orange")
    turtle.pensize(10)
    turtle.circle(10)  # draw starting point
    for i in range(1, len(path) - 1):
        # draw until middle of next cell
        turtle.goto(-300 + width * path[i][0] + width / 2, 300 - width * path[i][1] - width / 2)

    turtle.circle(10)  # draw end point

    tk.mainloop()  # needed for canvas window


def print_solution(coords):
    """
    prints out coordinates of solution path in command line
    ---------------
    Parameters:
    coords: two-int-tuple list
    list of coordinates along path from source to target
    """
    string = ""
    for i in range(len(coords) - 1):
        string += coords[i] + "->"
    string += coords[len(coords) - 1]

    print(string)


def generate_new_maze():
    """
    generate a new maze to output to the user
    """
    pass


if __name__ == "__main__":
    """
    Call methods one by one to read in args, build maze and solve maze
    """
    args = parse_args()

    maze_matrix = construct_maze(args)
    print(maze_matrix)

    graph = build_graph(maze_matrix)

    # path = solve_maze(graph)

    # print_solution(path)

    path = [(1, 1), (2, 1), (2, 2), (3, 2)]  # dummy path for testing
    draw_solution(maze_matrix, path)

    # generate_new_maze()

    # testing
    # ./maze_solver.py
    # python3 -c 'import maze_solver; maze_solver.parse_args()' 0 0 0 0 01010 00000
