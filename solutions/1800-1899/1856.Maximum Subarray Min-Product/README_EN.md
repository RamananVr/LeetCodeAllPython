---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1856.Maximum%20Subarray%20Min-Product/README_EN.md
rating: 2051
source: Weekly Contest 240 Q3
tags:
    - Stack
    - Array
    - Prefix Sum
    - Monotonic Stack
---

<!-- problem:start -->

# [1856. Maximum Subarray Min-Product](https://leetcode.com/problems/maximum-subarray-min-product)

## Description

<!-- description:start -->

<p>The <strong>min-product</strong> of an array is equal to the <strong>minimum value</strong> in the array <strong>multiplied by</strong> the array&#39;s <strong>sum</strong>.</p>

<ul>
	<li>For example, the array <code>[3,2,5]</code> (minimum value is <code>2</code>) has a min-product of <code>2 * (3+2+5) = 2 * 10 = 20</code>.</li>
</ul>

<p>Given an array of integers <code>nums</code>, return <em>the <strong>maximum min-product</strong> of any <strong>non-empty subarray</strong> of </em><code>nums</code>. Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>Note that the min-product should be maximized <strong>before</strong> performing the modulo operation. Testcases are generated such that the maximum min-product <strong>without</strong> modulo will fit in a <strong>64-bit signed integer</strong>.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,<u>2,3,2</u>]
<strong>Output:</strong> 14
<strong>Explanation:</strong> The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,<u>3,3</u>,1,2]
<strong>Output:</strong> 18
<strong>Explanation:</strong> The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,<u>5,6,4</u>,2]
<strong>Output:</strong> 60
<strong>Explanation:</strong> The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack + Prefix Sum

We can enumerate each element $nums[i]$ as the minimum value of the subarray, and find the left and right boundaries $left[i]$ and $right[i]$ of the subarray. Where $left[i]$ represents the first position strictly less than $nums[i]$ on the left side of $i$, and $right[i]$ represents the first position less than or equal to $nums[i]$ on the right side of $i$.

To conveniently calculate the sum of the subarray, we can preprocess the prefix sum array $s$, where $s[i]$ represents the sum of the first $i$ elements of $nums$.

Then the minimum product with $nums[i]$ as the minimum value of the subarray is $nums[i] \times (s[right[i]] - s[left[i] + 1])$. We can enumerate each element $nums[i]$, find the minimum product with $nums[i]$ as the minimum value of the subarray, and then take the maximum value.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, x in enumerate(nums):
            while stk and nums[stk[-1]] >= x:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] > nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        s = list(accumulate(nums, initial=0))
        mod = 10**9 + 7
        return max((s[right[i]] - s[left[i] + 1]) * x for i, x in enumerate(nums)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
