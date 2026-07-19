---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2617.Minimum%20Number%20of%20Visited%20Cells%20in%20a%20Grid/README_EN.md
rating: 2581
source: Weekly Contest 340 Q4
tags:
    - Stack
    - Breadth-First Search
    - Union Find
    - Array
    - Dynamic Programming
    - Matrix
    - Monotonic Stack
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2617. Minimum Number of Visited Cells in a Grid](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> <code>m x n</code> integer matrix <code>grid</code>. Your initial position is at the <strong>top-left</strong> cell <code>(0, 0)</code>.</p>

<p>Starting from the cell <code>(i, j)</code>, you can move to one of the following cells:</p>

<ul>
	<li>Cells <code>(i, k)</code> with <code>j &lt; k &lt;= grid[i][j] + j</code> (rightward movement), or</li>
	<li>Cells <code>(k, j)</code> with <code>i &lt; k &lt;= grid[i][j] + i</code> (downward movement).</li>
</ul>

<p>Return <em>the minimum number of cells you need to visit to reach the <strong>bottom-right</strong> cell</em> <code>(m - 1, n - 1)</code>. If there is no valid path, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2617.Minimum%20Number%20of%20Visited%20Cells%20in%20a%20Grid/images/ex1.png" style="width: 271px; height: 171px;" />
<pre>
<strong>Input:</strong> grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The image above shows one of the paths that visits exactly 4 cells.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2617.Minimum%20Number%20of%20Visited%20Cells%20in%20a%20Grid/images/ex2.png" style="width: 271px; height: 171px;" />
<pre>
<strong>Input:</strong> grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The image above shows one of the paths that visits exactly 3 cells.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2617.Minimum%20Number%20of%20Visited%20Cells%20in%20a%20Grid/images/ex3.png" style="width: 181px; height: 81px;" />
<pre>
<strong>Input:</strong> grid = [[2,1,0],[1,0,0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proven that no path exists.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt; m * n</code></li>
	<li><code>grid[m - 1][n - 1] == 0</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue

Let's denote the number of rows of the grid as $m$ and the number of columns as $n$. Define $dist[i][j]$ to be the shortest distance from the coordinate $(0, 0)$ to the coordinate $(i, j)$. Initially, $dist[0][0]=1$ and $dist[i][j]=-1$ for all other $i$ and $j$.

For each grid $(i, j)$, it can come from the grid above or the grid on the left. If it comes from the grid above $(i', j)$, where $0 \leq i' \lt i$, then $(i', j)$ must satisfy $grid[i'][j] + i' \geq i$. We need to select from these grids the one that is closest.

Therefore, we maintain a priority queue (min-heap) for each column $j$. Each element of the priority queue is a pair $(dist[i][j], i)$, which represents that the shortest distance from the coordinate $(0, 0)$ to the coordinate $(i, j)$ is $dist[i][j]$. When we consider the coordinate $(i, j)$, we only need to take out the head element $(dist[i'][j], i')$ of the priority queue. If $grid[i'][j] + i' \geq i$, we can move from the coordinate $(i', j)$ to the coordinate $(i, j)$. At this time, we can update the value of $dist[i][j]$, that is, $dist[i][j] = dist[i'][j] + 1$, and add $(dist[i][j], i)$ to the priority queue.

Similarly, we can maintain a priority queue for each row $i$ and perform a similar operation.

Finally, we can obtain the shortest distance from the coordinate $(0, 0)$ to the coordinate $(m - 1, n - 1)$, that is, $dist[m - 1][n - 1]$, which is the answer.

The time complexity is $O(m \times n \times \log (m \times n))$ and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1
        row = [[] for _ in range(m)]
        col = [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                while row[i] and grid[i][row[i][0][1]] + row[i][0][1] < j:
                    heappop(row[i])
                if row[i] and (dist[i][j] == -1 or dist[i][j] > row[i][0][0] + 1):
                    dist[i][j] = row[i][0][0] + 1
                while col[j] and grid[col[j][0][1]][j] + col[j][0][1] < i:
                    heappop(col[j])
                if col[j] and (dist[i][j] == -1 or dist[i][j] > col[j][0][0] + 1):
                    dist[i][j] = col[j][0][0] + 1
                if dist[i][j] != -1:
                    heappush(row[i], (dist[i][j], j))
                    heappush(col[j], (dist[i][j], i))
        return dist[-1][-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
