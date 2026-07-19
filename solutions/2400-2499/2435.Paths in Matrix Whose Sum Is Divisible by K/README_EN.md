---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2435.Paths%20in%20Matrix%20Whose%20Sum%20Is%20Divisible%20by%20K/README_EN.md
rating: 1951
source: Weekly Contest 314 Q4
tags:
    - Array
    - Dynamic Programming
    - Matrix
---

<!-- problem:start -->

# [2435. Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> <code>m x n</code> integer matrix <code>grid</code> and an integer <code>k</code>. You are currently at position <code>(0, 0)</code> and you want to reach position <code>(m - 1, n - 1)</code> moving only <strong>down</strong> or <strong>right</strong>.</p>

<p>Return<em> the number of paths where the sum of the elements on the path is divisible by </em><code>k</code>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2435.Paths%20in%20Matrix%20Whose%20Sum%20Is%20Divisible%20by%20K/images/image-20220813183124-1.png" style="width: 437px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2435.Paths%20in%20Matrix%20Whose%20Sum%20Is%20Divisible%20by%20K/images/image-20220817112930-3.png" style="height: 85px; width: 132px;" />
<pre>
<strong>Input:</strong> grid = [[0,0]], k = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong> The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2435.Paths%20in%20Matrix%20Whose%20Sum%20Is%20Divisible%20by%20K/images/image-20220812224605-3.png" style="width: 257px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
<strong>Output:</strong> 10
<strong>Explanation:</strong> Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We denote the $k$ in the problem as $K$, and let $m$ and $n$ be the number of rows and columns of the matrix $\textit{grid}$, respectively.

Define $f[i][j][k]$ as the number of paths starting from $(0, 0)$, reaching position $(i, j)$, where the sum of elements along the path modulo $K$ equals $k$. Initially, $f[0][0][\textit{grid}[0][0] \bmod K] = 1$. The final answer is $f[m - 1][n - 1][0]$.

We can derive the state transition equation:

$$
f[i][j][k] = f[i - 1][j][(k - \textit{grid}[i][j])\bmod K] + f[i][j - 1][(k - \textit{grid}[i][j])\bmod K]
$$

To avoid issues with negative modulo operations, we can replace $(k - \textit{grid}[i][j])\bmod K$ in the above equation with $((k - \textit{grid}[i][j] \bmod K) + K) \bmod K$.

The answer is $f[m - 1][n - 1][0]$.

The time complexity is $O(m \times n \times K)$ and the space complexity is $O(m \times n \times K)$, where $m$ and $n$ are the number of rows and columns of the matrix $\textit{grid}$, respectively, and $K$ is the integer $k$ from the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfPaths(self, grid: List[List[int]], K: int) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        f = [[[0] * K for _ in range(n)] for _ in range(m)]
        f[0][0][grid[0][0] % K] = 1
        for i in range(m):
            for j in range(n):
                for k in range(K):
                    k0 = ((k - grid[i][j] % K) + K) % K
                    if i:
                        f[i][j][k] += f[i - 1][j][k0]
                    if j:
                        f[i][j][k] += f[i][j - 1][k0]
                    f[i][j][k] %= mod
        return f[m - 1][n - 1][0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
