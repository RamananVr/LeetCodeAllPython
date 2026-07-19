---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3286.Find%20a%20Safe%20Walk%20Through%20a%20Grid/README_EN.md
rating: 1607
source: Biweekly Contest 139 Q2
tags:
    - Breadth-First Search
    - Graph
    - Array
    - Matrix
    - Shortest Path
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3286. Find a Safe Walk Through a Grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> binary matrix <code>grid</code> and an integer <code>health</code>.</p>

<p>You start on the upper-left corner <code>(0, 0)</code> and would like to get to the lower-right corner <code>(m - 1, n - 1)</code>.</p>

<p>You can move up, down, left, or right from one cell to another adjacent cell as long as your health <em>remains</em> <strong>positive</strong>.</p>

<p>Cells <code>(i, j)</code> with <code>grid[i][j] = 1</code> are considered <strong>unsafe</strong> and reduce your health by 1.</p>

<p>Return <code>true</code> if you can reach the final cell with a health value of 1 or more, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The final cell can be reached safely by walking along the gray cells below.</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3286.Find%20a%20Safe%20Walk%20Through%20a%20Grid/images/3868_examples_1drawio.png" style="width: 301px; height: 121px;" /></div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>A minimum of 4 health points is needed to reach the final cell safely.</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3286.Find%20a%20Safe%20Walk%20Through%20a%20Grid/images/3868_examples_2drawio.png" style="width: 361px; height: 161px;" /></div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The final cell can be reached safely by walking along the gray cells below.</p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3286.Find%20a%20Safe%20Walk%20Through%20a%20Grid/images/3868_examples_3drawio.png" style="width: 181px; height: 121px;" /></p>

<p>Any path that does not go through the cell <code>(1, 1)</code> is unsafe since your health will drop to 0 when reaching the final cell.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code><font face="monospace">2 &lt;= m * n</font></code></li>
	<li><code>1 &lt;= health &lt;= m + n</code></li>
	<li><code>grid[i][j]</code> is either 0 or 1.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

We define a 2D array $\textit{dist}$, where $\textit{dist}[i][j]$ represents the minimum health value required to reach position $(i, j)$ from the top-left corner. Initially, we set $\textit{dist}[0][0]$ to $\textit{grid}[0][0]$ and add $(0, 0)$ to the queue $\textit{q}$.

Then, we continuously take elements $(x, y)$ from the queue and try to move in four directions. If we move to a valid position $(nx, ny)$ and the health value required to move from $(x, y)$ to $(nx, ny)$ is smaller, we update $\textit{dist}[nx][ny] = \textit{dist}[x][y] + \textit{grid}[nx][ny]$ and add $(nx, ny)$ to the queue $\textit{q}$.

Finally, when the queue is empty, we obtain $\textit{dist}[m-1][n-1]$, which is the minimum health value required to reach the bottom-right corner from the top-left corner. If this value is less than $\textit{health}$, then we can reach the bottom-right corner; otherwise, we cannot.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        q = deque([(0, 0)])
        dirs = (-1, 0, 1, 0, -1)
        while q:
            x, y = q.popleft()
            for a, b in pairwise(dirs):
                nx, ny = x + a, y + b
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and dist[nx][ny] > dist[x][y] + grid[nx][ny]
                ):
                    dist[nx][ny] = dist[x][y] + grid[nx][ny]
                    q.append((nx, ny))
        return dist[-1][-1] < health
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
