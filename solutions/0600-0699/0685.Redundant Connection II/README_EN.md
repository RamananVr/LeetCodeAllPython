---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0685.Redundant%20Connection%20II/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Graph
---

<!-- problem:start -->

# [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii)

## Description

<!-- description:start -->

<p>In this problem, a rooted tree is a <b>directed</b> graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.</p>

<p>The given input is a directed graph that started as a rooted tree with <code>n</code> nodes (with distinct values from <code>1</code> to <code>n</code>), with one additional directed edge added. The added edge has two different vertices chosen from <code>1</code> to <code>n</code>, and was not an edge that already existed.</p>

<p>The resulting graph is given as a 2D-array of <code>edges</code>. Each element of <code>edges</code> is a pair <code>[u<sub>i</sub>, v<sub>i</sub>]</code> that represents a <b>directed</b> edge connecting nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>, where <code>u<sub>i</sub></code> is a parent of child <code>v<sub>i</sub></code>.</p>

<p>Return <em>an edge that can be removed so that the resulting graph is a rooted tree of</em> <code>n</code> <em>nodes</em>. If there are multiple answers, return the answer that occurs last in the given 2D-array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0685.Redundant%20Connection%20II/images/graph1.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> [2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0685.Redundant%20Connection%20II/images/graph2.jpg" style="width: 222px; height: 382px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
<strong>Output:</strong> [4,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Union-Find

According to the problem description, for a rooted tree, the in-degree of the root node is $0$, and the in-degree of other nodes is $1$. After adding an edge to the tree, there can be the following three scenarios:

1. The added edge points to a non-root node, and the in-degree of that node becomes $2$. In this case, there is no directed cycle in the graph:

    ```plaintext
       1
      / \
     v   v
     2-->3
    ```

2. The added edge points to a non-root node, and the in-degree of that node becomes $2$. In this case, there is a directed cycle in the graph:

    ```plaintext
       1
       |
       v
       2 <--> 3
    ```

3. The added edge points to the root node, and the in-degree of the root node becomes $1$. In this case, there is a directed cycle in the graph, but there are no nodes with an in-degree of $2$.

    ```plaintext
        1
        /^
       v  \
       2-->3
    ```

Therefore, we first calculate the in-degree of each node. If there exists a node with an in-degree of $2$, we identify the two edges corresponding to that node, denoted as $\textit{dup}[0]$ and $\textit{dup}[1]$. If deleting $\textit{dup}[1]$ results in the remaining edges not forming a tree, then $\textit{dup}[0]$ is the edge that needs to be deleted; otherwise, $\textit{dup}[1]$ is the edge that needs to be deleted.

If there are no nodes with an in-degree of $2$, we traverse the array $\textit{edges}$. For each edge $(u, v)$, we use the union-find data structure to maintain connectivity between nodes. If $u$ and $v$ are already connected, it indicates that there is a directed cycle in the graph, and the current edge is the one that needs to be deleted.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of edges.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(edges)
        ind = [0] * n
        for _, v in edges:
            ind[v - 1] += 1
        dup = [i for i, (_, v) in enumerate(edges) if ind[v - 1] == 2]
        p = list(range(n))
        if dup:
            for i, (u, v) in enumerate(edges):
                if i == dup[1]:
                    continue
                pu, pv = find(u - 1), find(v - 1)
                if pu == pv:
                    return edges[dup[0]]
                p[pu] = pv
            return edges[dup[1]]
        for i, (u, v) in enumerate(edges):
            pu, pv = find(u - 1), find(v - 1)
            if pu == pv:
                return edges[i]
            p[pu] = pv
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Union-Find (Template Approach)

Here is a template approach using Union-Find for your reference.

The time complexity is $O(n \alpha(n))$, and the space complexity is $O(n)$. Here, $n$ is the number of edges, and $\alpha(n)$ is the inverse Ackermann function, which can be considered a very small constant.

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    __slots__ = "p", "size"

    def __init__(self, n: int):
        self.p: List[int] = list(range(n))
        self.size: List[int] = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ind = [0] * n
        for _, v in edges:
            ind[v - 1] += 1
        dup = [i for i, (_, v) in enumerate(edges) if ind[v - 1] == 2]
        uf = UnionFind(n)
        if dup:
            for i, (u, v) in enumerate(edges):
                if i == dup[1]:
                    continue
                if not uf.union(u - 1, v - 1):
                    return edges[dup[0]]
            return edges[dup[1]]
        for i, (u, v) in enumerate(edges):
            if not uf.union(u - 1, v - 1):
                return edges[i]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
