import heapq
from grid import Board


def dijkstra(graph, start_key):
    start_vertex = graph.get_vertex(start_key)
    if not start_vertex:
        return None

    pq = [(0, start_vertex)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    previous_vertices = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in current_vertex.get_neighbors():
            weight = current_vertex.get_weight(neighbor)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_vertices


def shortest_path(graph, start_key, end_key):
    distances, previous_vertices = dijkstra(graph, start_key)
    if not distances[end_key]:
        return None

    path = []
    current_vertex = graph.get_vertex(end_key)
    while current_vertex:
        path.append(current_vertex.get_key())
        current_vertex = previous_vertices[current_vertex]

    return distances[end_key], path[::-1]