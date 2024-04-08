TERRAIN = {
    "plains": 1,
    "desert": 2,
    "snow": 3,
    "mountains": 100
}

class Vertex:
    def __init__(self, coords: tuple[int], enviro="plains"):
        self.id = coords
        self.connected_to = {}
        # self.event = ""     # enemy, gold
        self.enviro = enviro

    def set_id(self):
        return self.id

    def add_neighbor(self, nbr, weight=1):
        self.connected_to[nbr] = weight
        # self.connected_to[nbr] = max(TERRAIN[self.enviro], TERRAIN[nbr.enviro])

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def delete_neighbors(self):
        self.connected_to.clear()

    def __str__(self):
        return f"{self.id} connected to: {[x.id for x in self.connected_to]}."



