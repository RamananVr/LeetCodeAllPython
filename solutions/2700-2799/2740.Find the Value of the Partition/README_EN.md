---
comments: true
difficulty: Medium
rating: 1301
source: Weekly Contest 350 Q2
tags:
    - Array
    - Sorting
---

<!-- problem:start -->

# [2740. Find the Value of the Partition](https://leetcode.com/problems/find-the-value-of-the-partition)

## Description

<!-- description:start -->

<p>You are given a <strong>positive</strong> integer array <code>nums</code>.</p>

<p>Partition <code>nums</code> into two arrays,&nbsp;<code>nums1</code> and <code>nums2</code>, such that:</p>

<ul>
	<li>Each element of the array <code>nums</code> belongs to either the array <code>nums1</code> or the array <code>nums2</code>.</li>
	<li>Both arrays are <strong>non-empty</strong>.</li>
	<li>The value of the partition is <strong>minimized</strong>.</li>
</ul>

<p>The value of the partition is <code>|max(nums1) - min(nums2)|</code>.</p>

<p>Here, <code>max(nums1)</code> denotes the maximum element of the array <code>nums1</code>, and <code>min(nums2)</code> denotes the minimum element of the array <code>nums2</code>.</p>

<p>Return <em>the integer denoting the value of such partition</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1. 
It can be proven that 1 is the minimum value out of all partitions.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,1,10]
<strong>Output:</strong> 9
<strong>Explanation:</strong> We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- The maximum element of the array nums1 is equal to 10.
- The minimum element of the array nums2 is equal to 1.
The value of the partition is |10 - 1| = 9.
It can be proven that 9 is the minimum value out of all partitions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

<!-- thinking:start -->

> **Thinking**
>
> Split the array into two nonempty groups and minimize the difference of their maxima. Order inside a group does not matter; only how the global extremes are separated does.
>
> After sorting, every adjacent pair is a candidate cut between the left maximum and the right minimum, and the partition value is their difference. The answer is the minimum adjacent gap.

<!-- thinking:end -->

The problem requires us to minimize the partition value. Therefore, we can sort the array and then take the minimum difference between two adjacent numbers.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(b - a for a, b in pairwise(nums))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
