from vertex import Vertex
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt


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
        self.size = n

    def create_grid(self, n):
        """
        Creates a grid that simulates the square map
        :param n: size of the grid
        """
        self.add_vertex((0, 0))
        for row in range(n):
            for col in range(n):
                if col < n - 1:
                    self.add_vertex((row, col + 1))
                if row < n - 1:
                    self.add_vertex((row + 1, col))

    def add_path(self, ver1, ver2):
        self.add_edge(ver1, ver2)

    def as_list(self) -> list[list[int]]:
        lst = []
        n = self.size
        for i in range(n):
            row = [1, 0] * (n - 1)
            row.append(1)
            lst.append(row)
            if i < n - 1:
                lst.append([0] * (2 * n - 1))

        for row in range(self.size):
            for col in range(self.size):
                if self.get_vertex((row, col)).get_weight(b.get_vertex((row, col + 1))):
                    lst[2 * row][2 * col + 1] = 1
                if self.get_vertex((row, col)).get_weight(b.get_vertex((row + 1, col))):
                    lst[2 * row + 1][2 * col] = 1

        return lst 
    
    def get_neighbors_keys(self, key):
        n = self.size
        if key == (0, 0):
            return [(1, 0), (0, 1)]
        
        if key == (0, n - 1):
            return [(0, n - 2), (1, n - 1)]
        
        if key == (n - 1, 0):
            return [(n - 2, 0), (n - 1, 1)]
        
        if key == (n - 1, n - 1):
            return [(n - 1, n - 2), ( n - 2, n - 1)]
        
        if key[0] == 0:
            return [(0, key[1] - 1), (0, key[1] + 1), (1, key[1])]
        
        if key[1] == 0:
            return [(key[0] - 1, 0), (key[0] + 1, 0), (key[0], 1)]
        
        if key[0] == n - 1:
            return [(n - 1, key[1] - 1), (n - 1, key[1] + 1), (n - 2, key[1])]
        
        if key[1] == n - 1:
            return [(key[0] - 1, n - 1), (key[0] + 1, n - 1), (key[0], n - 2)]
        else:
            return [(key[0] - 1, key[1]), (key[0] + 1, key[1]), (key[0], key[1] - 1), (key[0], key[1] + 1)]
    
    def dfs(self, start_key):
        colors = {}
        # print(self.vert_list)
        for v_key in self.vert_list:
            colors[v_key] = "white"
        
        stack = []
        stack.append(self.vert_list[start_key])
        colors[start_key] = 'black'
        while stack:
            current_vert = stack.pop()  # deque
            cur_key = current_vert.get_id()
            # print(f"current vertex: {cur_key}")

            nbrs = self.get_neighbors_keys(cur_key)
            shuffle(nbrs)
            # print(f"neighbors: {nbrs}")

            for nbr_key in nbrs:
                if colors[nbr_key] == 'white':
                    stack.append(current_vert)
                    self.add_edge(cur_key, nbr_key)
                    self.add_edge(nbr_key, cur_key)
                    stack.append(self.get_vertex(nbr_key))
                    colors[nbr_key] = 'black'

            # colors[cur_key] = 'black'

    def __str__(self) -> str:
        lst = self.as_list()
        for row in lst:
            print(row)

    @classmethod
    def fromlist(cls, lst: list[list[int]]):
        b = Board(len(lst))
        
        return b


if __name__ == '__main__':
    # for i in range(1000000):
    #     b = Board(20)
    #     b.dfs((0,0))
    #     l = b.as_list()
    #     with open(f'training_lab/maze{i}.txt','w') as file:
    #         for line in l:
    #             file.write(' '.join(str(p) for p in line) + '\n')

    b = Board(20)
    b.dfs((0,0))
    l = b.as_list()
    print()
    for row in l:
        print(row)

    a = np.array(l)

    fig, ax = plt.subplots()
    im = ax.imshow(a, cmap='Greys_r')
    plt.show()
    