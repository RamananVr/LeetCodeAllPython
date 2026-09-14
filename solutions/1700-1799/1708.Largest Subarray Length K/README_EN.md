---
comments: true
difficulty: Easy
tags:
    - Greedy
    - Array
---

<!-- problem:start -->

# [1708. Largest Subarray Length K 🔒](https://leetcode.com/problems/largest-subarray-length-k)

## Description

<!-- description:start -->

<p>An array <code>A</code> is larger than some array <code>B</code> if for the first index <code>i</code> where <code>A[i] != B[i]</code>, <code>A[i] &gt; B[i]</code>.</p>

<p>For example, consider <code>0</code>-indexing:</p>

<ul>
	<li><code>[1,3,2,4] &gt; [1,2,2,4]</code>, since at index <code>1</code>, <code>3 &gt; 2</code>.</li>
	<li><code>[1,4,4,4] &lt; [2,1,1,1]</code>, since at index <code>0</code>, <code>1 &lt; 2</code>.</li>
</ul>

<p>A subarray is a contiguous subsequence of the array.</p>

<p>Given an integer array <code>nums</code> of <strong>distinct</strong> integers, return the <strong>largest</strong> subarray of <code>nums</code> of length <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,5,2,3], k = 3
<strong>Output:</strong> [5,2,3]
<strong>Explanation:</strong> The subarrays of size 3 are: [1,4,5], [4,5,2], and [5,2,3].
Of these, [5,2,3] is the largest.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,5,2,3], k = 4
<strong>Output:</strong> [4,5,2,3]
<strong>Explanation:</strong> The subarrays of size 4 are: [1,4,5,2], and [4,5,2,3].
Of these, [4,5,2,3] is the largest.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,5,2,3], k = 1
<strong>Output:</strong> [5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> What if the integers in <code>nums</code> are not distinct?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> Among subarrays of length $k$, the lexicographically largest is decided by its first element, since all values are distinct.
>
> Valid starts lie in $[0,n-k]$. Take the index $i$ of the maximum in that range; the answer is $nums[i..i+k)$. One scan suffices.

<!-- thinking:end -->

All integers in the array are distinct, so we can first find the index of the maximum element in the range $[0,..n-k]$, and then take $k$ elements starting from this index.

The time complexity is $O(n)$, where $n$ is the length of the array. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        i = nums.index(max(nums[: len(nums) - k + 1]))
        return nums[i : i + k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
