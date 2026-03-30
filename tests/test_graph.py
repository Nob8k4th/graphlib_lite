from graphlib_lite.graph import Graph

def test_add_remove_edge_pass():
    g=Graph(); g.add_edge('a','b'); g.remove_edge('a','b'); assert 'b' not in g.adj['a']

def test_remove_node_fail_cleanup1():
    g=Graph(); g.add_edge('a','b'); g.remove_node('b'); assert 'b' not in g.adj['a']

def test_remove_node_fail_cleanup2():
    g=Graph(); g.add_edge('x','y'); g.remove_node('y'); assert all('y' not in v for v in g.adj.values())

def test_add_node_pass():
    g=Graph(); g.add_node('a'); assert 'a' in g.adj

def test_undirected_pass():
    g=Graph(); g.add_edge('a','b'); assert 'a' in g.adj['b']
