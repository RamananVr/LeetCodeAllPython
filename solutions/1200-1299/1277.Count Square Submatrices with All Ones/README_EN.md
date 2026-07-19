---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1277.Count%20Square%20Submatrices%20with%20All%20Ones/README_EN.md
rating: 1613
source: Weekly Contest 165 Q3
tags:
    - Array
    - Dynamic Programming
    - Matrix
---

<!-- problem:start -->

# [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones)

## Description

<!-- description:start -->

<p>Given a <code>m * n</code> matrix of ones and zeros, return how many <strong>square</strong> submatrices have all ones.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
There are <strong>10</strong> squares of side 1.
There are <strong>4</strong> squares of side 2.
There is  <strong>1</strong> square of side 3.
Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
There are <b>6</b> squares of side 1.  
There is <strong>1</strong> square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 300</code></li>
	<li><code>1 &lt;= arr[0].length&nbsp;&lt;= 300</code></li>
	<li><code>0 &lt;= arr[i][j] &lt;= 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the side length of the square submatrix with $(i,j)$ as the bottom-right corner. Initially $f[i][j] = 0$, and the answer is $\sum_{i,j} f[i][j]$.

Consider how to perform state transition for $f[i][j]$.

- When $\text{matrix}[i][j] = 0$, we have $f[i][j] = 0$.
- When $\text{matrix}[i][j] = 1$, the value of state $f[i][j]$ depends on the values of the three positions above, left, and top-left:
    - If $i = 0$ or $j = 0$, then $f[i][j] = 1$.
    - Otherwise $f[i][j] = \min(f[i-1][j-1], f[i-1][j], f[i][j-1]) + 1$.

The answer is $\sum_{i,j} f[i][j]$.

Time complexity $O(m \times n)$, space complexity $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns of the matrix respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == 0:
                    continue
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
                ans += f[i][j]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
