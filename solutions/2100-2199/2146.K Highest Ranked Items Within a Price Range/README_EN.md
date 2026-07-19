---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2100-2199/2146.K%20Highest%20Ranked%20Items%20Within%20a%20Price%20Range/README_EN.md
rating: 1836
source: Biweekly Contest 70 Q3
tags:
    - Breadth-First Search
    - Array
    - Matrix
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2146. K Highest Ranked Items Within a Price Range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> 2D integer array <code>grid</code> of size <code>m x n</code> that represents a map of the items in a shop. The integers in the grid represent the following:</p>

<ul>
	<li><code>0</code> represents a wall that you cannot pass through.</li>
	<li><code>1</code> represents an empty cell that you can freely move to and from.</li>
	<li>All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.</li>
</ul>

<p>It takes <code>1</code> step to travel between adjacent grid cells.</p>

<p>You are also given integer arrays <code>pricing</code> and <code>start</code> where <code>pricing = [low, high]</code> and <code>start = [row, col]</code> indicates that you start at the position <code>(row, col)</code> and are interested only in items with a price in the range of <code>[low, high]</code> (<strong>inclusive</strong>). You are further given an integer <code>k</code>.</p>

<p>You are interested in the <strong>positions</strong> of the <code>k</code> <strong>highest-ranked</strong> items whose prices are <strong>within</strong> the given price range. The rank is determined by the <strong>first</strong> of these criteria that is different:</p>

<ol>
	<li>Distance, defined as the length of the shortest path from the <code>start</code> (<strong>shorter</strong> distance has a higher rank).</li>
	<li>Price (<strong>lower</strong> price has a higher rank, but it must be <strong>in the price range</strong>).</li>
	<li>The row number (<strong>smaller</strong> row number has a higher rank).</li>
	<li>The column number (<strong>smaller</strong> column number has a higher rank).</li>
</ol>

<p>Return <em>the </em><code>k</code><em> highest-ranked items within the price range <strong>sorted</strong> by their rank (highest to lowest)</em>. If there are fewer than <code>k</code> reachable items within the price range, return <em><strong>all</strong> of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2146.K%20Highest%20Ranked%20Items%20Within%20a%20Price%20Range/images/example1drawio.png" style="width: 200px; height: 151px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3
<strong>Output:</strong> [[0,1],[1,1],[2,1]]
<strong>Explanation:</strong> You start at (0,0).
With a price range of [2,5], we can take items from (0,1), (1,1), (2,1) and (2,2).
The ranks of these items are:
- (0,1) with distance 1
- (1,1) with distance 2
- (2,1) with distance 3
- (2,2) with distance 4
Thus, the 3 highest ranked items in the price range are (0,1), (1,1), and (2,1).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2146.K%20Highest%20Ranked%20Items%20Within%20a%20Price%20Range/images/example2drawio1.png" style="width: 200px; height: 151px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2
<strong>Output:</strong> [[2,1],[1,2]]
<strong>Explanation:</strong> You start at (2,3).
With a price range of [2,3], we can take items from (0,1), (1,1), (1,2) and (2,1).
The ranks of these items are:
- (2,1) with distance 2, price 2
- (1,2) with distance 2, price 3
- (1,1) with distance 3
- (0,1) with distance 4
Thus, the 2 highest ranked items in the price range are (2,1) and (1,2).
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2146.K%20Highest%20Ranked%20Items%20Within%20a%20Price%20Range/images/example3.png" style="width: 149px; height: 150px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3
<strong>Output:</strong> [[2,1],[2,0]]
<strong>Explanation:</strong> You start at (0,0).
With a price range of [2,3], we can take items from (2,0) and (2,1). 
The ranks of these items are: 
- (2,1) with distance 5
- (2,0) with distance 6
Thus, the 2 highest ranked items in the price range are (2,1) and (2,0). 
Note that k = 3 but there are only 2 reachable items within the price range.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>pricing.length == 2</code></li>
	<li><code>2 &lt;= low &lt;= high &lt;= 10<sup>5</sup></code></li>
	<li><code>start.length == 2</code></li>
	<li><code>0 &lt;= row &lt;= m - 1</code></li>
	<li><code>0 &lt;= col &lt;= n - 1</code></li>
	<li><code>grid[row][col] &gt; 0</code></li>
	<li><code>1 &lt;= k &lt;= m * n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS + Sorting

We can start from $(\textit{row}, \textit{col})$ and use breadth-first search to find all items with prices in the range $[\textit{low}, \textit{high}]$. Store the distance, price, row coordinate, and column coordinate of these items in the array $\textit{pq}$.

Finally, sort $\textit{pq}$ by distance, price, row coordinate, and column coordinate, and return the coordinates of the first $k$ items.

The time complexity is $O(m \times n \times \log (m \times n))$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the 2D array $\textit{grid}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row, col = start
        low, high = pricing
        q = deque([(row, col)])
        pq = []
        if low <= grid[row][col] <= high:
            pq.append((0, grid[row][col], row, col))
        grid[row][col] = 0
        dirs = (-1, 0, 1, 0, -1)
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for a, b in pairwise(dirs):
                    nx, ny = x + a, y + b
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                        if low <= grid[nx][ny] <= high:
                            pq.append((step, grid[nx][ny], nx, ny))
                        grid[nx][ny] = 0
                        q.append((nx, ny))
        pq.sort()
        return [list(x[2:]) for x in pq[:k]]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
