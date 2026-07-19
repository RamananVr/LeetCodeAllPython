---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/README_EN.md
rating: 1837
source: Biweekly Contest 33 Q4
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Array
    - Matrix
---

<!-- problem:start -->

# [1559. Detect Cycles in 2D Grid](https://leetcode.com/problems/detect-cycles-in-2d-grid)

## Description

<!-- description:start -->

<p>Given a 2D array of characters <code>grid</code> of size <code>m x n</code>, you need to find if there exists any cycle consisting of the <strong>same value</strong> in <code>grid</code>.</p>

<p>A cycle is a path of <strong>length 4 or more</strong> in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the <strong>same value</strong> of the current cell.</p>

<p>Also, you cannot move to the cell that you visited in your last move. For example, the cycle <code>(1, 1) -&gt; (1, 2) -&gt; (1, 1)</code> is invalid because from <code>(1, 2)</code> we visited <code>(1, 1)</code> which was the last visited cell.</p>

<p>Return <code>true</code> if any cycle of the same value exists in <code>grid</code>, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/1.png" style="width: 231px; height: 152px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;]]
<strong>Output:</strong> true
<strong>Explanation: </strong>There are two valid cycles shown in different colors in the image below:
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/11.png" style="width: 225px; height: 163px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/22.png" style="width: 236px; height: 154px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;c&quot;,&quot;c&quot;,&quot;c&quot;,&quot;a&quot;],[&quot;c&quot;,&quot;d&quot;,&quot;c&quot;,&quot;c&quot;],[&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;c&quot;],[&quot;f&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]]
<strong>Output:</strong> true
<strong>Explanation: </strong>There is only one valid cycle highlighted in the image below:
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/2.png" style="width: 229px; height: 157px;" />
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1559.Detect%20Cycles%20in%202D%20Grid/images/3.png" style="width: 183px; height: 120px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;z&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;b&quot;,&quot;a&quot;]]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

We can traverse each cell in the 2D grid. For each cell, if the cell $grid[i][j]$ has not been visited, we start a breadth-first search (BFS) from that cell. During the search, we need to record the parent node of each cell and the coordinates of the previous cell. If the value of the next cell is the same as the current cell, and it is not the previous cell, and it has already been visited, then it indicates the presence of a cycle, and we return $\textit{true}$. After traversing all cells, if no cycle is found, we return $\textit{false}$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the 2D grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        dirs = (-1, 0, 1, 0, -1)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if vis[i][j]:
                    continue
                vis[i][j] = True
                q = [(i, j, -1, -1)]
                while q:
                    x, y, px, py = q.pop()
                    for dx, dy in pairwise(dirs):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if grid[nx][ny] != grid[i][j] or (nx == px and ny == py):
                                continue
                            if vis[nx][ny]:
                                return True
                            vis[nx][ny] = True
                            q.append((nx, ny, x, y))
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: DFS

We can traverse each cell in the 2D grid. For each cell, if the cell $grid[i][j]$ has not been visited, we start a depth-first search (DFS) from that cell. During the search, we need to record the parent node of each cell and the coordinates of the previous cell. If the value of the next cell is the same as the current cell, and it is not the previous cell, and it has already been visited, then it indicates the presence of a cycle, and we return $\textit{true}$. After traversing all cells, if no cycle is found, we return $\textit{false}$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the 2D grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x: int, y: int, px: int, py: int) -> bool:
            vis[x][y] = True
            for dx, dy in pairwise(dirs):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] != grid[x][y] or (nx == px and ny == py):
                        continue
                    if vis[nx][ny] or dfs(nx, ny, x, y):
                        return True
            return False

        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        dirs = (-1, 0, 1, 0, -1)
        for i in range(m):
            for j in range(n):
                if vis[i][j]:
                    continue
                if dfs(i, j, -1, -1):
                    return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
