---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2508.Add%20Edges%20to%20Make%20Degrees%20of%20All%20Nodes%20Even/README_EN.md
rating: 2060
source: Weekly Contest 324 Q3
tags:
    - Graph
    - Hash Table
---

<!-- problem:start -->

# [2508. Add Edges to Make Degrees of All Nodes Even](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even)

## Description

<!-- description:start -->

<p>There is an <strong>undirected</strong> graph consisting of <code>n</code> nodes numbered from <code>1</code> to <code>n</code>. You are given the integer <code>n</code> and a <strong>2D</strong> array <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. The graph can be disconnected.</p>

<p>You can add <strong>at most</strong> two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.</p>

<p>Return <code>true</code><em> if it is possible to make the degree of each node in the graph even, otherwise return </em><code>false</code><em>.</em></p>

<p>The degree of a node is the number of edges connected to it.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2508.Add%20Edges%20to%20Make%20Degrees%20of%20All%20Nodes%20Even/images/agraphdrawio.png" style="width: 500px; height: 190px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2508.Add%20Edges%20to%20Make%20Degrees%20of%20All%20Nodes%20Even/images/aagraphdrawio.png" style="width: 400px; height: 120px;" />
<pre>
<strong>Input:</strong> n = 4, edges = [[1,2],[3,4]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The above diagram shows a valid way of adding two edges.</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2508.Add%20Edges%20to%20Make%20Degrees%20of%20All%20Nodes%20Even/images/aaagraphdrawio.png" style="width: 150px; height: 158px;" />
<pre>
<strong>Input:</strong> n = 4, edges = [[1,2],[1,3],[1,4]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to obtain a valid graph with adding at most 2 edges.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Case Analysis

We first build the graph $g$ using `edges`, and then find all nodes with odd degrees, denoted as $vs$.

If the length of $vs$ is $0$, it means all nodes in the graph $g$ have even degrees, so we return `true`.

If the length of $vs$ is $2$, it means there are two nodes with odd degrees in the graph $g$. If we can directly connect these two nodes with an edge, making all nodes in the graph $g$ have even degrees, we return `true`. Otherwise, if we can find a third node $c$ such that we can connect $a$ and $c$, and $b$ and $c$, making all nodes in the graph $g$ have even degrees, we return `true`. Otherwise, we return `false`.

If the length of $vs$ is $4$, we enumerate all possible pairs and check if any combination meets the conditions. If so, we return `true`; otherwise, we return `false`.

In other cases, we return `false`.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$. Where $n$ and $m$ are the number of nodes and edges, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        vs = [i for i, v in g.items() if len(v) & 1]
        if len(vs) == 0:
            return True
        if len(vs) == 2:
            a, b = vs
            if a not in g[b]:
                return True
            return any(a not in g[c] and c not in g[b] for c in range(1, n + 1))
        if len(vs) == 4:
            a, b, c, d = vs
            if a not in g[b] and c not in g[d]:
                return True
            if a not in g[c] and b not in g[d]:
                return True
            if a not in g[d] and b not in g[c]:
                return True
            return False
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
