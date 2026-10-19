---
comments: true
difficulty: Medium
---

<!-- problem:start -->

# [4084. Last Visited Cell in a Directional Grid](https://leetcode.com/problems/last-visited-cell-in-a-directional-grid)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> matrix <code>grid</code> where each cell contains one of the following characters:</p>

<ul>
	<li><code>&#39;L&#39;</code>: move one cell left.</li>
	<li><code>&#39;R&#39;</code>: move one cell right.</li>
	<li><code>&#39;U&#39;</code>: move one cell up.</li>
	<li><code>&#39;D&#39;</code>: move one cell down.</li>
</ul>

<p>You start at cell <code>(0, 0)</code>, which is considered visited. At each step, move to the cell indicated by the character in your current cell.</p>

<p>The process <strong>ends</strong> if the indicated move would either leave the grid or enter a cell that has already been visited. In either case, the move is <strong>not</strong> made.</p>

<p>Return an integer array <code>[r, c]</code> representing the <strong>row and column indices</strong> of the <strong>last visited cell</strong>. The indices are <strong>0-based</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[&quot;R&quot;,&quot;D&quot;],[&quot;U&quot;,&quot;L&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Start at cell <code>(0, 0)</code>, which contains <code>&#39;R&#39;</code>, so move right to <code>(0, 1)</code>.</li>
	<li>At cell <code>(0, 1)</code>, the character is <code>&#39;D&#39;</code>, so move down to <code>(1, 1)</code>.</li>
	<li>At cell <code>(1, 1)</code>, the character is <code>&#39;L&#39;</code>, so move left to <code>(1, 0)</code>.</li>
	<li>At cell <code>(1, 0)</code>, the character is <code>&#39;U&#39;</code>, which indicates moving to <code>(0, 0)</code>. However, <code>(0, 0)</code> has already been visited, so this move is not made.</li>
	<li>Therefore, the process ends at the last visited cell <code>(1, 0)</code>, so the answer is <code>[1, 0]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[&quot;R&quot;,&quot;R&quot;,&quot;R&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,2]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Start at cell <code>(0, 0)</code>, which contains <code>&#39;R&#39;</code>, so move right to <code>(0, 1)</code>.</li>
	<li>At cell <code>(0, 1)</code>, the character is <code>&#39;R&#39;</code>, so move right to <code>(0, 2)</code>.</li>
	<li>At cell <code>(0, 2)</code>, the character is <code>&#39;R&#39;</code>, which indicates moving to <code>(0, 3)</code>. However, <code>(0, 3)</code> is outside the grid, so this move is not made.</li>
	<li>Therefore, the process ends at the last visited cell <code>(0, 2)</code>, so the answer is <code>[0, 2]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= n == grid[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>grid[i][j]</code> is one of <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, <code>&#39;U&#39;</code>, or <code>&#39;D&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> The grid has at most $10^5$ cells. Following the arrows without remembering visited cells never stops once the path enters a cycle.
>
> Movement ends in only two cases: the next step would leave the grid, or it would enter a cell that was already visited. In both cases that step is not taken, and the answer is the previous valid coordinate.
>
> Each cell is entered at most once. Mark visits in a two-dimensional boolean array, start at $(0,0)$, update the row and column from the current character, and return the saved coordinate when the next step is illegal.

<!-- thinking:end -->

Simulate from $(0,0)$. Use a boolean array $\textit{vis}$ to mark cells that have already been visited. At each step, save the current coordinate $(r,c)$, then move according to $\textit{grid}[r][c]$: $L$ and $R$ change the column, while $U$ and $D$ change the row. If the new coordinate is outside the grid or its cell has already been visited, do not take that step and return the saved coordinate. Each cell is visited at most once.

The time complexity is $O(mn)$ and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        r = c = 0
        vis = [[False] * n for _ in range(m)]
        while 1:
            cur = [r, c]
            vis[r][c] = True
            match grid[r][c]:
                case "L":
                    c -= 1
                case "R":
                    c += 1
                case "U":
                    r -= 1
                case "D":
                    r += 1
            if 0 <= r < m and 0 <= c < n and not vis[r][c]:
                continue
            return cur
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
