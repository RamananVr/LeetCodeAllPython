---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0311.Sparse%20Matrix%20Multiplication/README_EN.md
tags:
    - Array
    - Hash Table
    - Matrix
---

<!-- problem:start -->

# [311. Sparse Matrix Multiplication 🔒](https://leetcode.com/problems/sparse-matrix-multiplication)

## Description

<!-- description:start -->

<p>Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> <code>mat1</code> of size <code>m x k</code> and <code>mat2</code> of size <code>k x n</code>, return the result of <code>mat1 x mat2</code>. You may assume that multiplication is always possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0311.Sparse%20Matrix%20Multiplication/images/mult-grid.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> [[7,0,0],[-7,0,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat1 = [[0]], mat2 = [[0]]
<strong>Output:</strong> [[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat1.length</code></li>
	<li><code>k == mat1[i].length == mat2.length</code></li>
	<li><code>n == mat2[i].length</code></li>
	<li><code>1 &lt;= m, n, k &lt;= 100</code></li>
	<li><code>-100 &lt;= mat1[i][j], mat2[i][j] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Direct Multiplication

We can directly calculate each element in the result matrix according to the definition of matrix multiplication.

The time complexity is $O(m \times n \times k)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows of matrix $mat1$ and the number of columns of matrix $mat2$ respectively, and $k$ is the number of columns of matrix $mat1$ or the number of rows of matrix $mat2$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n = len(mat1), len(mat2[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(len(mat2)):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Preprocessing

We can preprocess the sparse representation of the two matrices, i.e., $g1[i]$ represents the column index and value of all non-zero elements in the $i$th row of matrix $mat1$, and $g2[i]$ represents the column index and value of all non-zero elements in the $i$th row of matrix $mat2$.

Next, we traverse each row $i$, traverse each element $(k, x)$ in $g1[i]$, traverse each element $(j, y)$ in $g2[k]$, then $mat1[i][k] \times mat2[k][j]$ will correspond to $ans[i][j]$ in the result matrix, and we can accumulate all the results.

The time complexity is $O(m \times n \times k)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows of matrix $mat1$ and the number of columns of matrix $mat2$ respectively, and $k$ is the number of columns of matrix $mat1$ or the number of rows of matrix $mat2$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def f(mat: List[List[int]]) -> List[List[int]]:
            g = [[] for _ in range(len(mat))]
            for i, row in enumerate(mat):
                for j, x in enumerate(row):
                    if x:
                        g[i].append((j, x))
            return g

        g1 = f(mat1)
        g2 = f(mat2)
        m, n = len(mat1), len(mat2[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for k, x in g1[i]:
                for j, y in g2[k]:
                    ans[i][j] += x * y
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
