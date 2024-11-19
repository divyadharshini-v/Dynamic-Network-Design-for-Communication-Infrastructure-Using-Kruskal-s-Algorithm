class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        self.edges = []  # List to store all edges


    def add_edge(self, u, v, weight):
                                  # Adds an edge with a given weight between nodes u and v
        self.edges.append((weight, u, v))

    def find(self, parent, v):
        if parent[v] != v:

            return self.find(parent, parent[v])
        return parent[v]
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        self.edges = []  # List to store all edges


    def add_edge(self, u, v, weight):
                                  # Adds an edge with a given weight between nodes u and v
        self.edges.append((weight, u, v))

    def find(self, parent, v):
        if parent[v] != v:

            return self.find(parent, parent[v])
        return parent[v]

    # Initialize parent and rank for each vertex
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

            mst = []  # This will store the MST edges

        for weight, u, v in self.edges:
        # Check if including this edge creates a cycle
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

…print("Minimum Spanning Tree (MST) for the network:")

for u, v, weight in mst:
      print(f"Location {u} -- Location {v} with cost {weight}")
