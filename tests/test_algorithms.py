import pytest
from graphlib_lite.graph import Graph
from graphlib_lite.algorithms import dijkstra, topological_sort

def test_dijkstra_fail1():
    g=Graph(directed=True); g.add_edge('a','b'); assert dijkstra(g,'a')['b']==1

def test_dijkstra_fail2():
    g=Graph(directed=True); g.add_edge('a','b'); g.add_edge('b','c'); assert dijkstra(g,'a')['c']==2

def test_topological_fail_undirected():
    g=Graph(); g.add_edge('a','b')
    with pytest.raises(ValueError):
        topological_sort(g)

def test_topological_contains_all_nodes_pass():
    g=Graph(directed=True); g.add_edge('a','b'); g.add_edge('b','c')
    result = topological_sort(g)
    assert set(result) == {'a', 'b', 'c'}

def test_dijkstra_start_zero_pass():
    g=Graph(directed=True); g.add_node('a'); g.add_node('b')
    assert dijkstra(g, 'a')['a'] == 0

def test_dfs_visits_all_connected_pass():
    from graphlib_lite.traversal import dfs
    g=Graph(); g.add_edge('a','b'); g.add_edge('b','c')
    assert set(dfs(g, 'a')) == {'a', 'b', 'c'}
