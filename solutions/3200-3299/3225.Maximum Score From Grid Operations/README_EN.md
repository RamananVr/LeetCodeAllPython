---
comments: true
difficulty: Hard
rating: 3027
source: Biweekly Contest 135 Q4
tags:
    - Array
    - Dynamic Programming
    - Matrix
    - Prefix Sum
---

<!-- problem:start -->

# [3225. Maximum Score From Grid Operations](https://leetcode.com/problems/maximum-score-from-grid-operations)

## Description

<!-- description:start -->

<p>You are given a 2D matrix <code>grid</code> of size <code>n x n</code>. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices <code>(i, j)</code>, and color black all the cells of the <code>j<sup>th</sup></code> column starting from the top row down to the <code>i<sup>th</sup></code> row.</p>

<p>The grid score is the sum of all <code>grid[i][j]</code> such that cell <code>(i, j)</code> is white and it has a horizontally adjacent black cell.</p>

<p>Return the <strong>maximum</strong> score that can be achieved after some number of operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3225.Maximum%20Score%20From%20Grid%20Operations/images/one.png" style="width: 300px; height: 200px;" />
<p>In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is <code>grid[3][0] + grid[1][2] + grid[3][3]</code> which is equal to 11.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">94</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3225.Maximum%20Score%20From%20Grid%20Operations/images/two-1.png" style="width: 300px; height: 200px;" />
<p>We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is <code>grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4]</code> which is equal to 94.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;n == grid.length &lt;= 100</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming + Prefix Sum

<!-- thinking:start -->

> **Thinking**
>
> Each column is painted black from the top for some height; a white cell scores only if a neighbor column is black there. $n\le 100$, so enumerating height tuples is $(n+1)^n$. Column $j$'s score depends only on its height and its two neighbors, which suggests a column DP.
>
> $f[h_1][h_2]$ is the best score with current height $h_1$ and previous height $h_2$. When enumerating the next height, $\max(h_2,h_p)$ makes the addend piecewise, so prefix/suffix maxima over $h_2$ drop a column from $O(n^3)$ to $O(n^2)$. Column prefix sums precompute white-range totals.

<!-- thinking:end -->

For each column $j$, let $k[j] \in \{0, 1, \ldots, n\}$ be the number of cells colored black from the top. A white cell $(i, j)$ scores if and only if at least one horizontally adjacent cell is black, and it is counted only once. The contribution of column $j$ is therefore:

$$
\max\bigl(0,\ s[j][\max(k[j-1], k[j+1])] - s[j][k[j]]\bigr)
$$

where $s[j][h]$ is the prefix sum of the first $h$ cells in column $j$ (boundary column heights are treated as $0$).

Let $f[h_1][h_2]$ be the maximum score after processing column $j$ with $k[j] = h_1$ and $k[j-1] = h_2$. When choosing the next height $hp = k[j+1]$:

$$
g[hp][h_1] = \max_{h_2}\bigl(f[h_1][h_2] + \max(0,\ s[j][\max(h_2, hp)] - s[j][h_1])\bigr)
$$

Split the transition into $h_2 \le hp$ and $h_2 > hp$, and maintain prefix / suffix maxima so that each column costs $O(n^2)$ instead of $O(n^3)$.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$, where $n$ is the grid size.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i, x in enumerate(grid):
                s[j][i + 1] = s[j][i] + x[j]
        f = [[-inf] * (n + 1) for _ in range(n + 1)]
        for h in range(n + 1):
            f[h][0] = 0
        for j in range(n - 1):
            g = [[-inf] * (n + 1) for _ in range(n + 1)]
            for h1 in range(n + 1):
                pre = [-inf] * (n + 2)
                pre[0] = f[h1][0]
                for h2 in range(1, n + 1):
                    pre[h2] = max(pre[h2 - 1], f[h1][h2])
                suf = [-inf] * (n + 2)
                for h2 in range(n, -1, -1):
                    v = -inf
                    if f[h1][h2] != -inf:
                        v = f[h1][h2] + max(0, s[j][h2] - s[j][h1])
                    suf[h2] = max(suf[h2 + 1], v)
                for hp in range(n + 1):
                    add = max(0, s[j][hp] - s[j][h1])
                    v1 = -inf if pre[hp] == -inf else pre[hp] + add
                    g[hp][h1] = max(v1, suf[hp + 1])
            f = g
        ans = 0
        for h1 in range(n + 1):
            for h2 in range(n + 1):
                if f[h1][h2] != -inf:
                    ans = max(ans, f[h1][h2] + max(0, s[-1][h2] - s[-1][h1]))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
