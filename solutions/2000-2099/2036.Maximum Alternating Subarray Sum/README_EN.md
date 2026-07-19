---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2036.Maximum%20Alternating%20Subarray%20Sum/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [2036. Maximum Alternating Subarray Sum 🔒](https://leetcode.com/problems/maximum-alternating-subarray-sum)

## Description

<!-- description:start -->

<p>A <strong>subarray</strong> of a <strong>0-indexed</strong> integer array is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>The <strong>alternating subarray sum</strong> of a subarray that ranges from index <code>i</code> to <code>j</code> (<strong>inclusive</strong>, <code>0 &lt;= i &lt;= j &lt; nums.length</code>) is <code>nums[i] - nums[i+1] + nums[i+2] - ... +/- nums[j]</code>.</p>

<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, return <em>the <strong>maximum alternating subarray sum</strong> of any subarray of </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,-1,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
The subarray [3,-1,1] has the largest alternating subarray sum.
The alternating subarray sum is 3 - (-1) + 1 = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The subarrays [2], [2,2,2], and [2,2,2,2,2] have the largest alternating subarray sum.
The alternating subarray sum of [2] is 2.
The alternating subarray sum of [2,2,2] is 2 - 2 + 2 = 2.
The alternating subarray sum of [2,2,2,2,2] is 2 - 2 + 2 - 2 + 2 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
There is only one non-empty subarray, which is [1].
The alternating subarray sum is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f$ as the maximum sum of the alternating subarray ending with $nums[i]$, and define $g$ as the maximum sum of the alternating subarray ending with $-nums[i]$. Initially, both $f$ and $g$ are $-\infty$.

Next, we traverse the array $nums$. For position $i$, we need to maintain the values of $f$ and $g$, i.e., $f = \max(g, 0) + nums[i]$, and $g = f - nums[i]$. The answer is the maximum value among all $f$ and $g$.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        ans = f = g = -inf
        for x in nums:
            f, g = max(g, 0) + x, f - x
            ans = max(ans, f, g)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
