---
comments: true
difficulty: Hard
rating: 1999
source: Weekly Contest 495 Q3
tags:
    - Array
    - Math
    - Enumeration
    - Sorting
---

<!-- problem:start -->

# [3886. Sum of Sortable Integers](https://leetcode.com/problems/sum-of-sortable-integers)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>An integer <code>k</code> is called <strong>sortable</strong> if <code>k</code> <strong>divides</strong> <code>n</code> and you can sort <code>nums</code> in <strong>non-decreasing</strong> order by sequentially performing the following operations:</p>

<ul>
	<li>Partition <code>nums</code> into <strong>consecutive <span data-keyword="subarray-nonempty">subarrays</span></strong> of length <code>k</code>.</li>
	<li><strong>Cyclically rotate each subarray independently</strong> any number of times to the left or to the right.</li>
</ul>

<p>Return an integer denoting the sum of all possible sortable integers <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>For <code>n = 3</code>, possible divisors are 1 and 3.</li>
	<li>For <code>k = 1</code>: each subarray has one element. No rotation can sort the array.</li>
	<li>For <code>k = 3</code>: the single subarray <code>[3, 1, 2]</code> can be rotated once to produce <code>[1, 2, 3]</code>, which is sorted.</li>
	<li>Only <code>k = 3</code> is sortable. Hence, the answer is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [7,6,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>n = 3</code>, possible divisors are 1 and 3.</li>
	<li>For <code>k = 1</code>: each subarray has one element. No rotation can sort the array.</li>
	<li>For <code>k = 3</code>: the single subarray <code>[7, 6, 5]</code> cannot be rotated into non-decreasing order.</li>
	<li>No <code>k</code> is sortable. Hence, the answer is 0.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>For <code>n = 2</code>, possible divisors are 1 and 2.</li>
	<li>Since <code>[5, 8]</code> is already sorted, every divisor is sortable. Hence, the answer is <code>1 + 2 = 3</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Simulation

<!-- thinking:start -->

> **Thinking**
>
> Trying every rotation of every block for each divisor $k$ costs $O(k^2)$ per block, which is too slow when $n \le 10^5$.
>
> Those repeated rotations are the bottleneck. A block can be cycled into non-decreasing order exactly when it has at most one strict circular descent. After every block is rotated that way, the concatenation is globally non-decreasing exactly when, at every boundary, the maximum on the left does not exceed the minimum on the right.
>
> Both quantities sit on the block boundaries.
>
> We precompute the prefix maximum, the suffix minimum, and a prefix sum of adjacent descents, then enumerate the divisors of $n$ and judge each block in $O(1)$ time.

<!-- thinking:end -->

First build three auxiliary arrays. $\textit{prefMax}[i]$ is the maximum of $\textit{nums}[0..i-1]$, with $\textit{prefMax}[0] = 0$. $\textit{suffMin}[i]$ is the minimum of $\textit{nums}[i..n-1]$. $\textit{prefDrop}[i]$ counts how many index pairs $(0,1),\ldots,(i-1,i)$ satisfy $\textit{nums}[j-1] > \textit{nums}[j]$.

Then enumerate every divisor $k$ of $n$ and split the array into blocks of length $k$. For a block starting at $i$, the number of adjacent descents inside the block is $\textit{prefDrop}[i+k-1] - \textit{prefDrop}[i]$, plus one more when $\textit{nums}[i+k-1] > \textit{nums}[i]$. If this total is at most $1$ and $\textit{prefMax}[i] \le \textit{suffMin}[i]$, the block can be cyclically rotated onto the already ordered prefix. When every block passes, add $k$ to the answer.

The time complexity is $O(n + \sigma(n))$, and the space complexity is $O(n)$, where $n$ is the length of the array and $\sigma(n)$ is the sum of all positive divisors of $n$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        pref_max = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref_max[i + 1] = max(pref_max[i], x)
        suff_min = [10**9] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (nums[i - 1] > nums[i])

        def check(k: int) -> bool:
            for start in range(0, n, k):
                end = start + k - 1
                drops = pref_drop[end] - pref_drop[start]
                if nums[end] > nums[start]:
                    drops += 1
                if drops > 1 or pref_max[start] > suff_min[start]:
                    return False
            return True

        ans = 0
        i = 1
        while i <= n // i:
            if n % i == 0:
                if check(i):
                    ans += i
                other = n // i
                if i != other and check(other):
                    ans += other
            i += 1
        return ans
```

<!-- tabs:end -->
<!-- solution:end -->

<!-- problem:end -->
