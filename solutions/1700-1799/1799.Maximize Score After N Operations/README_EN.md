---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1799.Maximize%20Score%20After%20N%20Operations/README_EN.md
rating: 2072
source: Biweekly Contest 48 Q4
tags:
    - Bit Manipulation
    - Array
    - Math
    - Dynamic Programming
    - Backtracking
    - Bitmask
    - Number Theory
---

<!-- problem:start -->

# [1799. Maximize Score After N Operations](https://leetcode.com/problems/maximize-score-after-n-operations)

## Description

<!-- description:start -->

<p>You are given <code>nums</code>, an array of positive integers of size <code>2 * n</code>. You must perform <code>n</code> operations on this array.</p>

<p>In the <code>i<sup>th</sup></code> operation <strong>(1-indexed)</strong>, you will:</p>

<ul>
	<li>Choose two elements, <code>x</code> and <code>y</code>.</li>
	<li>Receive a score of <code>i * gcd(x, y)</code>.</li>
	<li>Remove <code>x</code> and <code>y</code> from <code>nums</code>.</li>
</ul>

<p>Return <em>the maximum score you can receive after performing </em><code>n</code><em> operations.</em></p>

<p>The function <code>gcd(x, y)</code> is the greatest common divisor of <code>x</code> and <code>y</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,6,8]
<strong>Output:</strong> 11
<strong>Explanation:</strong>&nbsp;The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6]
<strong>Output:</strong> 14
<strong>Explanation:</strong>&nbsp;The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 7</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: State Compression + Dynamic Programming

We can preprocess to get the greatest common divisor of any two numbers in the array `nums`, stored in the two-dimensional array $g$, where $g[i][j]$ represents the greatest common divisor of $nums[i]$ and $nums[j]$.

Then define $f[k]$ to represent the maximum score that can be obtained when the state after the current operation is $k$. Suppose $m$ is the number of elements in the array `nums`, then there are a total of $2^m$ states, that is, the range of $k$ is $[0, 2^m - 1]$.

Enumerate all states from small to large, for each state $k$, first determine whether the number of $1$s in the binary bits of this state $cnt$ is even, if so, perform the following operations:

Enumerate the positions where the binary bits in $k$ are 1, suppose they are $i$ and $j$, then the elements at positions $i$ and $j$ can perform one operation, and the score that can be obtained at this time is $\frac{cnt}{2} \times g[i][j]$, update the maximum value of $f[k]$.

The final answer is $f[2^m - 1]$.

The time complexity is $O(2^m \times m^2)$, and the space complexity is $O(2^m)$. Here, $m$ is the number of elements in the array `nums`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        f = [0] * (1 << m)
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                g[i][j] = gcd(nums[i], nums[j])
        for k in range(1 << m):
            if (cnt := k.bit_count()) % 2 == 0:
                for i in range(m):
                    if k >> i & 1:
                        for j in range(i + 1, m):
                            if k >> j & 1:
                                f[k] = max(
                                    f[k],
                                    f[k ^ (1 << i) ^ (1 << j)] + cnt // 2 * g[i][j],
                                )
        return f[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
