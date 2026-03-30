# graphlib_lite

`graphlib_lite` 提供常用图结构与算法接口，适合教学、练习和小规模图问题原型。

## 提供能力

- `Graph`：有向/无向图构建，节点和边的增删
- `bfs`、`dfs`：图遍历访问顺序
- `dijkstra`：最短路距离估计
- `topological_sort`：拓扑排序

## 快速使用

```bash
pip install -e .
```

```python
from graphlib_lite import Graph, bfs, dfs, dijkstra, topological_sort

g = Graph(directed=True)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

print(bfs(g, "A"))
print(dfs(g, "A"))
print(dijkstra(g, "A"))
print(topological_sort(g))
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
