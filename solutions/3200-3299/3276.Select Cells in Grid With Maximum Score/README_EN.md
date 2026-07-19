---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3276.Select%20Cells%20in%20Grid%20With%20Maximum%20Score/README_EN.md
rating: 2402
source: Weekly Contest 413 Q3
tags:
    - Bit Manipulation
    - Array
    - Dynamic Programming
    - Bitmask
    - Matrix
---

<!-- problem:start -->

# [3276. Select Cells in Grid With Maximum Score](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score)

## Description

<!-- description:start -->

<p>You are given a 2D matrix <code>grid</code> consisting of positive integers.</p>

<p>You have to select <em>one or more</em> cells from the matrix such that the following conditions are satisfied:</p>

<ul>
	<li>No two selected cells are in the <strong>same</strong> row of the matrix.</li>
	<li>The values in the set of selected cells are <strong>unique</strong>.</li>
</ul>

<p>Your score will be the <strong>sum</strong> of the values of the selected cells.</p>

<p>Return the <strong>maximum</strong> score you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2,3],[4,3,2],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3276.Select%20Cells%20in%20Grid%20With%20Maximum%20Score/images/grid1drawio.png" /></p>

<p>We can select the cells with values 1, 3, and 4 that are colored above.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[8,7,6],[8,3,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3276.Select%20Cells%20in%20Grid%20With%20Maximum%20Score/images/grid8_8drawio.png" style="width: 170px; height: 114px;" /></p>

<p>We can select the cells with values 7 and 8 that are colored above.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: State Compression Dynamic Programming

We define $f[i][j]$ to represent the maximum score when selecting numbers from $[1,..i]$ and the state of the rows corresponding to the selected numbers is $j$. Initially, $f[i][j] = 0$, and the answer is $f[\textit{mx}][2^m - 1]$, where $\textit{mx}$ represents the maximum value in the matrix, and $m$ represents the number of rows in the matrix.

First, we preprocess the matrix using a hash table $g$ to record the set of rows corresponding to each number. Then, we can use state compression dynamic programming to solve the problem.

For the state $f[i][j]$, we can choose not to select the number $i$, in which case $f[i][j] = f[i-1][j]$. Alternatively, we can choose the number $i$. In this case, we need to enumerate each row $k$ in the set $g[i]$ corresponding to the number $i$. If the $k$-th bit of $j$ is $1$, it means we can select the number $i$. Thus, $f[i][j] = \max(f[i][j], f[i-1][j \oplus 2^k] + i)$.

Finally, we return $f[\textit{mx}][2^m - 1]$.

The time complexity is $O(m \times 2^m \times \textit{mx})$, and the space complexity is $O(\textit{mx} \times 2^m)$. Here, $m$ is the number of rows in the matrix, and $\textit{mx}$ is the maximum value in the matrix.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        g = defaultdict(set)
        mx = 0
        for i, row in enumerate(grid):
            for x in row:
                g[x].add(i)
                mx = max(mx, x)
        m = len(grid)
        f = [[0] * (1 << m) for _ in range(mx + 1)]
        for i in range(1, mx + 1):
            for j in range(1 << m):
                f[i][j] = f[i - 1][j]
                for k in g[i]:
                    if j >> k & 1:
                        f[i][j] = max(f[i][j], f[i - 1][j ^ 1 << k] + i)
        return f[-1][-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
