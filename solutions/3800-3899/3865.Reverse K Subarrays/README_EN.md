---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3865.Reverse%20K%20Subarrays/README_EN.md
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [3865. Reverse K Subarrays 🔒](https://leetcode.com/problems/reverse-k-subarrays)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>You must <strong>partition</strong> the array into <code>k</code> contiguous subarrays of <strong>equal</strong> length and <strong>reverse</strong> each subarray.</p>

<p>It is guaranteed that <code>n</code> is divisible by <code>k</code>.</p>

<p>Return the resulting array after performing the above operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,3,5,6], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,1,3,4,6,5]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The array is partitioned into <code>k = 3</code> subarrays: <code>[1, 2]</code>, <code>[4, 3]</code>, and <code>[5, 6]</code>.</li>
	<li>After reversing each subarray: <code>[2, 1]</code>, <code>[3, 4]</code>, and <code>[6, 5]</code>.</li>
	<li>Combining them gives the final array <code>[2, 1, 3, 4, 6, 5]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,4,2], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,4,4,5]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The array is partitioned into <code>k = 1</code> subarray: <code>[5, 4, 4, 2]</code>.</li>
	<li>Reversing it produces <code>[2, 4, 4, 5]</code>, which is the final array.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li><code>n</code> is divisible by <code>k</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

Since we need to partition the array into $k$ subarrays of equal length, the length of each subarray is $m = \frac{n}{k}$. We can use a loop to traverse the array with a step size of $m$, and in each iteration, reverse the current subarray.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(1)$, as we only use a constant amount of extra space.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        m = n // k
        for i in range(0, n, m):
            nums[i : i + m] = nums[i : i + m][::-1]
        return nums
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
