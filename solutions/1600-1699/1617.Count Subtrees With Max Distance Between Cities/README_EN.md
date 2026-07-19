---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1617.Count%20Subtrees%20With%20Max%20Distance%20Between%20Cities/README_EN.md
rating: 2308
source: Weekly Contest 210 Q4
tags:
    - Bit Manipulation
    - Tree
    - Dynamic Programming
    - Bitmask
    - Enumeration
---

<!-- problem:start -->

# [1617. Count Subtrees With Max Distance Between Cities](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities)

## Description

<!-- description:start -->

<p>There are <code>n</code> cities numbered from <code>1</code> to <code>n</code>. You are given an array <code>edges</code> of size <code>n-1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> represents a bidirectional edge between cities <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>. There exists a unique path between each pair of cities. In other words, the cities form a <strong>tree</strong>.</p>

<p>A <strong>subtree</strong> is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.</p>

<p>For each <code>d</code> from <code>1</code> to <code>n-1</code>, find the number of subtrees in which the <strong>maximum distance</strong> between any two cities in the subtree is equal to <code>d</code>.</p>

<p>Return <em>an array of size</em> <code>n-1</code> <em>where the </em><code>d<sup>th</sup></code><em> </em><em>element <strong>(1-indexed)</strong> is the number of subtrees in which the <strong>maximum distance</strong> between any two cities is equal to </em><code>d</code>.</p>

<p><strong>Notice</strong>&nbsp;that&nbsp;the <strong>distance</strong> between the two cities is the number of edges in the path between them.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1617.Count%20Subtrees%20With%20Max%20Distance%20Between%20Cities/images/p1.png" style="width: 161px; height: 181px;" /></strong></p>

<pre>

<strong>Input:</strong> n = 4, edges = [[1,2],[2,3],[2,4]]

<strong>Output:</strong> [3,4,0]

<strong>Explanation:

</strong>The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.

The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.

No subtree has two nodes where the max distance between them is 3.

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> n = 2, edges = [[1,2]]

<strong>Output:</strong> [1]

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>

<strong>Input:</strong> n = 3, edges = [[1,2],[2,3]]

<strong>Output:</strong> [2,1]

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>2 &lt;= n &lt;= 15</code></li>

    <li><code>edges.length == n-1</code></li>

    <li><code>edges[i].length == 2</code></li>

    <li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>

    <li>All pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are distinct.</li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSubgraphsForEachDiameter(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        def dfs(u: int, d: int = 0):
            nonlocal mx, nxt, msk
            if mx < d:
                mx, nxt = d, u
            msk ^= 1 << u
            for v in g[u]:
                if msk >> v & 1:
                    dfs(v, d + 1)

        g = defaultdict(list)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
        ans = [0] * (n - 1)
        nxt = mx = 0
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            msk, mx = mask, 0
            cur = msk.bit_length() - 1
            dfs(cur)
            if msk == 0:
                msk, mx = mask, 0
                dfs(nxt)
                ans[mx - 1] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSubgraphsForEachDiameter(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        def bfs(u: int) -> int:
            d = -1
            q = deque([u])
            nonlocal msk, nxt
            msk ^= 1 << u
            while q:
                d += 1
                for _ in range(len(q)):
                    nxt = u = q.popleft()
                    for v in g[u]:
                        if msk >> v & 1:
                            msk ^= 1 << v
                            q.append(v)
            return d

        g = defaultdict(list)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
        ans = [0] * (n - 1)
        nxt = 0
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            msk = mask
            cur = msk.bit_length() - 1
            bfs(cur)
            if msk == 0:
                msk = mask
                mx = bfs(nxt)
                ans[mx - 1] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
