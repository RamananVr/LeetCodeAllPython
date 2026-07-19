---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2328.Number%20of%20Increasing%20Paths%20in%20a%20Grid/README_EN.md
rating: 2001
source: Weekly Contest 300 Q4
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
    - Topological Sort
    - Memoization
    - Array
    - Dynamic Programming
    - Matrix
---

<!-- problem:start -->

# [2328. Number of Increasing Paths in a Grid](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> integer matrix <code>grid</code>, where you can move from a cell to any adjacent cell in all <code>4</code> directions.</p>

<p>Return <em>the number of <strong>strictly</strong> <strong>increasing</strong> paths in the grid such that you can start from <strong>any</strong> cell and end at <strong>any</strong> cell. </em>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>Two paths are considered different if they do not have exactly the same sequence of visited cells.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2300-2399/2328.Number%20of%20Increasing%20Paths%20in%20a%20Grid/images/griddrawio-4.png" style="width: 181px; height: 121px;" />
<pre>
<strong>Input:</strong> grid = [[1,1],[3,4]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -&gt; 3], [1 -&gt; 4], [3 -&gt; 4].
- Paths with length 3: [1 -&gt; 3 -&gt; 4].
The total number of paths is 4 + 3 + 1 = 8.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1],[2]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -&gt; 2].
The total number of paths is 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + Memorization

We design a function $dfs(i, j)$, which represents the number of strictly increasing paths that can be reached from the grid graph starting at the $i$-th row and $j$-th column. Then the answer is $\sum_{i=0}^{m-1} \sum_{j=0}^{n-1} dfs(i, j)$. In the search process, we can use a two-dimensional array $f$ to record the calculated results to avoid repeated calculation.

The calculation process of the function $dfs(i, j)$ is as follows:

- If $f[i][j]$ is not $0$, it means that it has been calculated, and $f[i][j]$ is returned directly;
- Otherwise, we initialize $f[i][j] = 1$, and then enumerate the four directions of $(i, j)$. If the grid $(x, y)$ in a certain direction satisfies $0 \leq x \lt m$, $0 \leq y \lt n$, and $grid[i][j] \lt grid[x][y]$, we can start from the grid $(i, j)$ to the grid $(x, y)$, and the number on the path is strictly increasing, so $f[i][j] += dfs(x, y)$.

Finally, we return $f[i][j]$.

The answer is $\sum_{i=0}^{m-1} \sum_{j=0}^{n-1} dfs(i, j)$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns in the grid graph, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            ans = 1
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[i][j] < grid[x][y]:
                    ans = (ans + dfs(x, y)) % mod
            return ans

        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
