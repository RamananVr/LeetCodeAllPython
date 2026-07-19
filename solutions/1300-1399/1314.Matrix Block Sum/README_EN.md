---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1314.Matrix%20Block%20Sum/README_EN.md
rating: 1483
source: Biweekly Contest 17 Q2
tags:
    - Array
    - Matrix
    - Prefix Sum
---

<!-- problem:start -->

# [1314. Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum)

## Description

<!-- description:start -->

<p>Given a <code>m x n</code> matrix <code>mat</code> and an integer <code>k</code>, return <em>a matrix</em> <code>answer</code> <em>where each</em> <code>answer[i][j]</code> <em>is the sum of all elements</em> <code>mat[r][c]</code> <em>for</em>:</p>

<ul>
	<li><code>i - k &lt;= r &lt;= i + k,</code></li>
	<li><code>j - k &lt;= c &lt;= j + k</code>, and</li>
	<li><code>(r, c)</code> is a valid position in the matrix.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>Output:</strong> [[12,21,16],[27,45,33],[24,39,28]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
<strong>Output:</strong> [[45,45,45],[45,45,45],[45,45,45]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;mat.length</code></li>
	<li><code>n ==&nbsp;mat[i].length</code></li>
	<li><code>1 &lt;= m, n, k &lt;= 100</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two-Dimensional Prefix Sum

This problem is a template for two-dimensional prefix sum.

We define $s[i][j]$ as the sum of the elements in the first $i$ rows and the first $j$ columns of the matrix $mat$. The calculation formula for $s[i][j]$ is:

$$
s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + mat[i-1][j-1]
$$

In this way, we can quickly calculate the sum of elements in any rectangular area through the $s$ array.

For a rectangular area with the upper left coordinate $(x_1, y_1)$ and the lower right coordinate $(x_2, y_2)$, we can calculate the sum of its elements through the $s$ array:

$$
s[x_2+1][y_2+1] - s[x_1][y_2+1] - s[x_2+1][y_1] + s[x_1][y_1]
$$

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat, 1):
            for j, x in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + x
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1 = max(i - k, 0), max(j - k, 0)
                x2, y2 = min(m - 1, i + k), min(n - 1, j + k)
                ans[i][j] = (
                    s[x2 + 1][y2 + 1] - s[x1][y2 + 1] - s[x2 + 1][y1] + s[x1][y1]
                )
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
