---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2664.The%20Knight%E2%80%99s%20Tour/README_EN.md
tags:
    - Array
    - Backtracking
    - Matrix
---

<!-- problem:start -->

# [2664. The Knight’s Tour 🔒](https://leetcode.com/problems/the-knights-tour)

## Description

<!-- description:start -->

<p>Given two positive integers <code>m</code> and <code>n</code> which are the height and width of a <strong>0-indexed</strong> 2D-array <code>board</code>, a pair of positive integers <code>(r, c)</code> which is the starting position of the knight on the board.</p>

<p>Your task is to find an order of movements for the knight, in a manner that every cell of the&nbsp;<code>board</code> gets visited <strong>exactly</strong> once (the starting cell is considered visited and you <strong>shouldn&#39;t</strong> visit it again).</p>

<p>Return <em>the array</em> <code>board</code> <em>in which the cells&#39; values show the order of visiting the cell starting from 0 (the initial place of the knight).</em></p>

<p>Note that a <strong>knight</strong> can <strong>move</strong> from cell <code>(r1, c1)</code> to cell <code>(r2, c2)</code> if <code>0 &lt;= r2 &lt;= m - 1</code> and <code>0 &lt;= c2 &lt;= n - 1</code> and <code>min(abs(r1 - r2), abs(c1 - c2)) = 1</code> and <code>max(abs(r1 - r2), abs(c1 - c2)) = 2</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> m = 1, n = 1, r = 0, c = 0
<strong>Output:</strong> [[0]]
<strong>Explanation:</strong> There is only 1 cell and the knight is initially on it so there is only a 0 inside the 1x1 grid.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 4, r = 0, c = 0
<strong>Output:</strong> [[0,3,6,9],[11,8,1,4],[2,5,10,7]]
<strong>Explanation:</strong> By the following order of movements we can visit the entire board.
(0,0)-&gt;(1,2)-&gt;(2,0)-&gt;(0,1)-&gt;(1,3)-&gt;(2,1)-&gt;(0,2)-&gt;(2,3)-&gt;(1,1)-&gt;(0,3)-&gt;(2,2)-&gt;(1,0)</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 5</code></li>
	<li><code>0 &lt;= r &lt;= m - 1</code></li>
	<li><code>0 &lt;= c &lt;= n - 1</code></li>
	<li>The inputs will be generated such that there exists <strong>at least</strong> one possible order of movements with the given condition</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Backtracking

We create a two-dimensional array $g$, used to record the knight's movement order, initially $g[r][c] = -1$, and all other positions are set to $-1$ as well. Additionally, we need a variable $ok$ to record whether a solution has been found.

Next, we start depth-first search from $(r, c)$. Each time we search position $(i, j)$, we first check if $g[i][j]$ equals $m \times n - 1$. If so, it means we have found a solution, then we set $ok$ to `true` and return. Otherwise, we enumerate the knight's eight possible movement directions to position $(x, y)$. If $0 \leq x < m$, $0 \leq y < n$, and $g[x][y]=-1$, then we update $g[x][y]$ to $g[i][j]+1$, and recursively search position $(x, y)$. If after the search, the variable $ok$ is `true`, we return directly. Otherwise, we reset $g[x][y]$ to $-1$ and continue searching in other directions.

Finally, return the two-dimensional array $g$.

The time complexity is $O(8^{m \times n})$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the integers given in the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        def dfs(i: int, j: int):
            nonlocal ok
            if g[i][j] == m * n - 1:
                ok = True
                return
            for a, b in pairwise((-2, -1, 2, 1, -2, 1, 2, -1, -2)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and g[x][y] == -1:
                    g[x][y] = g[i][j] + 1
                    dfs(x, y)
                    if ok:
                        return
                    g[x][y] = -1

        g = [[-1] * n for _ in range(m)]
        g[r][c] = 0
        ok = False
        dfs(r, c)
        return g
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
