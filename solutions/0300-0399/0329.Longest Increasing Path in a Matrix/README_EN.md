---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0329.Longest%20Increasing%20Path%20in%20a%20Matrix/README_EN.md
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

# [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> integers <code>matrix</code>, return <em>the length of the longest increasing path in </em><code>matrix</code>.</p>

<p>From each cell, you can either move in four directions: left, right, up, or down. You <strong>may not</strong> move <strong>diagonally</strong> or move <strong>outside the boundary</strong> (i.e., wrap-around is not allowed).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0329.Longest%20Increasing%20Path%20in%20a%20Matrix/images/grid1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[9,9,4],[6,6,8],[2,1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing path is <code>[1, 2, 6, 9]</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0329.Longest%20Increasing%20Path%20in%20a%20Matrix/images/tmp-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> matrix = [[3,4,5],[3,2,6],[2,2,1]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest increasing path is <code>[3, 4, 5, 6]</code>. Moving diagonally is not allowed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We design a function $dfs(i, j)$, which represents the length of the longest increasing path that can be obtained starting from the coordinate $(i, j)$ in the matrix. The answer is $\max_{i, j} \textit{dfs}(i, j)$.

The execution logic of the function $dfs(i, j)$ is as follows:

- If $(i, j)$ has been visited, directly return $\textit{f}(i, j)$;
- Otherwise, search $(i, j)$, search the coordinates $(x, y)$ in four directions. If $0 \le x < m, 0 \le y < n$ and $matrix[x][y] > matrix[i][j]$, then search $(x, y)$. After the search is over, update $\textit{f}(i, j)$ to $\textit{f}(i, j) = \max(\textit{f}(i, j), \textit{f}(x, y) + 1)$. Finally, return $\textit{f}(i, j)$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

Similar problems:

- [2328. Number of Increasing Paths in a Grid](https://github.com/doocs/leetcode/blob/main/solution/2300-2399/2328.Number%20of%20Increasing%20Paths%20in%20a%20Grid/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            ans = 0
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, dfs(x, y))
            return ans + 1

        m, n = len(matrix), len(matrix[0])
        return max(dfs(i, j) for i in range(m) for j in range(n))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
