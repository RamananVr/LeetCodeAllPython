---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2503.Maximum%20Number%20of%20Points%20From%20Grid%20Queries/README_EN.md
rating: 2195
source: Weekly Contest 323 Q4
tags:
    - Breadth-First Search
    - Union Find
    - Array
    - Two Pointers
    - Matrix
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2503. Maximum Number of Points From Grid Queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> integer matrix <code>grid</code> and an array <code>queries</code> of size <code>k</code>.</p>

<p>Find an array <code>answer</code> of size <code>k</code> such that for each integer <code>queries[i]</code> you start in the <strong>top left</strong> cell of the matrix and repeat the following process:</p>

<ul>
	<li>If <code>queries[i]</code> is <strong>strictly</strong> greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any <strong>adjacent</strong> cell in all <code>4</code> directions: up, down, left, and right.</li>
	<li>Otherwise, you do not get any points, and you end this process.</li>
</ul>

<p>After the process, <code>answer[i]</code> is the <strong>maximum</strong> number of points you can get. <strong>Note</strong> that for each query you are allowed to visit the same cell <strong>multiple</strong> times.</p>

<p>Return <em>the resulting array</em> <code>answer</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2503.Maximum%20Number%20of%20Points%20From%20Grid%20Queries/images/image1.png" style="width: 571px; height: 152px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
<strong>Output:</strong> [5,8,1]
<strong>Explanation:</strong> The diagrams above show which cells we visit to get points for each query.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2503.Maximum%20Number%20of%20Points%20From%20Grid%20Queries/images/yetgriddrawio-2.png" />
<pre>
<strong>Input:</strong> grid = [[5,2,1],[1,1,2]], queries = [3]
<strong>Output:</strong> [0]
<strong>Explanation:</strong> We can not get any points because the value of the top left cell is already greater than or equal to 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 1000</code></li>
	<li><code>4 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>k == queries.length</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= grid[i][j], queries[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Offline Query + BFS + Priority Queue (Min Heap)

According to the problem description, each query is independent, the order of the queries does not affect the result, and we are required to start from the top left corner each time, counting the number of cells that can be accessed and whose value is less than the current query value.

Therefore, we can first sort the `queries` array, and then process each query in ascending order.

We use a priority queue (min heap) to maintain the smallest cell value that we have currently accessed, and use an array or hash table `vis` to record whether the current cell has been visited. Initially, we add the data $(grid[0][0], 0, 0)$ of the top left cell as a tuple to the priority queue, and set `vis[0][0]` to `True`.

For each query `queries[i]`, we judge whether the minimum value of the current priority queue is less than `queries[i]`. If it is, we pop the current minimum value, increment the counter `cnt`, and add the four cells above, below, left, and right of the current cell to the priority queue, noting to check whether they have been visited. Repeat the above operation until the minimum value of the current priority queue is greater than or equal to `queries[i]`, at which point `cnt` is the answer to the current query.

The time complexity is $O(k \times \log k + m \times n \log(m \times n))$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns of the grid, and $k$ is the number of queries. We need to sort the `queries` array, which has a time complexity of $O(k \times \log k)$. Each cell in the matrix will be visited at most once, and the time complexity of each enqueue and dequeue operation is $O(\log(m \times n))$. Therefore, the total time complexity is $O(k \times \log k + m \times n \log(m \times n))$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        qs = sorted((v, i) for i, v in enumerate(queries))
        ans = [0] * len(qs)
        q = [(grid[0][0], 0, 0)]
        cnt = 0
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        for v, k in qs:
            while q and q[0][0] < v:
                _, i, j = heappop(q)
                cnt += 1
                for a, b in pairwise((-1, 0, 1, 0, -1)):
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                        heappush(q, (grid[x][y], x, y))
                        vis[x][y] = True
            ans[k] = cnt
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
