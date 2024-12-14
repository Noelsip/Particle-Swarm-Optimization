import sys

# Algoritma Dijkstra untuk menemukan jalur terpendek dari satu titik ke titik lainnya dalam sebuah graf
# Penjelasan diberikan dalam bentuk komentar di dalam program


# Fungsi untuk menemukan simpul dengan jarak minimum yang belum diproses
def min_distance(dist, spt_set):
    min_val = sys.maxsize
    min_index = -1

    for v in range(len(dist)):
        if dist[v] < min_val and not spt_set[v]:
            min_val = dist[v]
            min_index = v

    return min_index

# Fungsi untuk mencetak jalur terpendek dari sumber ke simpul tertentu
def print_solution(dist):
    print("Vertex \tDistance from Source")
    for i in range(len(dist)):
        print(f"{i} \t\t{dist[i]}")

# Fungsi utama yang mengimplementasikan algoritma Dijkstra
def dijkstra(graph, src):
    dist = [sys.maxsize] * len(graph)  # Inisialisasi jarak dari sumber ke semua simpul dengan infinity
    dist[src] = 0  # Jarak dari sumber ke dirinya sendiri adalah 0
    spt_set = [False] * len(graph)  # Set untuk melacak simpul yang sudah diproses

    for _ in range(len(graph)):
        u = min_distance(dist, spt_set)  # Pilih simpul dengan jarak minimum yang belum diproses
        spt_set[u] = True  # Tandai simpul sebagai sudah diproses

        for v in range(len(graph)):
            # Update jarak dist[v] jika belum diproses, ada edge dari u ke v, dan total jarak dari sumber ke v melalui u lebih kecil dari jarak saat ini
            if not spt_set[v] and graph[u][v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist)

# Contoh graf yang direpresentasikan sebagai matriks adjacency
graph = [
    [0, 10, 20, 0, 0, 0],
    [10, 0, 0, 50, 10, 0],
    [20, 0, 0, 20, 33, 0],
    [0, 50, 20, 0, 20, 2],
    [0, 10, 33, 20, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

# Panggil fungsi dijkstra dengan sumber dari simpul 0
dijkstra(graph, 0)