---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2809.Minimum%20Time%20to%20Make%20Array%20Sum%20At%20Most%20x/README_EN.md
rating: 2978
source: Biweekly Contest 110 Q4
tags:
    - Array
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [2809. Minimum Time to Make Array Sum At Most x](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code> of equal length. Every second, for all indices <code>0 &lt;= i &lt; nums1.length</code>, value of <code>nums1[i]</code> is incremented by <code>nums2[i]</code>. <strong>After</strong> this is done, you can do the following operation:</p>

<ul>
	<li>Choose an index <code>0 &lt;= i &lt; nums1.length</code> and make <code>nums1[i] = 0</code>.</li>
</ul>

<p>You are also given an integer <code>x</code>.</p>

<p>Return <em>the <strong>minimum</strong> time in which you can make the sum of all elements of </em><code>nums1</code><em> to be<strong> less than or equal</strong> to </em><code>x</code>, <em>or </em><code>-1</code><em> if this is not possible.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3], nums2 = [1,2,3], x = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
For the 1st second, we apply the operation on i = 0. Therefore nums1 = [0,2+2,3+3] = [0,4,6]. 
For the 2nd second, we apply the operation on i = 1. Therefore nums1 = [0+1,0,6+3] = [1,0,9]. 
For the 3rd second, we apply the operation on i = 2. Therefore nums1 = [1+1,0+2,0] = [2,2,0]. 
Now sum of nums1 = 4. It can be shown that these operations are optimal, so we return 3.

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3], nums2 = [3,3,3], x = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that the sum of nums1 will always be greater than x, no matter which operations are performed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><font face="monospace">1 &lt;= nums1.length &lt;= 10<sup>3</sup></font></code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 10<sup>3</sup></code></li>
	<li><code>0 &lt;= nums2[i] &lt;= 10<sup>3</sup></code></li>
	<li><code>nums1.length == nums2.length</code></li>
	<li><code>0 &lt;= x &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Dynamic Programming

We notice that if we operate on the same number multiple times, only the last operation is meaningful, and the rest of the operations on that number will only increase the other numbers. Therefore, we operate on each number at most once, that is to say, the number of operations is within $[0,..n]$.

Let's assume that we have performed $j$ operations, and the indices of the numbers operated on are $i_1, i_2, \cdots, i_j$. For these $j$ operations, the value that each operation can reduce the sum of array elements is:

$$
\begin{aligned}
& d_1 = nums_1[i_1] + nums_2[i_1] \times 1 \\
& d_2 = nums_1[i_2] + nums_2[i_2] \times 2 \\
& \cdots \\
& d_j = nums_1[i_j] + nums_2[i_j] \times j
\end{aligned}
$$

From a greedy perspective, in order to maximize the reduction of the sum of array elements, we should let the larger elements in $nums_2$ be operated on as late as possible. Therefore, we can sort $nums_1$ and $nums_2$ in ascending order of the element values in $nums_2$.

Next, we consider the implementation of dynamic programming. We use $f[i][j]$ to represent the maximum value that can reduce the sum of array elements for the first $i$ elements of the array $nums_1$ with $j$ operations. We can get the following state transition equation:

$$
f[i][j] = \max \{f[i-1][j], f[i-1][j-1] + nums_1[i] + nums_2[i] \times j\}
$$

Finally, we enumerate $j$ and find the smallest $j$ that satisfies $s_1 + s_2 \times j - f[n][j] \le x$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i, (a, b) in enumerate(sorted(zip(nums1, nums2), key=lambda z: z[1]), 1):
            for j in range(n + 1):
                f[i][j] = f[i - 1][j]
                if j > 0:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + a + b * j)
        s1 = sum(nums1)
        s2 = sum(nums2)
        for j in range(n + 1):
            if s1 + s2 * j - f[n][j] <= x:
                return j
        return -1
```

<!-- tabs:end -->

We notice that the state $f[i][j]$ is only related to $f[i-1][j]$ and $f[i-1][j-1]$, so we can optimize the first dimension and reduce the space complexity to $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        f = [0] * (n + 1)
        for a, b in sorted(zip(nums1, nums2), key=lambda z: z[1]):
            for j in range(n, 0, -1):
                f[j] = max(f[j], f[j - 1] + a + b * j)
        s1 = sum(nums1)
        s2 = sum(nums2)
        for j in range(n + 1):
            if s1 + s2 * j - f[j] <= x:
                return j
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
