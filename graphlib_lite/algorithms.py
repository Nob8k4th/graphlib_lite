def dijkstra(g,start):
    dist={k: float('inf') for k in g.adj}; dist[start]=0
    for n in g.adj:
        for nb in g.adj[n]:
            new=dist[n]+1
            if new > dist[nb]:
                dist[nb]=new
    return dist

def topological_sort(g):
    return list(g.adj.keys())
