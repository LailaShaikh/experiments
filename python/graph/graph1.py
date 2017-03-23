from collections import deque


class Vertex(object):
    def __init__(self, name):
        self.name = name   # Name of the vertex
        self.connections = {}

    def add_neighbor(self, neighbor_vertex, cost):
        self.connections[neighbor_vertex] = cost

    def __str__(self):
        return "%s connected To: %s" % (self.name, str([x.name for x in self.connections]))

    def get_cost(self, nbr):
        return self.connections[nbr]
        
    def get_neighbors(self):
        return self.connections.keys()
        

class Graph(object):
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name):
        v = Vertex(name)
        if name not in self.vertices:
            self.vertices[name] = v

    def add_edge(self, src, dest, cost=0):
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[src].add_neighbor(self.vertices[dest], cost)

    def add_undirected_edge(self, src, dst, cost=0):
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        
        self.vertices[src].add_neighbor(self.vertices[dest], cost)
        self.vertices[dst].add_neighbor(self.vertices[src], cost)
        
  

def bfs(g, s):
    '''
    g -> graph
    s -> source node
    '''
    
    visited = []
    q = deque()
    q.append(s)
    visited.append(s)

    while len(q):
        print q
        cn = q.popleft()
        print "visiting", cn
        visited.append(cn)

        for nn in g.vertices[cn].get_neighbors():
            if nn.name not in visited:
                q.append(nn.name)


if __name__ == '__main__':
    v = Vertex('0')
    v1 = Vertex('1')
    v2 = Vertex('2')
    v3 = Vertex('3')
    v4 = Vertex('4')
    v5 = Vertex('5')
    v6 = Vertex('6')
    v.add_neighbor(v1, 4)
    v.add_neighbor(v2, 5)
    v.add_neighbor(v3, 5)
    v1.add_neighbor(v2, 5)
    v2.add_neighbor(v3, 5)
    v3.add_neighbor(v4, 5)
    v1.add_neighbor(v4, 5)
    v4.add_neighbor(v5, 5)
    v5.add_neighbor(v1, 5)
  
    g = Graph()
    g.add_edge('0', '2', 3)
    g.add_edge('0', '3', 3)
    g.add_edge('0', '4', 3)
    g.add_edge('2', '3', 3)
   
    bfs(g, '0')
