
#!/usr/bin/python3


class Graph:
    """
    Works for undirected graph (can be modified to work with directed ones)
    """

    def __init__(self, n):
        """
        Constructor
        ------------
        Parameters:
        n: int
            number of nodes in the graph
        ------------
        Attribute:
        adj_list: list of int lists
        int list at index i contains the neighbors of node i (nodes represented as ints from 0 to n-1)
        """
        # adjacency list of graph (entry at index i = list of neighbors of node i) initialized with empty neighbor lists
        self.adj_list = [[]] * n

    def getSize(self):
        """
        Returns:
        number of vertices in graph
        """
        return len(self.adj_list)

    def addEdge(self, u, v):
        """
        Adds an edge between vertices u & v
        -----------
        Parameters:
        u: int
            vertex at one end of edge
        v: int
            vertex at another end of edge
        -----------
        Returns:
        void
        """
        if u < 0 or u > len(self.adj_list) - 1 or v < 0 or v > len(self.adj_list) - 1:
            raise Exception("Invalid start/end vertices for edge")

        # add edge by adding to list of neighbors if it's not already in
        if v not in self.adj_list[u] and u not in self.adj_list[v]:
            # undirected graph -> add edge in both directions
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def neighbors(self, u):
        """
        Gets neighbors of node u
        -------------
        Parameters:
        u: int
            vertex to find neighbors of
        -------------
        Returns:
        int list - list of neighbors of vertex u
        """
        if u < 0 or u > len(self.adj_list) - 1:
            raise Exception("Invalid vertex")

        return self.adj_list[u]
