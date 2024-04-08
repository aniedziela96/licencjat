from vertex import Vertex

class Graph:
    def __init__(self):
        self.vert_list = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def add_edge(self, f, t, weight=1):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __contains__(self, key):  # key in g
        return key in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())


class Board(Graph):
    def __init__(self, n):
        super().__init__()  # Initialize the Graph superclass
        self.create_grid(n)

    def create_grid(self, n):
        """
        Creates a grid that simulates the square map
        :param n: size of the grid
        """
        self.add_vertex((0, 0))
        for row in range(n):
            for col in range(n):
                vertex_key = (row, col)  # Unique key for each vertex based on row and column
                # Connect with right neighbor
                if col < n - 1:
                    self.add_edge(vertex_key, (row, col + 1))
                # Connect with bottom neighbor
                if row < n - 1:
                    self.add_edge(vertex_key, (row + 1, col))

    def add_wall(self, key):
        self.vert_list[key].delete_neighbors()
