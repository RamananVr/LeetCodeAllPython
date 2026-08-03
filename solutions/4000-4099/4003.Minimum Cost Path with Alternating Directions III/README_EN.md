---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/4000-4099/4003.Minimum%20Cost%20Path%20with%20Alternating%20Directions%20III/README_EN.md
rating: 2122
source: Weekly Contest 512 Q4
---

<!-- problem:start -->

# [4003. Minimum Cost Path with Alternating Directions III](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii)

## Description

<!-- description:start -->

<p>You are given two integers <code>m</code> and <code>n</code> representing the number of rows and columns of a grid. Your goal is to reach cell <code>(m - 1, n - 1)</code>. You are also given a 2D integer array <code>penalty</code>.</p>

<p>The cost to enter cell <code>(i, j)</code> is <code>(i + 1) * (j + 1)</code>.</p>

<p>You begin at cell <code>(0, 0)</code> and initially pay its entrance cost. Actions performed after entering <code>(0, 0)</code> are numbered starting from 1.</p>

<p>On each action, you may move to an <strong>adjacent</strong> cell or wait in the current cell. A move follows the parity rule if:</p>

<ul>
	<li>On an <strong>odd-numbered</strong> action, you move <strong>right</strong> or <strong>down</strong>.</li>
	<li>On an <strong>even-numbered</strong> action, you move <strong>left</strong> or <strong>up</strong>.</li>
</ul>

<p>The cost of an action is determined as follows:</p>

<ul>
	<li>If you move according to the parity rule, pay only the entrance cost of the destination cell.</li>
	<li>If you move in a direction that <strong>violates</strong> the parity rule, pay the entrance cost of the destination cell plus <code>penalty[i][j]</code>, where <code>(i, j)</code> is the cell you move from.</li>
	<li>If you <strong>wait</strong> in cell <code>(i, j)</code>, pay <code>penalty[i][j]</code>.</li>
</ul>

<p>After every move or wait, the action number increases by 1. Therefore, the required parity alternates after every action, regardless of whether a penalty was paid.</p>

<p>Return the <strong>minimum</strong> total cost required to reach <code>(m - 1, n - 1)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 2, n = 2, penalty = [[5,3],[1,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal path is:</p>

<ul>
	<li>Start at cell <code>(0, 0)</code> with entry cost <code>(0 + 1) * (0 + 1) = 1</code>.</li>
	<li><strong>Move 1</strong>: Move down to cell <code>(1, 0)</code> with entry cost <code>(1 + 1) * (0 + 1) = 2</code>.</li>
	<li><strong>Move 2</strong>: Move right to cell <code>(1, 1)</code> with entry cost <code>(1 + 1) * (1 + 1) = 4</code> and an extra cost of <code>penalty[1][0] = 1</code> for violating the even parity rule.</li>
</ul>

<p>Thus, the total cost is <code>1 + 2 + 4 + 1 = 8</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 2, n = 2, penalty = [[0,7],[3,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal path is:</p>

<ul>
	<li>Start at cell <code>(0, 0)</code> with entry cost <code>(0 + 1) * (0 + 1) = 1</code>.</li>
	<li><strong>Move 1</strong>: Wait at cell <code>(0, 0)</code> with an extra cost of <code>penalty[0][0] = 0</code> to flip to even parity.</li>
	<li><strong>Move 2</strong>: Move right to cell <code>(0, 1)</code> with entry cost <code>(0 + 1) * (1 + 1) = 2</code> and an extra cost of <code>penalty[0][0] = 0</code> for violating the even parity rule.</li>
	<li><strong>Move 3</strong>: Move down to cell <code>(1, 1)</code> with entry cost <code>(1 + 1) * (1 + 1) = 4</code>.</li>
</ul>

<p>Thus, the total cost is <code>1 + 0 + 2 + 0 + 4 = 7</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 2, n = 3, penalty = [[8,0,9],[7,4,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal path is:</p>

<ul>
	<li>Start at cell <code>(0, 0)</code> with entry cost <code>(0 + 1) * (0 + 1) = 1</code>.</li>
	<li><strong>Move 1</strong>: Move right to cell <code>(0, 1)</code> with entry cost <code>(0 + 1) * (1 + 1) = 2</code>.</li>
	<li><strong>Move 2</strong>: Move right to cell <code>(0, 2)</code> with entry cost <code>(0 + 1) * (2 + 1) = 3</code> and an extra cost of <code>penalty[0][1] = 0</code> for violating the even parity rule.</li>
	<li><strong>Move 3</strong>: Move down to cell <code>(1, 2)</code> with entry cost <code>(1 + 1) * (2 + 1) = 6</code>.</li>
</ul>

<p>Thus, the total cost is <code>1 + 2 + 3 + 0 + 6 = 12</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>penalty.length == m</code></li>
	<li><code>penalty[i].length == n</code></li>
	<li><code>0 &lt;= penalty[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dijkstra

The cost to enter cell $(i, j)$ is $(i+1)(j+1)$. Actions are numbered from $1$: on odd actions you should move right or down, and on even actions left or up; you may also wait in place. Moving against the parity rule costs an extra $\textit{penalty}$ of the current cell, and waiting also costs $\textit{penalty}$. After every action the required parity flips.

Use state $(i, j, k)$ for the minimum cost of being at $(i, j)$ when the next action has parity $k$ ($k = 1$ for an odd action, $k = 0$ for an even action). The start is $(0, 0, 1)$ with cost $1$.

From the current state you may:

- **Wait**: add $\textit{penalty}[i][j]$ and flip the parity;
- **Move**: enumerate four directions, add the destination entrance cost; if the direction mismatches the current parity, also add $\textit{penalty}[i][j]$, then flip the parity at the new cell.

Run Dijkstra on this state graph; the first time $(m-1, n-1)$ is popped is the answer.

The time complexity is $O(mn \log (mn))$, and the space complexity is $O(mn)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        dist = [[[inf] * 2 for _ in range(n)] for _ in range(m)]
        dist[0][0][1] = 1
        pq = [(1, 0, 0, 1)]
        dirs = ((-1, 0), (0, 1), (0, -1), (1, 0))
        while pq:
            d, i, j, k = heappop(pq)
            if i == m - 1 and j == n - 1:
                return d
            if d > dist[i][j][k]:
                continue

            p = penalty[i][j]
            nd = d + p
            if nd < dist[i][j][k ^ 1]:
                dist[i][j][k ^ 1] = nd
                heappush(pq, (nd, i, j, k ^ 1))

            for idx, (dx, dy) in enumerate(dirs):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    nd = d + (x + 1) * (y + 1) + (idx & 1 ^ k) * p
                    if nd < dist[x][y][k ^ 1]:
                        dist[x][y][k ^ 1] = nd
                        heappush(pq, (nd, x, y, k ^ 1))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
