---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2832.Maximal%20Range%20That%20Each%20Element%20Is%20Maximum%20in%20It/README_EN.md
tags:
    - Stack
    - Array
    - Monotonic Stack
---

<!-- problem:start -->

# [2832. Maximal Range That Each Element Is Maximum in It 🔒](https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array <code>nums</code> of <b>distinct </b>integers.</p>

<p>Let us define a <strong>0-indexed </strong>array <code>ans</code> of the same length as <code>nums</code> in the following way:</p>

<ul>
	<li><code>ans[i]</code> is the <strong>maximum</strong> length of a subarray <code>nums[l..r]</code>, such that the maximum element in that subarray is equal to <code>nums[i]</code>.</li>
</ul>

<p>Return<em> the array </em><code>ans</code>.</p>

<p><strong>Note</strong> that a <strong>subarray</strong> is a contiguous part of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,4,3,6]
<strong>Output:</strong> [1,4,2,1,5]
<strong>Explanation:</strong> For nums[0] the longest subarray in which 1 is the maximum is nums[0..0] so ans[0] = 1.
For nums[1] the longest subarray in which 5 is the maximum is nums[0..3] so ans[1] = 4.
For nums[2] the longest subarray in which 4 is the maximum is nums[2..3] so ans[2] = 2.
For nums[3] the longest subarray in which 3 is the maximum is nums[3..3] so ans[3] = 1.
For nums[4] the longest subarray in which 6 is the maximum is nums[0..4] so ans[4] = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> For nums[i] the longest subarray in which it&#39;s the maximum is nums[0..i] so ans[i] = i + 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li>All elements in <code>nums</code> are distinct.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack

This problem is a template for monotonic stack. We only need to use the monotonic stack to find the position of the first element larger than $nums[i]$ on the left and right, denoted as $left[i]$ and $right[i]$. Then, the interval length with $nums[i]$ as the maximum value is $right[i] - left[i] - 1$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, x in enumerate(nums):
            while stk and nums[stk[-1]] <= x:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        return [r - l - 1 for l, r in zip(left, right)]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
