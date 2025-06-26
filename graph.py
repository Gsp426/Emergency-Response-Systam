class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, wt):
        self.adj.setdefault(u, []).append((v, wt))
        self.adj.setdefault(v, []).append((u, wt))

    def dijkstra(self, start, end):
        import heapq
        dist = {node: float('inf') for node in self.adj}
        prev = {}
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            d, u = heapq.heappop(heap)
            for v, wt in self.adj[u]:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    prev[v] = u
                    heapq.heappush(heap, (dist[v], v))

        path = []
        node = end
        while node != start:
            path.append(node)
            node = prev.get(node)
            if node is None:
                return []  # No path
        path.append(start)
        return list(reversed(path))
