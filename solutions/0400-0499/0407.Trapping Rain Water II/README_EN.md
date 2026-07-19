---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0407.Trapping%20Rain%20Water%20II/README_EN.md
tags:
    - Breadth-First Search
    - Array
    - Matrix
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> integer matrix <code>heightMap</code> representing the height of each unit cell in a 2D elevation map, return <em>the volume of water it can trap after raining</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0407.Trapping%20Rain%20Water%20II/images/trap1-3d.jpg" style="width: 361px; height: 321px;" />
<pre>
<strong>Input:</strong> heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0407.Trapping%20Rain%20Water%20II/images/trap2-3d.jpg" style="width: 401px; height: 321px;" />
<pre>
<strong>Input:</strong> heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == heightMap.length</code></li>
	<li><code>n == heightMap[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heightMap[i][j] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Min Heap)

This is a variant of the trapping rain water problem. Since the heights on the matrix boundaries are fixed, we can add these boundary heights to a priority queue. Then, we repeatedly take out the minimum height from the priority queue and compare it with the heights of its four adjacent cells. If an adjacent cell's height is less than the current height, we can trap water there. The volume of trapped water is the difference between the current height and the adjacent height. We then add the larger height back to the priority queue and repeat this process until the priority queue is empty.

The time complexity is $O(m \times n \times \log (m \times n))$, and the space complexity is $O(m \times n)$, where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        vis = [[False] * n for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(pq, (heightMap[i][j], i, j))
                    vis[i][j] = True
        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        while pq:
            h, i, j = heappop(pq)
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if x >= 0 and x < m and y >= 0 and y < n and not vis[x][y]:
                    ans += max(0, h - heightMap[x][y])
                    vis[x][y] = True
                    heappush(pq, (max(h, heightMap[x][y]), x, y))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
