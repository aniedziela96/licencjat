class Vertex:
    def __init__(self, coords: tuple[int]):
        self.id = coords
        self.connected_to = {}

    def get_id(self):
        return self.id

    def add_neighbor(self, nbr, weight=1):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        try:
            return self.connected_to[nbr]
        except KeyError:
            return None

    def delete_neighbors(self):
        self.connected_to.clear()

    def __str__(self):
        return f"{self.id} connected to: {[x.id for x in self.connected_to]}."