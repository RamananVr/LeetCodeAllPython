---
comments: true
difficulty: Medium
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Graph
    - Graph Coloring
    - Bipartite Graph
---

<!-- problem:start -->

# [886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition)

## Description

<!-- description:start -->

<p>We want to split a group of <code>n</code> people (labeled from <code>1</code> to <code>n</code>) into two groups of <strong>any size</strong>. Each person may dislike some other people, and they should not go into the same group.</p>

<p>Given the integer <code>n</code> and the array <code>dislikes</code> where <code>dislikes[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that the person labeled <code>a<sub>i</sub></code> does not like the person labeled <code>b<sub>i</sub></code>, return <code>true</code> <em>if it is possible to split everyone into two groups in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, dislikes = [[1,2],[1,3],[2,4]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The first group has [1,4], and the second group has [2,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, dislikes = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> false
<strong>Explanation:</strong> We need at least 3 groups to divide them. We cannot put them in two groups.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>0 &lt;= dislikes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>dislikes[i].length == 2</code></li>
	<li><code>1 &lt;= a<sub>i</sub> &lt; b<sub>i</sub> &lt;= n</code></li>
	<li>All the pairs of <code>dislikes</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> People who dislike each other cannot share a group, i.e. the dislike graph must be bipartite. $n\le 2000$, so a coloring DFS is enough: neighbors get opposite colors.
>
> Color each unseen node $1$ and recurse with $3-c$. If every component succeeds, a partition exists.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(i, c):
            color[i] = c
            for j in g[i]:
                if color[j] == c:
                    return False
                if color[j] == 0 and not dfs(j, 3 - c):
                    return False
            return True

        g = defaultdict(list)
        color = [0] * n
        for a, b in dislikes:
            a, b = a - 1, b - 1
            g[a].append(b)
            g[b].append(a)
        return all(c or dfs(i, 1) for i, c in enumerate(color))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 already colors the graph with an explicit stack. Union-find does not store colors. It merges people who must share a group: everyone disliked by one person should share a group, and none of them may share that person's group. If that person is already in the same set as a neighbor, the partition fails; otherwise those neighbors are merged under one representative.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        g = defaultdict(list)
        for a, b in dislikes:
            a, b = a - 1, b - 1
            g[a].append(b)
            g[b].append(a)
        p = list(range(n))
        for i in range(n):
            for j in g[i]:
                if find(i) == find(j):
                    return False
                p[find(j)] = find(g[i][0])
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Explicit-Stack Coloring

<!-- thinking:start -->

> **Thinking**
>
> People who dislike each other cannot share a group, so the dislike graph must be bipartite. With $n\le 2000$, recursion along a chain of dislikes uses a call depth equal to the number of people and overflows Python once the chain reaches length $1000$. A graph is bipartite exactly when two colors can cover it with every edge joining different colors. A stack therefore expands each component: an uncolored person is colored $1$ and pushed, a popped person fails the search when a neighbor already has the same color, and an uncolored neighbor is colored $3$ minus the current color and pushed. A partition exists when every component is colored.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in dislikes:
            a, b = a - 1, b - 1
            g[a].append(b)
            g[b].append(a)
        color = [0] * n
        for start in range(n):
            if color[start]:
                continue
            color[start] = 1
            stk = [start]
            while stk:
                i = stk.pop()
                for j in g[i]:
                    if color[j] == color[i]:
                        return False
                    if color[j] == 0:
                        color[j] = 3 - color[i]
                        stk.append(j)
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
