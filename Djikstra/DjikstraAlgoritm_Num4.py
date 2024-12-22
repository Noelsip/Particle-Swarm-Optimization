from collections import defaultdict
import heapq

# Konstanta INFINITY untuk nilai tak terhingga
INFINITY = float('inf')

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
        self.nodes = set()

    # Fungsi untuk menambahkan edge ke graf
    def addEdge(self, x, y, w):
        self.graph[x][y] = w
        self.nodes.update([x, y])

    # Fungsi untuk menjalankan algoritma Dijkstra
    def dijkstra(self, src):
        distances = {node: INFINITY for node in self.nodes}
        predecessors = {node: None for node in self.nodes}
        distances[src] = 0
        pq = [(0, src)]
        visited = set()

        # Format header tabel
        nodes_sorted = sorted(self.nodes)
        print(f"{'Step':<5} {'|':<2} {' | '.join(nodes_sorted):<70}")
        print("-" * (8 + len(nodes_sorted) * 7))

        step = 0

        # Proses Dijkstra
        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)

            # Menampilkan langkah-langkah sebagai baris tabel
            self.print_step(step, distances, nodes_sorted)
            step += 1

            for neighbor, weight in sorted(self.graph[current_node].items(), key=lambda x: x[1]):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Menampilkan jarak terpendek setelah tabel
        self.print_shortest_distances(src, distances, predecessors)
        return distances

    # Fungsi untuk mencetak baris tabel
    def print_step(self, step, distances, nodes_sorted):
        row = [f"{distances[node]:<3}" if distances[node] < INFINITY else "∞" for node in nodes_sorted]
        print(f"{step:<5} | {' | '.join(row)}")

    # Fungsi untuk mencetak jarak dan jalur terpendek setelah tabel
    def print_shortest_distances(self, src, distances, predecessors):
        print("\nShortest distances:")
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])  # Urutkan berdasarkan jarak
        for node, distance in sorted_distances:
            if distance < INFINITY and node != src:
                print(f"Jarak terpendek dari {src} menuju {node} adalah {distance}")
                # Cetak jalur setelah jarak
                path = []
                current = node
                while current:
                    path.append(current)
                    current = predecessors[current]
                path.reverse()
                print(" -> ".join(path))

# Membuat instance graf
g = Graph()
g.addEdge('v1','v2',6)
g.addEdge('v1','v3',5)
g.addEdge('v2','v4',5)
g.addEdge('v3','v4',6)
g.addEdge('v3','v6',8)
g.addEdge('v4','v5',10)
g.addEdge('v4','v6',7)
g.addEdge('v5','v8',6)
g.addEdge('v6','v8',14)
g.addEdge('v6','v5',5)
g.addEdge('v6','v7',2)
g.addEdge('v7','v8',6)

# Menjalankan algoritma Dijkstra dari node A
g.dijkstra('v1')
