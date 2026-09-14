---
comments: true
difficulty: Medium
rating: 1615
source: Weekly Contest 130 Q4
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Array
    - Matrix
---

<!-- problem:start -->

# [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>, where <code>0</code> represents a sea cell and <code>1</code> represents a land cell.</p>

<p>A <strong>move</strong> consists of walking from one land cell to another adjacent (<strong>4-directionally</strong>) land cell or walking off the boundary of the <code>grid</code>.</p>

<p>Return <em>the number of land cells in</em> <code>grid</code> <em>for which we cannot walk off the boundary of the grid in any number of <strong>moves</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1020.Number%20of%20Enclaves/images/enclaves1.jpg" style="width: 333px; height: 333px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1020.Number%20of%20Enclaves/images/enclaves2.jpg" style="width: 333px; height: 333px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All 1s are either on the boundary or can reach the boundary.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Testing whether each land cell can reach the border repeats searches over the same grid; $m,n\le 500$ makes that wasteful. Enclaves are land that cannot reach the border, so they are the complement of border-connected land.
>
> Flooding from every $1$ on the four borders removes all land that can leave. The remaining ones cannot.
>
> DFS performs the flood; the answer is the number of $1$s left.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int):
            grid[i][j] = 0
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        for j in range(n):
            if grid[0][j]:
                dfs(0, j)
            if grid[m - 1][j]:
                dfs(m - 1, j)
        for i in range(m):
            if grid[i][0]:
                dfs(i, 0)
            if grid[i][n - 1]:
                dfs(i, n - 1)
        return sum(sum(row) for row in grid)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> DFS may recurse on the order of $2.5\times 10^5$ cells. Connectivity does not depend on search order.
>
> A queue of border land cells runs the same flood in BFS, clearing reachable cells and counting what remains.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    q.append((i, j))
                    grid[i][j] = 0
        dirs = (-1, 0, 1, 0, -1)
        while q:
            i, j = q.popleft()
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y]:
                    q.append((x, y))
                    grid[x][y] = 0
        return sum(v for row in grid for v in row)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3

<!-- thinking:start -->

> **Thinking**
>
> Search still uses a stack or queue proportional to the component size. The same connectivity can be recorded with union-find: adjacent land is united, and every border land is united with a dummy exterior node.
>
> Cells that stay land and are not in the exterior component are enclaves, so we count those sizes.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.size[pa] > self.size[pb]:
                self.p[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.p[pa] = pb
                self.size[pb] += self.size[pa]

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n + 1)
        dirs = (-1, 0, 1, 0, -1)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        uf.union(i * n + j, m * n)
                    else:
                        for a, b in pairwise(dirs):
                            x, y = i + a, j + b
                            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y]:
                                uf.union(i * n + j, x * n + y)
        return sum(
            grid[i][j] == 1 and uf.find(i * n + j) != uf.find(m * n)
            for i in range(m)
            for j in range(n)
        )
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
