---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3112.Minimum%20Time%20to%20Visit%20Disappearing%20Nodes/README_EN.md
rating: 1756
source: Biweekly Contest 128 Q3
tags:
    - Graph
    - Array
    - Shortest Path
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3112. Minimum Time to Visit Disappearing Nodes](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes)

## Description

<!-- description:start -->

<p>There is an undirected graph of <code>n</code> nodes. You are given a 2D array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, length<sub>i</sub>]</code> describes an edge between node <code>u<sub>i</sub></code> and node <code>v<sub>i</sub></code> with a traversal time of <code>length<sub>i</sub></code> units.</p>

<p>Additionally, you are given an array <code>disappear</code>, where <code>disappear[i]</code> denotes the time when the node <code>i</code> disappears from the graph and you won&#39;t be able to visit it.</p>

<p><strong>Note</strong>&nbsp;that the graph might be <em>disconnected</em> and might contain <em>multiple edges</em>.</p>

<p>Return the array <code>answer</code>, with <code>answer[i]</code> denoting the <strong>minimum</strong> units of time required to reach node <code>i</code> from node 0. If node <code>i</code> is <strong>unreachable</strong> from node 0 then <code>answer[i]</code> is <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,-1,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3100-3199/3112.Minimum%20Time%20to%20Visit%20Disappearing%20Nodes/images/output-onlinepngtools.png" style="width: 350px; height: 210px;" /></p>

<p>We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears.</p>

<ul>
	<li>For node 0, we don&#39;t need any time as it is our starting point.</li>
	<li>For node 1, we need at least 2 units of time to traverse <code>edges[0]</code>. Unfortunately, it disappears at that moment, so we won&#39;t be able to visit it.</li>
	<li>For node 2, we need at least 4 units of time to traverse <code>edges[2]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3100-3199/3112.Minimum%20Time%20to%20Visit%20Disappearing%20Nodes/images/output-onlinepngtools-1.png" style="width: 350px; height: 210px;" /></p>

<p>We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears.</p>

<ul>
	<li>For node 0, we don&#39;t need any time as it is the starting point.</li>
	<li>For node 1, we need at least 2 units of time to traverse <code>edges[0]</code>.</li>
	<li>For node 2, we need at least 3 units of time to traverse <code>edges[0]</code> and <code>edges[1]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, edges = [[0,1,1]], disappear = [1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,-1]</span></p>

<p><strong>Explanation:</strong></p>

<p>Exactly when we reach node 1, it disappears.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>, length<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>1 &lt;= length<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>disappear.length == n</code></li>
	<li><code>1 &lt;= disappear[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Heap-Optimized Dijkstra

First, we create an adjacency list $\textit{g}$ to store the edges of the graph. Then, we create an array $\textit{dist}$ to store the shortest distances from node $0$ to other nodes. Initialize $\textit{dist}[0] = 0$, and the distances for the rest of the nodes are initialized to infinity.

Next, we use the Dijkstra algorithm to calculate the shortest distances from node $0$ to other nodes. The specific steps are as follows:

1. Create a priority queue $\textit{pq}$ to store the distances and node numbers. Initially, add node $0$ to the queue with a distance of $0$.
2. Remove a node $u$ from the queue. If the distance $du$ of $u$ is greater than $\textit{dist}[u]$, it means $u$ has already been updated, so we skip it directly.
3. Iterate through all neighbor nodes $v$ of node $u$. If $\textit{dist}[v] > \textit{dist}[u] + w$ and $\textit{dist}[u] + w < \textit{disappear}[v]$, then update $\textit{dist}[v] = \textit{dist}[u] + w$ and add node $v$ to the queue.
4. Repeat steps 2 and 3 until the queue is empty.

Finally, we iterate through the $\textit{dist}$ array. If $\textit{dist}[i] < \textit{disappear}[i]$, then $\textit{answer}[i] = \textit{dist}[i]$; otherwise, $\textit{answer}[i] = -1$.

The time complexity is $O(m \times \log m)$, and the space complexity is $O(m)$. Here, $m$ is the number of edges.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            du, u = heappop(pq)
            if du > dist[u]:
                continue
            for v, w in g[u]:
                if dist[v] > dist[u] + w and dist[u] + w < disappear[v]:
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        return [a if a < b else -1 for a, b in zip(dist, disappear)]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
