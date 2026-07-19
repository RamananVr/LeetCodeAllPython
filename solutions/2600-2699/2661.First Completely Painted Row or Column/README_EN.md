---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2661.First%20Completely%20Painted%20Row%20or%20Column/README_EN.md
rating: 1502
source: Weekly Contest 343 Q2
tags:
    - Array
    - Hash Table
    - Matrix
---

<!-- problem:start -->

# [2661. First Completely Painted Row or Column](https://leetcode.com/problems/first-completely-painted-row-or-column)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>arr</code>, and an <code>m x n</code> integer <strong>matrix</strong> <code>mat</code>. <code>arr</code> and <code>mat</code> both contain <strong>all</strong> the integers in the range <code>[1, m * n]</code>.</p>

<p>Go through each index <code>i</code> in <code>arr</code> starting from index <code>0</code> and paint the cell in <code>mat</code> containing the integer <code>arr[i]</code>.</p>

<p>Return <em>the smallest index</em> <code>i</code> <em>at which either a row or a column will be completely painted in</em> <code>mat</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2661.First%20Completely%20Painted%20Row%20or%20Column/images/image explanation for example 1" /><img alt="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2661.First%20Completely%20Painted%20Row%20or%20Column/images/image explanation for example 1" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2661.First%20Completely%20Painted%20Row%20or%20Column/images/grid1.jpg" style="width: 321px; height: 81px;" />
<pre>
<strong>Input:</strong> arr = [1,3,4,2], mat = [[1,4],[2,3]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="image explanation for example 2" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2600-2699/2661.First%20Completely%20Painted%20Row%20or%20Column/images/grid2.jpg" style="width: 601px; height: 121px;" />
<pre>
<strong>Input:</strong> arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The second column becomes fully painted at arr[3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n = mat[i].length</code></li>
	<li><code>arr.length == m * n</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i], mat[r][c] &lt;= m * n</code></li>
	<li>All the integers of <code>arr</code> are <strong>unique</strong>.</li>
	<li>All the integers of <code>mat</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Array Counting

We use a hash table $idx$ to record the position of each element in the matrix $mat$, that is $idx[mat[i][j]] = (i, j)$, and define two arrays $row$ and $col$ to record the number of colored elements in each row and each column respectively.

Traverse the array $arr$. For each element $arr[k]$, we find its position $(i, j)$ in the matrix $mat$, and then add $row[i]$ and $col[j]$ by one. If $row[i] = n$ or $col[j] = m$, it means that the $i$-th row or the $j$-th column has been colored, so $arr[k]$ is the element we are looking for, and we return $k$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here $m$ and $n$ are the number of rows and columns of the matrix $mat$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        idx = {}
        for i in range(m):
            for j in range(n):
                idx[mat[i][j]] = (i, j)
        row = [0] * m
        col = [0] * n
        for k in range(len(arr)):
            i, j = idx[arr[k]]
            row[i] += 1
            col[j] += 1
            if row[i] == n or col[j] == m:
                return k
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
