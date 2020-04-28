# CIS191-final-project
## Installation
Download maze_solver.py and graph.py into the same directory. Install required packages (argparse, turtle, tkinter, random, time) using your system's package manager
## Execution
### On Mac:
`python3 maze_solver.py [src_x] [src_y] [tgt_x] [tgt_y] [maze_ith_row]...`
<ul>
  <li> src_x: the x coordinate of the starting point </li>
  <li> src_y: the y coordinate of the starting point </li>
  <li> tgt_x: the x coordinate of the end point </li>
  <li> tgt_y: the y coordinate of the end point </li>
  <li> maze_ith_row: the ith row of the maze, represented by a string of 0's (empty cells) and 1's (blocked cells)
</ul>
Note:
<ul>
  <li> the upper left hand corner of the maze corresponds to coordinate (0, 0)</li>
  <li> each row in the maze has to be of the same length </li>
  <li> all inputs are required </li>
  <li> `python3 maze_solver.py -h` to see help message
</ul>
## Description
A maze can be described as a two by two grid of blocked cells and empty cells with a starting point and an end point. We take in this information and parse it using the argparse package. We first convert the read in rows of the maze into a 2d array, then construct a graph with nodes representing cells and edges representing valid paths between cells. We then run a breadth first search on the graph to solve the maze, outputting coordinates along the path from the starting point to the end point. We use turtle to draw out the maze and animate the solution path. A random maze of the same dimensions is generated and drawn out 5 seconds after drawing out the solution of the input maze. 

