---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/README_EN.md
tags:
    - Array
    - Binary Search
    - Divide and Conquer
    - Matrix
---

<!-- problem:start -->

# [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii)

## Description

<!-- description:start -->

<p>Write an efficient algorithm that searches for a value <code>target</code> in an <code>m x n</code> integer matrix <code>matrix</code>. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/images/searchgrid2.jpg" style="width: 300px; height: 300px;" />
<pre>
<strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/images/searchgrid.jpg" style="width: 300px; height: 300px;" />
<pre>
<strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers in each row are <strong>sorted</strong> in ascending order.</li>
	<li>All the integers in each column are <strong>sorted</strong> in ascending order.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

Since all elements in each row are sorted in ascending order, for each row, we can use binary search to find the first element greater than or equal to $\textit{target}$, and then check if that element is equal to $\textit{target}$. If it is equal to $\textit{target}$, it means the target value is found, and we return $\text{true}$. If it is not equal to $\textit{target}$, it means all elements in this row are less than $\textit{target}$, and we should continue searching the next row.

If all rows have been searched and the target value is not found, it means the target value does not exist, and we return $\text{false}$.

The time complexity is $O(m \times \log n)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            j = bisect_left(row, target)
            if j < len(matrix[0]) and row[j] == target:
                return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Search from Bottom-Left or Top-Right

We start the search from the bottom-left or top-right corner and move towards the top-right or bottom-left direction. Compare the current element $\textit{matrix}[i][j]$ with $\textit{target}$:

- If $\textit{matrix}[i][j] = \textit{target}$, it means the target value is found, and we return $\text{true}$.
- If $\textit{matrix}[i][j] > \textit{target}$, it means all elements in this column from the current position upwards are greater than $\textit{target}$, so we move the $i$ pointer upwards, i.e., $i \leftarrow i - 1$.
- If $\textit{matrix}[i][j] < \textit{target}$, it means all elements in this row from the current position to the right are less than $\textit{target}$, so we move the $j$ pointer to the right, i.e., $j \leftarrow j + 1$.

If the search ends and the $\textit{target}$ is not found, return $\text{false}$.

The time complexity is $O(m + n)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
