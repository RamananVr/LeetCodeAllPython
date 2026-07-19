---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1292.Maximum%20Side%20Length%20of%20a%20Square%20with%20Sum%20Less%20than%20or%20Equal%20to%20Threshold/README_EN.md
rating: 1734
source: Weekly Contest 167 Q3
tags:
    - Array
    - Binary Search
    - Matrix
    - Prefix Sum
---

<!-- problem:start -->

# [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold)

## Description

<!-- description:start -->

<p>Given a <code>m x n</code> matrix <code>mat</code> and an integer <code>threshold</code>, return <em>the maximum side-length of a square with a sum less than or equal to </em><code>threshold</code><em> or return </em><code>0</code><em> if there is no such square</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1292.Maximum%20Side%20Length%20of%20a%20Square%20with%20Sum%20Less%20than%20or%20Equal%20to%20Threshold/images/e1.png" style="width: 335px; height: 186px;" />
<pre>
<strong>Input:</strong> mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum side length of square with sum less than or equal to 4 is 2 as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>0 &lt;= mat[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= threshold &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: 2D Prefix Sum + Binary Search

We can precompute a 2D prefix sum array $s$, where $s[i + 1][j + 1]$ represents the sum of elements in the matrix $mat$ from $(0, 0)$ to $(i, j)$. With this, we can calculate the sum of elements in any square region in $O(1)$ time.

Next, we can use binary search to find the maximum side length. We enumerate the side length $k$ of the square, and then iterate through all possible top-left positions $(i, j)$ of the square. We can calculate the sum of elements $v$ for the square. If $v \leq threshold$, it indicates that there exists a square region with side length $k$ whose sum is less than or equal to the threshold; otherwise, no such square exists for the current $k$.

The time complexity is $O(m \times n \times \log \min(m, n))$, and the space complexity is $O(m \times n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def check(k: int) -> bool:
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    v = s[i + k][j + k] - s[i][j + k] - s[i + k][j] + s[i][j]
                    if v <= threshold:
                        return True
            return False

        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat, 1):
            for j, x in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + x
        l, r = 0, min(m, n)
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
