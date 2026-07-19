---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2906.Construct%20Product%20Matrix/README_EN.md
rating: 2074
source: Weekly Contest 367 Q4
tags:
    - Array
    - Matrix
    - Prefix Sum
---

<!-- problem:start -->

# [2906. Construct Product Matrix](https://leetcode.com/problems/construct-product-matrix)

## Description

<!-- description:start -->

<p>Given a <strong>0-indexed</strong> 2D integer matrix <code><font face="monospace">grid</font></code><font face="monospace"> </font>of size <code>n * m</code>, we define a <strong>0-indexed</strong> 2D matrix <code>p</code> of size <code>n * m</code> as the <strong>product</strong> matrix of <code>grid</code> if the following condition is met:</p>

<ul>
	<li>Each element <code>p[i][j]</code> is calculated as the product of all elements in <code>grid</code> except for the element <code>grid[i][j]</code>. This product is then taken modulo <code><font face="monospace">12345</font></code>.</li>
</ul>

<p>Return <em>the product matrix of</em> <code><font face="monospace">grid</font></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> [[24,12],[8,6]]
<strong>Explanation:</strong> p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
So the answer is [[24,12],[8,6]].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[12345],[2],[1]]
<strong>Output:</strong> [[2],[0],[0]]
<strong>Explanation:</strong> p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2.
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0. So p[0][1] = 0.
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0. So p[0][2] = 0.
So the answer is [[2],[0],[0]].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == grid.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m == grid[i].length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= n * m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix and Suffix Decomposition

We can preprocess the suffix product (excluding itself) of each element, and then traverse the matrix to calculate the prefix product (excluding itself) of each element. The product of the two gives us the result for each position.

Specifically, we use $p[i][j]$ to represent the result of the element in the $i$-th row and $j$-th column of the matrix. We define a variable $suf$ to represent the product of all elements below and to the right of the current position. Initially, $suf$ is set to $1$. We start traversing from the bottom right corner of the matrix. For each position $(i, j)$, we assign $suf$ to $p[i][j]$, and then update $suf$ to $suf \times grid[i][j] \bmod 12345$. This way, we can obtain the suffix product of each position.

Next, we start traversing from the top left corner of the matrix. For each position $(i, j)$, we multiply $p[i][j]$ by $pre$, take the result modulo $12345$, and then update $pre$ to $pre \times grid[i][j] \bmod 12345$. This way, we can obtain the prefix product of each position.

After the traversal, we return the result matrix $p$.

The time complexity is $O(n \times m)$, where $n$ and $m$ are the number of rows and columns in the matrix, respectively. Ignoring the space occupied by the result matrix, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]
        mod = 12345
        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suf
                suf = suf * grid[i][j] % mod
        pre = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = p[i][j] * pre % mod
                pre = pre * grid[i][j] % mod
        return p
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
