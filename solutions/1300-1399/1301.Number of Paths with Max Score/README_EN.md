---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1301.Number%20of%20Paths%20with%20Max%20Score/README_EN.md
rating: 1853
source: Biweekly Contest 16 Q4
tags:
    - Array
    - Dynamic Programming
    - Matrix
---

<!-- problem:start -->

# [1301. Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score)

## Description

<!-- description:start -->

<p>You are given a square <code>board</code>&nbsp;of characters. You can move on the board starting at the bottom right square marked with the character&nbsp;<code>&#39;S&#39;</code>.</p>

<p>You need&nbsp;to reach the top left square marked with the character <code>&#39;E&#39;</code>. The rest of the squares are labeled either with a numeric character&nbsp;<code>1, 2, ..., 9</code> or with an obstacle <code>&#39;X&#39;</code>. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.</p>

<p>Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, <strong>taken modulo <code>10^9 + 7</code></strong>.</p>

<p>In case there is no path, return&nbsp;<code>[0, 0]</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> board = ["E23","2X2","12S"]

<strong>Output:</strong> [7,1]

</pre><p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> board = ["E12","1X1","21S"]

<strong>Output:</strong> [4,2]

</pre><p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> board = ["E11","XXX","11S"]

<strong>Output:</strong> [0,0]

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>2 &lt;= board.length == board[i].length &lt;= 100</code></li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ to represent the maximum score from the starting point $(n - 1, n - 1)$ to $(i, j)$, and $g[i][j]$ to represent the number of ways to achieve the maximum score from the starting point $(n - 1, n - 1)$ to $(i, j)$. Initially, $f[n - 1][n - 1] = 0$ and $g[n - 1][n - 1] = 1$. The other positions of $f[i][j]$ are all $-1$, and $g[i][j]$ are all $0$.

For the current position $(i, j)$, it can be transferred from three positions: $(i + 1, j)$, $(i, j + 1)$, and $(i + 1, j + 1)$. Therefore, we can enumerate these three positions to update the values of $f[i][j]$ and $g[i][j]$. If the current position $(i, j)$ has an obstacle, or the current position is the starting point, or other positions are out of bounds, no update is performed. Otherwise, if another position $(x, y)$ satisfies $f[x][y] \gt f[i][j]$, then we update $f[i][j] = f[x][y]$ and $g[i][j] = g[x][y]$. If $f[x][y] = f[i][j]$, then we update $g[i][j] = g[i][j] + g[x][y]$. Finally, if the current position $(i, j)$ is reachable and is a number, we update $f[i][j] = f[i][j] + board[i][j]$.

Finally, if $f[0][0] \lt 0$, it means there is no path to reach the endpoint, return $[0, 0]$. Otherwise, return $[f[0][0], g[0][0]]$. Note that the result needs to be taken modulo $10^9 + 7$.

Time complexity $O(n^2)$, space complexity $O(n^2)$. Where $n$ is the side length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def update(i, j, x, y):
            if x >= n or y >= n or f[x][y] == -1 or board[i][j] in "XS":
                return
            if f[x][y] > f[i][j]:
                f[i][j] = f[x][y]
                g[i][j] = g[x][y]
            elif f[x][y] == f[i][j]:
                g[i][j] += g[x][y]

        n = len(board)
        f = [[-1] * n for _ in range(n)]
        g = [[0] * n for _ in range(n)]
        f[-1][-1], g[-1][-1] = 0, 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                update(i, j, i + 1, j)
                update(i, j, i, j + 1)
                update(i, j, i + 1, j + 1)
                if f[i][j] != -1 and board[i][j].isdigit():
                    f[i][j] += int(board[i][j])
        mod = 10**9 + 7
        return [0, 0] if f[0][0] == -1 else [f[0][0], g[0][0] % mod]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
