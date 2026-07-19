---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2713.Maximum%20Strictly%20Increasing%20Cells%20in%20a%20Matrix/README_EN.md
rating: 2387
source: Weekly Contest 347 Q4
tags:
    - Memoization
    - Array
    - Hash Table
    - Binary Search
    - Dynamic Programming
    - Matrix
    - Ordered Set
    - Sorting
---

<!-- problem:start -->

# [2713. Maximum Strictly Increasing Cells in a Matrix](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix)

## Description

<!-- description:start -->

<p>Given a <strong>1-indexed</strong>&nbsp;<code>m x n</code> integer matrix <code>mat</code>, you can select any cell in the matrix as your <strong>starting cell</strong>.</p>

<p>From the starting cell, you can move to any other cell <strong>in the</strong> <strong>same row or column</strong>, but only if the value of the destination cell is <strong>strictly greater</strong> than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.</p>

<p>Your task is to find the <strong>maximum number of cells</strong> that you can visit in the matrix by starting from some cell.</p>

<p>Return <em>an integer denoting the maximum number of cells that can be visited.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong class="example"><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2700-2799/2713.Maximum%20Strictly%20Increasing%20Cells%20in%20a%20Matrix/images/diag1drawio.png" style="width: 200px; height: 176px;" /></strong></p>

<pre>
<strong>Input:</strong> mat = [[3,1],[3,4]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong class="example"><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2700-2799/2713.Maximum%20Strictly%20Increasing%20Cells%20in%20a%20Matrix/images/diag3drawio.png" style="width: 200px; height: 176px;" /></strong></p>

<pre>
<strong>Input:</strong> mat = [[1,1],[1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Since the cells must be strictly increasing, we can only visit one cell in this example. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong class="example"><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2700-2799/2713.Maximum%20Strictly%20Increasing%20Cells%20in%20a%20Matrix/images/diag4drawio.png" style="width: 350px; height: 250px;" /></strong></p>

<pre>
<strong>Input:</strong> mat = [[3,1,6],[-9,5,7]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length&nbsp;</code></li>
	<li><code>n == mat[i].length&nbsp;</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Dynamic Programming

Based on the problem description, the value of the cells we move through in sequence must strictly increase. Therefore, we can use a hash table $g$ to record the positions of all cells corresponding to each value, and then traverse from the smallest to the largest value.

During this process, we can maintain two arrays `rowMax` and `colMax`, which record the maximum increasing length of each row and column, respectively. Initially, all elements of these two arrays are $0$.

For all cell positions corresponding to each value, we traverse them in order of position. For each position $(i, j)$, we can calculate the maximum increasing length ending at that position as $1 + \max(\textit{rowMax}[i], \textit{colMax}[j])$, update the answer, and then update `rowMax[i]` and `colMax[j]`.

Finally, return the answer.

The time complexity is $O(m \times n \times \log(m \times n))$, and the space complexity is $O(m \times n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[mat[i][j]].append((i, j))
        rowMax = [0] * m
        colMax = [0] * n
        ans = 0
        for _, pos in sorted(g.items()):
            mx = []
            for i, j in pos:
                mx.append(1 + max(rowMax[i], colMax[j]))
                ans = max(ans, mx[-1])
            for k, (i, j) in enumerate(pos):
                rowMax[i] = max(rowMax[i], mx[k])
                colMax[j] = max(colMax[j], mx[k])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
