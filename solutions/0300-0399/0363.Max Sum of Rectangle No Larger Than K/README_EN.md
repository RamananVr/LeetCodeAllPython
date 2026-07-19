---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0363.Max%20Sum%20of%20Rectangle%20No%20Larger%20Than%20K/README_EN.md
tags:
    - Array
    - Binary Search
    - Matrix
    - Ordered Set
    - Prefix Sum
---

<!-- problem:start -->

# [363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> matrix <code>matrix</code> and an integer <code>k</code>, return <em>the max sum of a rectangle in the matrix such that its sum is no larger than</em> <code>k</code>.</p>

<p>It is <strong>guaranteed</strong> that there will be a rectangle with a sum no larger than <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0363.Max%20Sum%20of%20Rectangle%20No%20Larger%20Than%20K/images/sum-grid.jpg" style="width: 255px; height: 176px;" />
<pre>
<strong>Input:</strong> matrix = [[1,0,1],[0,-2,3]], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[2,2,-1]], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
	<li><code>-10<sup>5</sup> &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the number of rows is much larger than the number of columns?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate Boundaries + Ordered Set

We can enumerate the upper and lower boundaries $i$ and $j$ of the rectangle, then calculate the sum of the elements in each column within this boundary, and record it in the array $nums$. The problem is transformed into how to find the maximum subarray sum not exceeding $k$ in the array $nums$.

We can use an ordered set to quickly find the maximum value less than or equal to $x$, thereby obtaining a subarray with the maximum subarray sum not exceeding $k$.

The time complexity is $O(m^2 \times n \times \log n)$, and the space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -inf
        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for h in range(n):
                    nums[h] += matrix[j][h]
                s = 0
                ts = SortedSet([0])
                for x in nums:
                    s += x
                    p = ts.bisect_left(s - k)
                    if p != len(ts):
                        ans = max(ans, s - ts[p])
                    ts.add(s)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
