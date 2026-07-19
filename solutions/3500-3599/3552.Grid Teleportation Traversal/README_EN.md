---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3552.Grid%20Teleportation%20Traversal/README_EN.md
rating: 2036
source: Weekly Contest 450 Q3
tags:
    - Breadth-First Search
    - Array
    - Hash Table
    - Matrix
---

<!-- problem:start -->

# [3552. Grid Teleportation Traversal](https://leetcode.com/problems/grid-teleportation-traversal)

## Description

<!-- description:start -->

<p>You are given a 2D character grid <code>matrix</code> of size <code>m x n</code>, represented as an array of strings, where <code>matrix[i][j]</code> represents the cell at the intersection of the <code>i<sup>th</sup></code> row and <code>j<sup>th</sup></code> column. Each cell is one of the following:</p>

<ul>
	<li><code>&#39;.&#39;</code> representing an empty cell.</li>
	<li><code>&#39;#&#39;</code> representing an obstacle.</li>
	<li>An uppercase letter (<code>&#39;A&#39;</code>-<code>&#39;Z&#39;</code>) representing a teleportation portal.</li>
</ul>

<p>You start at the top-left cell <code>(0, 0)</code>, and your goal is to reach the bottom-right cell <code>(m - 1, n - 1)</code>. You can move from the current cell to any adjacent cell (up, down, left, right) as long as the destination cell is within the grid bounds and is not an obstacle<strong>.</strong></p>

<p>If you step on a cell containing a portal letter and you haven&#39;t used that portal letter before, you may instantly teleport to any other cell in the grid with the same letter. This teleportation does not count as a move, but each portal letter can be used<strong> at most </strong>once during your journey.</p>

<p>Return the <strong>minimum</strong> number of moves required to reach the bottom-right cell. If it is not possible to reach the destination, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">matrix = [&quot;A..&quot;,&quot;.A.&quot;,&quot;...&quot;]</span></p>

<p><strong>Output:</strong> 2</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3500-3599/3552.Grid%20Teleportation%20Traversal/images/example04140.png" style="width: 151px; height: 151px;" /></p>

<ul>
	<li>Before the first move, teleport from <code>(0, 0)</code> to <code>(1, 1)</code>.</li>
	<li>In the first move, move from <code>(1, 1)</code> to <code>(1, 2)</code>.</li>
	<li>In the second move, move from <code>(1, 2)</code> to <code>(2, 2)</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">matrix = [&quot;.#...&quot;,&quot;.#.#.&quot;,&quot;.#.#.&quot;,&quot;...#.&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3500-3599/3552.Grid%20Teleportation%20Traversal/images/ezgifcom-animated-gif-maker.gif" style="width: 251px; height: 201px;" /></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == matrix.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= n == matrix[i].length &lt;= 10<sup>3</sup></code></li>
	<li><code>matrix[i][j]</code> is either <code>&#39;#&#39;</code>, <code>&#39;.&#39;</code>, or an uppercase English letter.</li>
	<li><code>matrix[0][0]</code> is not an obstacle.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: 0-1 BFS

We can use 0-1 BFS to solve this problem. We start from the top-left cell and use a double-ended queue to store the coordinates of the current cell. Each time we dequeue a cell, we check its four adjacent cells. If an adjacent cell is an empty cell and has not been visited, we add it to the queue and update its distance.

If an adjacent cell is a portal, we add it to the front of the queue and update its distance. We also need to maintain a dictionary to store the positions of each portal so that we can quickly find them when using a portal.

We also need a 2D array to store the distance for each cell, initialized to infinity. We set the distance of the starting point to 0 and then start BFS.

During the BFS process, we check whether each cell is the destination. If it is, we return its distance. If the queue is empty and the destination has not been reached, we return -1.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        g = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c.isalpha():
                    g[c].append((i, j))
        dirs = (-1, 0, 1, 0, -1)
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            d = dist[i][j]
            if i == m - 1 and j == n - 1:
                return d
            c = matrix[i][j]
            if c in g:
                for x, y in g[c]:
                    if d < dist[x][y]:
                        dist[x][y] = d
                        q.appendleft((x, y))
                del g[c]
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if (
                    0 <= x < m
                    and 0 <= y < n
                    and matrix[x][y] != "#"
                    and d + 1 < dist[x][y]
                ):
                    dist[x][y] = d + 1
                    q.append((x, y))
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
