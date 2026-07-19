---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2642.Design%20Graph%20With%20Shortest%20Path%20Calculator/README_EN.md
rating: 1810
source: Biweekly Contest 102 Q4
tags:
    - Graph
    - Design
    - Shortest Path
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2642. Design Graph With Shortest Path Calculator](https://leetcode.com/problems/design-graph-with-shortest-path-calculator)

## Description

<!-- description:start -->

<p>There is a <strong>directed weighted</strong> graph that consists of <code>n</code> nodes numbered from <code>0</code> to <code>n - 1</code>. The edges of the graph are initially represented by the given array <code>edges</code> where <code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, edgeCost<sub>i</sub>]</code> meaning that there is an edge from <code>from<sub>i</sub></code> to <code>to<sub>i</sub></code> with the cost <code>edgeCost<sub>i</sub></code>.</p>

<p>Implement the <code>Graph</code> class:</p>

<ul>
	<li><code>Graph(int n, int[][] edges)</code> initializes the object with <code>n</code> nodes and the given edges.</li>
	<li><code>addEdge(int[] edge)</code> adds an edge to the list of edges where <code>edge = [from, to, edgeCost]</code>. It is guaranteed that there is no edge between the two nodes before adding this one.</li>
	<li><code>int shortestPath(int node1, int node2)</code> returns the <strong>minimum</strong> cost of a path from <code>node1</code> to <code>node2</code>. If no path exists, return <code>-1</code>. The cost of a path is the sum of the costs of the edges in the path.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2642.Design%20Graph%20With%20Shortest%20Path%20Calculator/images/graph3drawio-2.png" style="width: 621px; height: 191px;" />
<pre>
<strong>Input</strong>
[&quot;Graph&quot;, &quot;shortestPath&quot;, &quot;shortestPath&quot;, &quot;addEdge&quot;, &quot;shortestPath&quot;]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
<strong>Output</strong>
[null, 6, -1, null, 6]

<strong>Explanation</strong>
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -&gt; 0 -&gt; 1 -&gt; 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -&gt; 1 -&gt; 3 with a total cost of 2 + 4 = 6.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= edges.length &lt;= n * (n - 1)</code></li>
	<li><code>edges[i].length == edge.length == 3</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub>, from, to, node1, node2 &lt;= n - 1</code></li>
	<li><code>1 &lt;= edgeCost<sub>i</sub>, edgeCost &lt;= 10<sup>6</sup></code></li>
	<li>There are no repeated edges and no self-loops in the graph at any point.</li>
	<li>At most <code>100</code> calls will be made for <code>addEdge</code>.</li>
	<li>At most <code>100</code> calls will be made for <code>shortestPath</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dijsktra's Algorithm

In the initialization function, we first use the adjacency matrix $g$ to store the edge weights of the graph, where $g_{ij}$ represents the edge weight from node $i$ to node $j$. If there is no edge between $i$ and $j$, the value of $g_{ij}$ is $\infty$.

In the `addEdge` function, we update the value of $g_{ij}$ to $edge[2]$.

In the `shortestPath` function, we use Dijsktra's algorithm to find the shortest path from node $node1$ to node $node2$. Here, $dist[i]$ represents the shortest path from node $node1$ to node $i$, and $vis[i]$ indicates whether node $i$ has been visited. We initialize $dist[node1]$ to $0$, and the rest of $dist[i]$ are all $\infty$. Then we iterate $n$ times, each time finding the current unvisited node $t$ such that $dist[t]$ is the smallest. Then we mark node $t$ as visited, and then update the value of $dist[i]$ to $min(dist[i], dist[t] + g_{ti})$. Finally, we return $dist[node2]$. If $dist[node2]$ is $\infty$, it means that there is no path from node $node1$ to node $node2$, so we return $-1$.

The time complexity is $O(n^2 \times q)$, and the space complexity is $O(n^2)$. Where $n$ is the number of nodes, and $q$ is the number of calls to the `shortestPath` function.

<!-- tabs:start -->

#### Python3

```python
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = [[inf] * n for _ in range(n)]
        for f, t, c in edges:
            self.g[f][t] = c

    def addEdge(self, edge: List[int]) -> None:
        f, t, c = edge
        self.g[f][t] = c

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [inf] * self.n
        dist[node1] = 0
        vis = [False] * self.n
        for _ in range(self.n):
            t = -1
            for j in range(self.n):
                if not vis[j] and (t == -1 or dist[t] > dist[j]):
                    t = j
            vis[t] = True
            for j in range(self.n):
                dist[j] = min(dist[j], dist[t] + self.g[t][j])
        return -1 if dist[node2] == inf else dist[node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
