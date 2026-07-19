---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0562.Longest%20Line%20of%20Consecutive%20One%20in%20Matrix/README_EN.md
tags:
    - Array
    - Dynamic Programming
    - Matrix
---

<!-- problem:start -->

# [562. Longest Line of Consecutive One in Matrix 🔒](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the length of the longest line of consecutive one in the matrix</em>.</p>

<p>The line could be horizontal, vertical, diagonal, or anti-diagonal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0562.Longest%20Line%20of%20Consecutive%20One%20in%20Matrix/images/long1-grid.jpg" style="width: 333px; height: 253px;" />
<pre>
<strong>Input:</strong> mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0562.Longest%20Line%20of%20Consecutive%20One%20in%20Matrix/images/long2-grid.jpg" style="width: 333px; height: 253px;" />
<pre>
<strong>Input:</strong> mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j][k]$ to represent the length of the longest consecutive $1$s ending at $(i, j)$ in direction $k$. The value range of $k$ is $0, 1, 2, 3$, representing horizontal, vertical, diagonal, and anti-diagonal directions, respectively.

> We can also use four 2D arrays to represent the length of the longest consecutive $1$s in the four directions.

We traverse the matrix, and when we encounter $1$, we update the value of $f[i][j][k]$. For each position $(i, j)$, we only need to update the values in its four directions. Then we update the answer.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$, where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        a = [[0] * (n + 2) for _ in range(m + 2)]
        b = [[0] * (n + 2) for _ in range(m + 2)]
        c = [[0] * (n + 2) for _ in range(m + 2)]
        d = [[0] * (n + 2) for _ in range(m + 2)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i - 1][j - 1]:
                    a[i][j] = a[i - 1][j] + 1
                    b[i][j] = b[i][j - 1] + 1
                    c[i][j] = c[i - 1][j - 1] + 1
                    d[i][j] = d[i - 1][j + 1] + 1
                    ans = max(ans, a[i][j], b[i][j], c[i][j], d[i][j])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
