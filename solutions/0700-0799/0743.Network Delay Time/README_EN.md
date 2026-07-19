---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0743.Network%20Delay%20Time/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
    - Shortest Path
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [743. Network Delay Time](https://leetcode.com/problems/network-delay-time)

## Description

<!-- description:start -->

<p>You are given a network of <code>n</code> nodes, labeled from <code>1</code> to <code>n</code>. You are also given <code>times</code>, a list of travel times as directed edges <code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>, where <code>u<sub>i</sub></code> is the source node, <code>v<sub>i</sub></code> is the target node, and <code>w<sub>i</sub></code> is the time it takes for a signal to travel from source to target.</p>

<p>We will send a signal from a given node <code>k</code>. Return <em>the <strong>minimum</strong> time it takes for all the</em> <code>n</code> <em>nodes to receive the signal</em>. If it is impossible for all the <code>n</code> nodes to receive the signal, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0743.Network%20Delay%20Time/images/931_example_1.png" style="width: 217px; height: 239px;" />
<pre>
<strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= times.length &lt;= 6000</code></li>
	<li><code>times[i].length == 3</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 100</code></li>
	<li>All the pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are <strong>unique</strong>. (i.e., no multiple edges.)</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Naive Dijkstra Algorithm

We define $\textit{g}[u][v]$ to represent the edge weight from node $u$ to node $v$. If there is no edge between node $u$ and node $v$, then $\textit{g}[u][v] = +\infty$.

We maintain an array $\textit{dist}$, where $\textit{dist}[i]$ represents the shortest path length from node $k$ to node $i$. Initially, we set all $\textit{dist}[i]$ to $+\infty$, except for $\textit{dist}[k - 1] = 0$. We define an array $\textit{vis}$, where $\textit{vis}[i]$ indicates whether node $i$ has been visited. Initially, we set all $\textit{vis}[i]$ to $\text{false}$.

Each time, we find the unvisited node $t$ with the smallest distance, and then perform relaxation operations centered on node $t$. For each node $j$, if $\textit{dist}[j] > \textit{dist}[t] + \textit{g}[t][j]$, we update $\textit{dist}[j] = \textit{dist}[t] + \textit{g}[t][j]$.

Finally, we return the maximum value in $\textit{dist}$ as the answer. If the answer is $+\infty$, it means there are unreachable nodes, and we return $-1$.

The time complexity is $O(n^2 + m)$, and the space complexity is $O(n^2)$. Here, $n$ and $m$ are the number of nodes and edges, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[inf] * n for _ in range(n)]
        for u, v, w in times:
            g[u - 1][v - 1] = w
        dist = [inf] * n
        dist[k - 1] = 0
        vis = [False] * n
        for _ in range(n):
            t = -1
            for j in range(n):
                if not vis[j] and (t == -1 or dist[t] > dist[j]):
                    t = j
            vis[t] = True
            for j in range(n):
                dist[j] = min(dist[j], dist[t] + g[t][j])
        ans = max(dist)
        return -1 if ans == inf else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Heap-Optimized Dijkstra Algorithm

We can use a priority queue (heap) to optimize the naive Dijkstra algorithm.

We define $\textit{g}[u]$ to represent all adjacent edges of node $u$, and $\textit{dist}[u]$ to represent the shortest path length from node $k$ to node $u$. Initially, we set all $\textit{dist}[u]$ to $+\infty$, except for $\textit{dist}[k - 1] = 0$.

We define a priority queue $\textit{pq}$, where each element is $(\textit{d}, u)$, representing the distance $\textit{d}$ from node $u$ to node $k$. Each time, we take out the node $(\textit{d}, u)$ with the smallest distance from $\textit{pq}$. If $\textit{d} > $\textit{dist}[u]$, we skip this node. Otherwise, we traverse all adjacent edges of node $u$. For each adjacent edge $(v, w)$, if $\textit{dist}[v] > \textit{dist}[u] + w$, we update $\textit{dist}[v] = \textit{dist}[u] + w$ and add $(\textit{dist}[v], v)$ to $\textit{pq}$.

Finally, we return the maximum value in $\textit{dist}$ as the answer. If the answer is $+\infty$, it means there are unreachable nodes, and we return $-1$.

The time complexity is $O(m \times \log m + n)$, and the space complexity is $O(n + m)$. Here, $n$ and $m$ are the number of nodes and edges, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u - 1].append((v - 1, w))
        dist = [inf] * n
        dist[k - 1] = 0
        pq = [(0, k - 1)]
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if (nd := d + w) < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))
        ans = max(dist)
        return -1 if ans == inf else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
