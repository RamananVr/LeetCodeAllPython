---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0688.Knight%20Probability%20in%20Chessboard/README_EN.md
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [688. Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard)

## Description

<!-- description:start -->

<p>On an <code>n x n</code> chessboard, a knight starts at the cell <code>(row, column)</code> and attempts to make exactly <code>k</code> moves. The rows and columns are <strong>0-indexed</strong>, so the top-left cell is <code>(0, 0)</code>, and the bottom-right cell is <code>(n - 1, n - 1)</code>.</p>

<p>A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.</p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0688.Knight%20Probability%20in%20Chessboard/images/knight.png" style="width: 300px; height: 300px;" />
<p>Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.</p>

<p>The knight continues moving until it has made exactly <code>k</code> moves or has moved off the chessboard.</p>

<p>Return <em>the probability that the knight remains on the board after it has stopped moving</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 2, row = 0, column = 0
<strong>Output:</strong> 0.06250
<strong>Explanation:</strong> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 0, row = 0, column = 0
<strong>Output:</strong> 1.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 25</code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
	<li><code>0 &lt;= row, column &lt;= n - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[h][i][j]$ to represent the probability that the knight remains on the board after taking $h$ steps starting from position $(i, j)$. The final answer is $f[k][\textit{row}][\textit{column}]$.

When $h=0$, the knight is definitely on the board, so the probability is $1$, i.e., $f[0][i][j]=1$.

When $h \gt 0$, the probability that the knight is at position $(i, j)$ can be derived from the probabilities of the $8$ possible positions it could have come from in the previous step, i.e.,

$$
f[h][i][j] = \sum_{x, y} f[h - 1][x][y] \times \frac{1}{8}
$$

where $(x, y)$ is one of the $8$ positions the knight can move to from $(i, j)$.

The final answer is $f[k][\textit{row}][\textit{column}]$.

The time complexity is $O(k \times n^2)$, and the space complexity is $O(k \times n^2)$. Here, $k$ and $n$ are the given number of steps and the size of the board, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        f = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for i in range(n):
            for j in range(n):
                f[0][i][j] = 1
        for h in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for a, b in pairwise((-2, -1, 2, 1, -2, 1, 2, -1, -2)):
                        x, y = i + a, j + b
                        if 0 <= x < n and 0 <= y < n:
                            f[h][i][j] += f[h - 1][x][y] / 8
        return f[k][row][column]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
