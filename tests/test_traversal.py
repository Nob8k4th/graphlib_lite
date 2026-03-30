from graphlib_lite.graph import Graph
from graphlib_lite.traversal import bfs, dfs

def sample():
    g=Graph(); g.add_edge('a','b'); g.add_edge('a','c'); return g

def test_bfs_pass():
    assert bfs(sample(),'a')[0]=='a'

def test_dfs_pass():
    assert dfs(sample(),'a')[0]=='a'

def test_bfs_len_pass():
    assert len(bfs(sample(),'a'))==3

def test_dfs_len_pass():
    assert len(dfs(sample(),'a'))==3

def test_bfs_order_pass():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    result = bfs(g, 'a')
    assert result.index('a') < result.index('b')
    assert result.index('a') < result.index('c')
    assert result.index('b') < result.index('d') or result.index('c') < result.index('d')
