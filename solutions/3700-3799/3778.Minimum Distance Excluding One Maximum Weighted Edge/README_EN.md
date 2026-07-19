---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3778.Minimum%20Distance%20Excluding%20One%20Maximum%20Weighted%20Edge/README_EN.md
---

<!-- problem:start -->

# [3778. Minimum Distance Excluding One Maximum Weighted Edge 🔒](https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge)

## Description

<!-- description:start -->

<p>You are given a positive integer <code>n</code> and a 2D integer array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code>.</p>

<p>There is a <strong>weighted</strong> <strong>connected</strong> simple undirected graph with <code>n</code> nodes labeled from 0 to <code>n - 1</code>. Each <code>[u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> in <code>edges</code> represents an edge between node <code>u<sub>i</sub></code> and node <code>v<sub>i</sub></code> with <strong>positive</strong> weight <code>w<sub>i</sub></code>.</p>

<p>The <strong>cost</strong> of a path is the <strong>sum</strong> of weights of the edges in the path, <strong>excluding</strong> the edge with the <strong>maximum</strong> weight. If there are multiple edges in the path with the maximum weight, <strong>only</strong> the <strong>first</strong> such edge is excluded.</p>

<p>Return an integer representing the <strong>minimum</strong> <strong>cost</strong> of a path going from node 0 to node <code>n - 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, edges = [[0,1,2],[1,2,7],[2,3,7],[3,4,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one path going from node 0 to node 4: <code>0 -&gt; 1 -&gt; 2 -&gt; 3 -&gt; 4</code>.</p>

<p>The edge weights on this path are 2, 7, 7, and 4.</p>

<p>Excluding the first edge with maximum weight, which is <code>1 -&gt; 2</code>, the cost of this path is <code>2 + 7 + 4 = 13</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,50000]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are two paths going from node 0 to node 2:</p>

<ul>
	<li><code>0 -&gt; 1 -&gt; 2</code></li>
</ul>

<p>The edge weights on this path are 1 and 1.</p>

<p>Excluding the first edge with maximum weight, which is <code>0 -&gt; 1</code>, the cost of this path is 1.</p>

<ul>
	<li><code>0 -&gt; 2</code></li>
</ul>

<p>The only edge weight on this path is 1.</p>

<p>Excluding the first edge with maximum weight, which is <code>0 -&gt; 2</code>, the cost of this path is 0.</p>

<p>The minimum cost is <code>min(1, 0) = 0</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>n - 1 &lt;= edges.length &lt;= 10<sup>9</sup></code></li>
	<li><code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub> &lt; v<sub>i</sub> &lt; n</code></li>
	<li><code>[u<sub>i</sub>, v<sub>i</sub>] != [u<sub>j</sub>, v<sub>j</sub>]</code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= 5 * 10<sup>4</sup></code></li>
	<li>The graph is connected.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dijkstra's Algorithm

The problem is essentially equivalent to finding a path from node $0$ to node $n-1$, where we have one opportunity to treat the weight of a traversed edge as $0$, in order to minimize the sum of path weights.

We first convert $\textit{edges}$ into an adjacency list $\textit{g}$, where $\textit{g}[u]$ stores all edges $(v, w)$ connected to node $u$, indicating that there is an edge with weight $w$ between node $u$ and node $v$.

Next, we use Dijkstra's algorithm to find the shortest path. We define a 2D array $\textit{dist}$, where $\textit{dist}[u][0]$ represents the minimum sum of path weights from node $0$ to node $u$ without using the opportunity to treat an edge weight as $0$; $\textit{dist}[u][1]$ represents the minimum sum of path weights from node $0$ to node $u$ having already used the opportunity to treat an edge weight as $0$.

We use a priority queue $\textit{pq}$ to store pending nodes. Initially, we enqueue $(0, 0, 0)$, indicating that we start from node $0$, with a current path weight sum of $0$, and haven't used the opportunity.

In each iteration, we dequeue the node $(\textit{cur}, u, \textit{used})$ with the minimum path weight sum from the priority queue. If the current path weight sum $\textit{cur}$ is greater than $\textit{dist}[u][\textit{used}]$, we skip this node.

If the current node $u$ is node $n-1$ and we have already used the opportunity $\textit{used} = 1$, we return the current path weight sum $\textit{cur}$.

For each edge $(v, w)$ of node $u$, we calculate the path weight sum to reach node $v$ without using the opportunity: $\textit{nxt} = \textit{cur} + w$. If $\textit{nxt} < \textit{dist}[v][\textit{used}]$, we update $\textit{dist}[v][\textit{used}]$ and enqueue $(\textit{nxt}, v, \textit{used})$.

If we haven't used the opportunity yet $\textit{used} = 0$, we calculate the path weight sum to reach node $v$ when using the opportunity: $\textit{nxt} = \textit{cur}$. If $\textit{nxt} < \textit{dist}[v][1]$, we update $\textit{dist}[v][1]$ and enqueue $(\textit{nxt}, v, 1)$.

After the traversal ends, we return $\textit{dist}[n-1][1]$ as the answer.

The time complexity is $O(m \times \log n)$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of nodes and edges, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCostExcludingMax(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        dist = [[inf] * 2 for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            cur, u, used = heappop(pq)
            if cur > dist[u][used]:
                continue
            if u == n - 1 and used:
                return cur
            for v, w in g[u]:
                nxt = cur + w
                if nxt < dist[v][used]:
                    dist[v][used] = nxt
                    heappush(pq, (nxt, v, used))
                if used == 0:
                    nxt = cur
                    if nxt < dist[v][1]:
                        dist[v][1] = nxt
                        heappush(pq, (nxt, v, 1))
        return dist[n - 1][1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
