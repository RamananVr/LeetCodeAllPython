---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/README_EN.md
tags:
    - Array
    - Math
    - Dynamic Programming
    - Matrix
---

<!-- problem:start -->

# [750. Number Of Corner Rectangles 🔒](https://leetcode.com/problems/number-of-corner-rectangles)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> integer matrix <code>grid</code> where each entry is only <code>0</code> or <code>1</code>, return <em>the number of <strong>corner rectangles</strong></em>.</p>

<p>A <strong>corner rectangle</strong> is four distinct <code>1</code>&#39;s on the grid that forms an axis-aligned rectangle. Note that only the corners need to have the value <code>1</code>. Also, all four <code>1</code>&#39;s used must be distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/images/cornerrec1-grid.jpg" style="width: 413px; height: 333px;" />
<pre>
<strong>Input:</strong> grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/images/cornerrec2-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,1,1],[1,1,1]]
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/images/cornerrec3-grid.jpg" style="width: 333px; height: 93px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1,1]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Rectangles must have four distinct corners.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>The number of <code>1</code>&#39;s in the grid is in the range <code>[1, 6000]</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

We enumerate each row as the bottom of the rectangle. For the current row, if both column $i$ and column $j$ are $1$, then we use a hash table to find out how many of the previous rows have both columns $i$ and $j$ as $1$. This is the number of rectangles with $(i, j)$ as the bottom right corner, and we add this number to the answer. Then we add $(i, j)$ to the hash table and continue to enumerate the next pair $(i, j)$.

The time complexity is $O(m \times n^2)$, and the space complexity is $O(n^2)$. Here, $m$ and $n$ are the number of rows and columns of the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        ans = 0
        cnt = Counter()
        n = len(grid[0])
        for row in grid:
            for i, c1 in enumerate(row):
                if c1:
                    for j in range(i + 1, n):
                        if row[j]:
                            ans += cnt[(i, j)]
                            cnt[(i, j)] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
