---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2387.Median%20of%20a%20Row%20Wise%20Sorted%20Matrix/README_EN.md
tags:
    - Array
    - Binary Search
    - Matrix
---

<!-- problem:start -->

# [2387. Median of a Row Wise Sorted Matrix 🔒](https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> matrix <code>grid</code> containing an <strong>odd</strong> number of integers where each row is sorted in <strong>non-decreasing</strong> order, return <em>the <strong>median</strong> of the matrix</em>.</p>

<p>You must solve the problem in less than <code>O(m * n)</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1,2],[2,3,3],[1,3,4]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The elements of the matrix in sorted order are 1,1,1,2,<u>2</u>,3,3,3,4. The median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1,3,3,4]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The elements of the matrix in sorted order are 1,1,<u>3</u>,3,4. The median is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>m</code> and <code>n</code> are both odd.</li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
	<li><code>grid[i]</code> is sorted in non-decreasing order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Binary Searches

The median is actually the $target = \left \lceil \frac{m \times n}{2} \right \rceil$-th number after sorting.

We perform a binary search on the elements of the matrix $x$, counting the number of elements in the grid that are greater than $x$, denoted as $cnt$. If $cnt \ge target$, it means the median is on the left side of $x$ (including $x$); otherwise, it is on the right side.

The time complexity is $O(m \times \log n \times \log M)$, where $m$ and $n$ are the number of rows and columns of the grid, respectively, and $M$ is the maximum element in the grid. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        def count(x):
            return sum(bisect_right(row, x) for row in grid)

        m, n = len(grid), len(grid[0])
        target = (m * n + 1) >> 1
        return bisect_left(range(10**6 + 1), target, key=count)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
