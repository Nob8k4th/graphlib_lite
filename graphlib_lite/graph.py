class Graph:
    def __init__(self, directed=False):
        self.directed=directed
        self.adj={}
    def add_node(self,n): self.adj.setdefault(n,set())
    def add_edge(self,a,b):
        self.add_node(a); self.add_node(b); self.adj[a].add(b)
        if not self.directed: self.adj[b].add(a)
    def remove_edge(self,a,b):
        self.adj.get(a,set()).discard(b)
        if not self.directed: self.adj.get(b,set()).discard(a)
    def remove_node(self,n):
        self.adj.pop(n,None)
