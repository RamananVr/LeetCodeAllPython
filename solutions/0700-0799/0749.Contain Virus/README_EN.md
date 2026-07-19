---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0749.Contain%20Virus/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Array
    - Matrix
    - Simulation
---

<!-- problem:start -->

# [749. Contain Virus](https://leetcode.com/problems/contain-virus)

## Description

<!-- description:start -->

<p>A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.</p>

<p>The world is modeled as an <code>m x n</code> binary grid <code>isInfected</code>, where <code>isInfected[i][j] == 0</code> represents uninfected cells, and <code>isInfected[i][j] == 1</code> represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two <strong>4-directionally</strong> adjacent cells, on the shared boundary.</p>

<p>Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There <strong>will never be a tie</strong>.</p>

<p>Return <em>the number of walls used to quarantine all the infected regions</em>. If the world will become fully infected, return the number of walls used.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus11-grid.jpg" style="width: 500px; height: 255px;" />
<pre>
<strong>Input:</strong> isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus12edited-grid.jpg" style="width: 500px; height: 257px;" />
On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus13edited-grid.jpg" style="width: 500px; height: 261px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0749.Contain%20Virus/images/virus2-grid.jpg" style="width: 653px; height: 253px;" />
<pre>
<strong>Input:</strong> isInfected = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> The region on the left only builds two new walls.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;isInfected.length</code></li>
	<li><code>n ==&nbsp;isInfected[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>isInfected[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There is always a contiguous viral region throughout the described process that will <strong>infect strictly more uncontaminated squares</strong> in the next round.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        def dfs(i, j):
            vis[i][j] = True
            areas[-1].append((i, j))
            for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    if isInfected[x][y] == 1 and not vis[x][y]:
                        dfs(x, y)
                    elif isInfected[x][y] == 0:
                        c[-1] += 1
                        boundaries[-1].add((x, y))

        m, n = len(isInfected), len(isInfected[0])
        ans = 0
        while 1:
            vis = [[False] * n for _ in range(m)]
            areas = []
            c = []
            boundaries = []
            for i, row in enumerate(isInfected):
                for j, v in enumerate(row):
                    if v == 1 and not vis[i][j]:
                        areas.append([])
                        boundaries.append(set())
                        c.append(0)
                        dfs(i, j)
            if not areas:
                break
            idx = boundaries.index(max(boundaries, key=len))
            ans += c[idx]
            for k, area in enumerate(areas):
                if k == idx:
                    for i, j in area:
                        isInfected[i][j] = -1
                else:
                    for i, j in area:
                        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                            x, y = i + a, j + b
                            if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                                isInfected[x][y] = 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
