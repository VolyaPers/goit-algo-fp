import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.vertices[from_vertex][to_vertex] = weight
        self.vertices[to_vertex][from_vertex] = weight

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}

        heap = [(0, start)]

        visited = set()

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.vertices[current_vertex].items():
                if neighbor in visited:
                    continue

                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))

        return distances, previous

    def get_path(self, previous, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        if path[0] == start:
            return path
        return []

    def print_results(self, start, distances, previous):
        print(f"\nНайкоротші шляхи від вершини '{start}':")
        print("-" * 50)
        for vertex in sorted(distances.keys()):
            if vertex == start:
                continue
            path = self.get_path(previous, start, vertex)
            path_str = " -> ".join(path)
            print(f"До '{vertex}': відстань = {distances[vertex]}, шлях: {path_str}")


if __name__ == "__main__":
    graph = Graph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 8)
    graph.add_edge("C", "E", 10)
    graph.add_edge("D", "E", 2)
    graph.add_edge("D", "F", 6)
    graph.add_edge("E", "F", 3)

    print("Граф (ребра з вагами):")
    print("-" * 50)
    printed_edges = set()
    for vertex in graph.vertices:
        for neighbor, weight in graph.vertices[vertex].items():
            edge = tuple(sorted([vertex, neighbor]))
            if edge not in printed_edges:
                print(f"{vertex} -- {neighbor}: {weight}")
                printed_edges.add(edge)

    start_vertex = "A"
    distances, previous = graph.dijkstra(start_vertex)

    graph.print_results(start_vertex, distances, previous)

    print("\n" + "=" * 50)
    print("Таблиця найкоротших відстаней:")
    print("-" * 50)
    print(f"{'Вершина':<10} {'Відстань':<10}")
    print("-" * 50)
    for vertex in sorted(distances.keys()):
        print(f"{vertex:<10} {distances[vertex]:<10}")
