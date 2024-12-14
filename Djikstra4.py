from collections import defaultdict

# Initialisasi konstan INFINITY sebagai nilai tak terhingga
INFINITY = float('inf')

class Graph:
    # Fungsi untuk mendefinisikan graf sebagai dictionary dengan nilai default dictionary
    def __init__(self):
        self.graph = defaultdict(dict)
        
    # Fungsi untuk menambahkan edge ke graf
    def addEdge(self, x, y, w):
        if x not in self.graph:
            self.graph[x] = {}
        if y not in self.graph:
            self.graph[y] = {}
        self.graph[x][y] = w
    
    # fungsi untuk menampilkan graf
    def __str__(self):
        for k, v in self.graph.items():
            print("%s -> %s" % (k, v))
    
    # Fungsi untuk mencari jalur terpendek dari node sumber ke node tujuan
    def dijkstra(self, src, dest, visited=[], distances={}, predecessors={}):
        if src not in self.graph:
            raise TypeError("Node Sumber tidak ada di graf")
        if dest not in self.graph:
            raise TypeError("Node tujuan tidak ada di graf")
        if src == dest:
            path=[]
            pred=dest
            while pred != None:
                path.append(pred)
                pred=predecessors.get(pred,None)
            path.reverse()
            
            # Cetak jalur terpendek dan biayanya
            print()
            print('Shortest path: ' + ' -> '.join(path) + " \ncost=" + str(distances[dest]))
            return (path,distances[dest])
        
        else :
            if not visited:
                distances[src]=0
            for neighbor in self.graph[src]:
                if neighbor not in visited:
                    new_distance = distances[src] + self.graph[src][neighbor]
                    if new_distance < distances.get(neighbor,INFINITY):
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = src 
                        
        visited.append(src)
        unvisited={}
        for k in self.graph:
            if k not in visited:
                unvisited[k] = distances.get(k,INFINITY)
        x=min(unvisited, key=unvisited.get)
        self.dijkstra(x, dest, visited, distances, predecessors)
        
# membuat instance dari kelas Graph
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

# Mencari dan menampilkan jalur terpendek dari awal ke tujuan
g.dijkstra('v1', 'v8')
