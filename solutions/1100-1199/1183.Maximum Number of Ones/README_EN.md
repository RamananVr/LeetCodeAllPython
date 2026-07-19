---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1183.Maximum%20Number%20of%20Ones/README_EN.md
rating: 2366
source: Biweekly Contest 8 Q4
tags:
    - Greedy
    - Math
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1183. Maximum Number of Ones 🔒](https://leetcode.com/problems/maximum-number-of-ones)

## Description

<!-- description:start -->

<p>Consider a matrix <code>M</code> with dimensions <code>width * height</code>, such that every cell has value <code>0</code>&nbsp;or <code>1</code>, and any <strong>square</strong>&nbsp;sub-matrix of <code>M</code> of size <code>sideLength * sideLength</code>&nbsp;has at most <code>maxOnes</code>&nbsp;ones.</p>

<p>Return the maximum possible number of ones that the matrix <code>M</code> can have.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> width = 3, height = 3, sideLength = 2, maxOnes = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong>
In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> width = 3, height = 3, sideLength = 2, maxOnes = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong>
[1,0,1]
[1,0,1]
[1,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= width, height &lt;= 100</code></li>
	<li><code>1 &lt;= sideLength &lt;= width, height</code></li>
	<li><code>0 &lt;= maxOnes &lt;= sideLength * sideLength</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Count Equivalent Positions

For convenience, let's denote $x = sideLength$.

Consider a $x \times x$ square, we need to select at most $maxOnes$ points inside the square and set them to 1. Note that when the point at coordinate $(i, j)$ is selected, all points at coordinates $(i\pm k_1 \times x, j\pm k_2 \times x)$ can be equivalently set to 1. Therefore, we calculate the number of equivalent positions of the coordinate $(i, j)$ in the matrix, and select the top $maxOnes$ with the most quantities.

The time complexity is $O(m \times n)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumNumberOfOnes(
        self, width: int, height: int, sideLength: int, maxOnes: int
    ) -> int:
        x = sideLength
        cnt = [0] * (x * x)
        for i in range(width):
            for j in range(height):
                k = (i % x) * x + (j % x)
                cnt[k] += 1
        cnt.sort(reverse=True)
        return sum(cnt[:maxOnes])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
