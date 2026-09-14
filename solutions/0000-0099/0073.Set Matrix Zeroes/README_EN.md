---
comments: true
difficulty: Medium
tags:
    - Array
    - Hash Table
    - Matrix
---

<!-- problem:start -->

# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>&#39;s.</p>

<p>You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0073.Set%20Matrix%20Zeroes/images/mat1.jpg" style="width: 450px; height: 169px;" />
<pre>
<strong>Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0073.Set%20Matrix%20Zeroes/images/mat2.jpg" style="width: 450px; height: 137px;" />
<pre>
<strong>Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong>Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[0].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>-2<sup>31</sup> &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>A straightforward solution using <code>O(mn)</code> space is probably a bad idea.</li>
	<li>A simple improvement uses <code>O(m + n)</code> space, but still not the best solution.</li>
	<li>Could you devise a constant space solution?</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Array Mark

<!-- thinking:start -->

> **Thinking**
>
> Zeroing a whole row and column as soon as we see a $0$ wipes zeros we have not scanned yet, and we cannot tell original zeros from new ones. Copying an $O(mn)$ matrix works, but the follow-up rejects that space. $m,n \le 200$, so two scans are fine.
>
> Record which rows and columns must be zeroed, then rewrite. An $m$-length row mark and an $n$-length column mark suffice: first pass only flags, second pass writes zeros. Extra space drops from $O(mn)$ to $O(m+n)$, still not the constant-space follow-up.

<!-- thinking:end -->

We use arrays `rows` and `cols` to mark the rows and columns to be cleared.

Then traverse the matrix again, and clear the elements in the rows and columns marked in `rows` and `cols`.

The time complexity is $O(m\times n)$, and the space complexity is $O(m+n)$. Where $m$ and $n$ are the number of rows and columns of the matrix respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Mark in Place

<!-- thinking:start -->

> **Thinking**
>
> Method 1 still spends $O(m+n)$ on mark arrays. The follow-up wants $O(1)$ extra space, and the first row and first column can play the role of $\textit{row}$ and $\textit{col}$. Those strips are both data and marks, so we save with $i0$, $j0$ whether they themselves must be zeroed, update the interior, and only then clear the first row and column — otherwise the marks get overwritten too early.

<!-- thinking:end -->

In the first method, we use an additional array to mark the rows and columns to be cleared. In fact, we can also use the first row and first column of the matrix to mark them, without creating an additional array.

Since the first row and the first column are used to mark, their values ​​may change due to the mark, so we need additional variables $i0$, $j0$ to mark whether the first row and the first column need to be cleared.

The time complexity is $O(m\times n)$, and the space complexity is $O(1)$. Where $m$ and $n$ are the number of rows and columns of the matrix respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        i0 = any(v == 0 for v in matrix[0])
        j0 = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if i0:
            for j in range(n):
                matrix[0][j] = 0
        if j0:
            for i in range(m):
                matrix[i][0] = 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
