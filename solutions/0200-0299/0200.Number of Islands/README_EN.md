---
comments: true
difficulty: Medium
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Array
    - Matrix
---

<!-- problem:start -->

# [200. Number of Islands](https://leetcode.com/problems/number-of-islands)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

<!-- thinking:start -->

> **Thinking**
>
> Counting every cell with value $1$ as its own island would double-count 4-connected land. With $m,n \le 300$, a full scan is acceptable, but each connected component must be cleared in one search.
>
> Adjacent land cells form one component, so a DFS from any unseen land cell covers the whole island. We scan the grid, start DFS at each $1$, rewrite visited land to $0$, and increment the answer once per search.

<!-- thinking:end -->

We can use depth-first search (DFS) to traverse each island. We iterate through each cell $(i, j)$ in the grid. If the cell's value is '1', it means we have found a new island. We can start a DFS from this cell, marking all connected land cells as '0' to avoid duplicate counting. Each time we find a new island, we increment the island count by 1.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns in the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)

        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: BFS

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 already clears each component with an explicit stack. The same 4-connectivity can be expanded with a queue.
>
> The scan order matches Solution 1. The extra space is still the size of the frontier.

<!-- thinking:end -->

We can also use breadth-first search (BFS) to traverse each island. We iterate through each cell $(i, j)$ in the grid. If the cell's value is '1', it means we have found a new island. We can start a BFS from this cell, marking all connected land cells as '0' to avoid duplicate counting. Each time we find a new island, we increment the island count by 1.

The specific BFS process is as follows:

1. Enqueue the starting cell $(i, j)$ and mark its value as '0'.
2. While the queue is not empty, perform the following operations:
    - Dequeue a cell $p$.
    - Iterate through the four adjacent cells $(x, y)$ of $p$. If $(x, y)$ is within the grid bounds and its value is '1', enqueue it and mark its value as '0'.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns in the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            grid[i][j] = '0'
            q = deque([(i, j)])
            while q:
                i, j = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        q.append((x, y))
                        grid[x][y] = 0

        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Union-Find

<!-- thinking:start -->

> **Thinking**
>
> If we want adjacency as an explicit partition, treat each land cell as a union-find node and union it with neighboring land.
>
> The number of islands is the number of components after the scan. Unions and finds are nearly linear; space remains proportional to the grid.

<!-- thinking:end -->

We can use the Union-Find data structure to solve this problem. We traverse each cell $(i, j)$ in the grid, and if the cell's value is '1', we merge it with adjacent land cells. Finally, we count the number of distinct root nodes in the Union-Find structure, which represents the number of islands.

The time complexity is $O(m \times n \times \log (m \times n))$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns in the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        dirs = (0, 1, 0)
        m, n = len(grid), len(grid[0])
        p = list(range(m * n))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for a, b in pairwise(dirs):
                        x, y = i + a, j + b
                        if x < m and y < n and grid[x][y] == '1':
                            p[find(i * n + j)] = find(x * n + y)
        return sum(
            grid[i][j] == '1' and i * n + j == find(i * n + j)
            for i in range(m)
            for j in range(n)
        )
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 4: Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> Counting every cell with value $1$ as its own island would double-count 4-connected land. With $m,n \le 300$, a full scan is acceptable, but each component must be cleared in one search.
>
> Recursing along a snake of $1000$ land cells overflows the call stack, and a $300\times 300$ grid can hold that snake.
>
> Clearing an island does not need a return value. It only rewrites 4-connected $1$s to $0$.
>
> When a $1$ is found, push it onto an explicit stack. Pop a cell and push each neighboring $1$ after marking it. Each time a search starts, add one to the answer.

<!-- thinking:end -->

Scan every cell. When the value is `'1'`, flood the island with an explicit stack, rewrite connected land to `'0'`, and add one to the answer.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns in the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def flood(i: int, j: int):
            stk = [(i, j)]
            grid[i][j] = '0'
            while stk:
                i, j = stk.pop()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        grid[x][y] = '0'
                        stk.append((x, y))

        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    flood(i, j)
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
