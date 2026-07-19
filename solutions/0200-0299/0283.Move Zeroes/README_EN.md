---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0283.Move%20Zeroes/README_EN.md
tags:
    - Array
    - Two Pointers
---

<!-- problem:start -->

# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use a pointer $k$ to record the current position to insert, initially $k = 0$.

Then we iterate through the array $\textit{nums}$, and each time we encounter a non-zero number, we swap it with $\textit{nums}[k]$ and increment $k$ by 1.

This way, we can ensure that the first $k$ elements of $\textit{nums}$ are non-zero, and their relative order is the same as in the original array.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i, x in enumerate(nums):
            if x:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
