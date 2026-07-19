---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2608.Shortest%20Cycle%20in%20a%20Graph/README_EN.md
rating: 1904
source: Biweekly Contest 101 Q4
tags:
    - Breadth-First Search
    - Graph
---

<!-- problem:start -->

# [2608. Shortest Cycle in a Graph](https://leetcode.com/problems/shortest-cycle-in-a-graph)

## Description

<!-- description:start -->

<p>There is a <strong>bi-directional </strong>graph with <code>n</code> vertices, where each vertex is labeled from <code>0</code> to <code>n - 1</code>. The edges in the graph are represented by a given 2D integer array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> denotes an edge between vertex <code>u<sub>i</sub></code> and vertex <code>v<sub>i</sub></code>. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.</p>

<p>Return <em>the length of the <strong>shortest </strong>cycle in the graph</em>. If no cycle exists, return <code>-1</code>.</p>

<p>A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2608.Shortest%20Cycle%20in%20a%20Graph/images/cropped.png" style="width: 387px; height: 331px;" />
<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The cycle with the smallest length is : 0 -&gt; 1 -&gt; 2 -&gt; 0 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2608.Shortest%20Cycle%20in%20a%20Graph/images/croppedagin.png" style="width: 307px; height: 307px;" />
<pre>
<strong>Input:</strong> n = 4, edges = [[0,1],[0,2]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no cycles in this graph.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= edges.length &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate edges + BFS

We first construct the adjacency list $g$ of the graph according to the array $edges$, where $g[u]$ represents all the adjacent vertices of vertex $u$.

Then we enumerate the two-directional edge $(u, v)$, if the path from vertex $u$ to vertex $v$ still exists after deleting this edge, then the length of the shortest cycle containing this edge is $dist[v] + 1$, where $dist[v]$ represents the shortest path length from vertex $u$ to vertex $v$. We take the minimum of all these cycles.

The time complexity is $O(m^2)$ and the space complexity is $O(m + n)$, where $m$ and $n$ are the length of the array $edges$ and the number of vertices.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        def bfs(u: int, v: int) -> int:
            dist = [inf] * n
            dist[u] = 0
            q = deque([u])
            while q:
                i = q.popleft()
                for j in g[i]:
                    if (i, j) != (u, v) and (j, i) != (u, v) and dist[j] == inf:
                        dist[j] = dist[i] + 1
                        q.append(j)
            return dist[v] + 1

        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        ans = min(bfs(u, v) for u, v in edges)
        return ans if ans < inf else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Enumerate points + BFS

Similar to Solution 1, we first construct the adjacency list $g$ of the graph according to the array $edges$, where $g[u]$ represents all the adjacent vertices of vertex $u$.

Then we enumerate the vertex $u$, if there are two paths from vertex $u$ to vertex $v$, then we currently find a cycle, the length is the sum of the length of the two paths. We take the minimum of all these cycles.

The time complexity is $O(m \times n)$ and the space complexity is $O(m + n)$, where $m$ and $n$ are the length of the array $edges$ and the number of vertices.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        def bfs(u: int) -> int:
            dist = [-1] * n
            dist[u] = 0
            q = deque([(u, -1)])
            ans = inf
            while q:
                u, fa = q.popleft()
                for v in g[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u] + 1
                        q.append((v, u))
                    elif v != fa:
                        ans = min(ans, dist[u] + dist[v] + 1)
            return ans

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
