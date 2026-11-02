---
comments: true
difficulty: Medium
rating: 1840
source: Weekly Contest 507 Q3
tags:
    - Graph
    - String
    - Shortest Path
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3970. Shortest Path With At Most K Consecutive Identical Characters](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code> representing the number of nodes in a <strong>directed weighted</strong> graph, numbered from 0 to <code>n - 1</code>. This is represented by a 2D integer array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> represents a directed edge from node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code> with weight <code>w<sub>i</sub></code>.</p>

<p>You are also given a string <code>labels</code> of length <code>n</code>, where <code>labels[i]</code> is the character assigned to node <code>i</code>, and an integer <code>k</code>.</p>

<p>Return the <strong>minimum</strong> <strong>total</strong> edge weight of a path from node 0 to node <code>n - 1</code> such that the concatenation of the labels of the nodes along the path contains <strong>at most</strong> <code>k</code> <strong>consecutive</strong> <strong>identical</strong> characters. If no valid path exists, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = &quot;aab&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal valid path from node 0 to node 2 is as follows:</p>

<ul>
	<li>Use <code>edges[2] = [0, 2, 3]</code> to reach node 2 with a weight <code>w<sub>i</sub> = 3</code>.</li>
</ul>
The corresponding concatenation of labels is <code>&quot;ab&quot;</code>, which satisfies at most <code>k = 1</code> consecutive identical characters. Thus, the answer is 3.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = &quot;aab&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal valid path from node 0 to node 2 is as follows:</p>

<ul>
	<li>Use <code>edges[0] = [0, 1, 1]</code> to reach node 1 with weight <code>w<sub>i</sub> = 1</code>.</li>
	<li>Use <code>edges[1] = [1, 2, 1]</code> to reach node 2 with weight <code>w<sub>i</sub> = 1</code>.</li>
</ul>
The corresponding concatenation of labels is <code>&quot;aab&quot;</code>, which satisfies at most <code>k = 2</code> consecutive identical characters. Thus, the answer is 2.</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1]], labels = &quot;aaa&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no valid path from node 0 to node 2 that satisfies at most <code>k = 2</code> consecutive identical characters. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == labels.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>labels</code> consists of lowercase English letters</li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dijkstra

<!-- thinking:start -->

> **Thinking**
>
> Edge weights are nonnegative, so a shortest path from node $0$ to $n - 1$ is a Dijkstra problem, except the concatenated labels may contain at most $k$ identical characters in a row. The unconstrained shortest path can be exactly the one that overruns a run, while a costlier path stays valid by changing labels along the way. With $n$ and the number of edges both up to $5 \times 10^4$, enumerating paths is not viable.
>
> Reaching the same node with different trailing run lengths leaves different room for another identical label, so one distance per node drops legal transitions. The run depends only on the current label and how long it has already lasted: the next label increments it when equal and resets it to $1$ otherwise, states past $k$ are dropped, and the start label itself counts as a run of $1$.
>
> The state is $(u, \textit{cur})$, and $\textit{dist}[u][\textit{cur}]$ stores the minimum edge-weight sum to reach it. Nonnegative weights let a binary heap expand states by distance, and the first time the destination leaves the heap is the answer.

<!-- thinking:end -->

Let $\textit{dist}[u][\textit{cur}]$ be the minimum total edge weight of a path from node $0$ to node $u$ whose trailing run of identical labels has length $\textit{cur}$.

Build an adjacency list from $\textit{edges}$. The start label is a run of length $1$, so $\textit{dist}[0][1] = 0$. Push $(0, 0, 1)$ into a min-heap. The triple is the distance, the node, and the run length.

Pop the triple $(d, u, \textit{cur})$ with the smallest distance. If $u = n - 1$, nonnegative weights make this the best way to reach the destination, so return $d$. If $d > \textit{dist}[u][\textit{cur}]$, the state is stale and is skipped.

Otherwise scan each outgoing edge $(v, w)$. The next run length is $\textit{nxt} = 1$ when the labels differ and $\textit{nxt} = \textit{cur} + 1$ when they match. The new distance is $nd = d + w$. Update $\textit{dist}[v][\textit{nxt}]$ and push the state only when $\textit{nxt} \le k$ and $nd < \textit{dist}[v][\textit{nxt}]$.

If the heap empties before the destination is reached, return $-1$.

The time complexity is $O(k(n + m) \log (nk))$, and the space complexity is $O(nk + m)$, where $n$ and $m$ are the number of nodes and edges.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, cur = heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u][cur]:
                continue
            for v, w in g[u]:
                nxt = 1 if labels[v] != labels[u] else cur + 1
                nd = d + w
                if nxt <= k and nd < dist[v][nxt]:
                    dist[v][nxt] = nd
                    heappush(pq, (nd, v, nxt))
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
