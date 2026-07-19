---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0915.Partition%20Array%20into%20Disjoint%20Intervals/README_EN.md
tags:
    - Array
---

<!-- problem:start -->

# [915. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, partition it into two (contiguous) subarrays <code>left</code> and <code>right</code> so that:</p>

<ul>
	<li>Every element in <code>left</code> is less than or equal to every element in <code>right</code>.</li>
	<li><code>left</code> and <code>right</code> are non-empty.</li>
	<li><code>left</code> has the smallest possible size.</li>
</ul>

<p>Return <em>the length of </em><code>left</code><em> after such a partitioning</em>.</p>

<p>Test cases are generated such that partitioning exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,0,3,8,6]
<strong>Output:</strong> 3
<strong>Explanation:</strong> left = [5,0,3], right = [8,6]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,0,6,12]
<strong>Output:</strong> 4
<strong>Explanation:</strong> left = [1,1,1,0], right = [6,12]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li>There is at least one valid answer for the given input.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Maximum + Suffix Minimum

To satisfy the requirements of the problem after partitioning into two subarrays, we need to ensure that the "maximum value of the array prefix" is less than or equal to the "minimum value of the array suffix".

Therefore, we can first preprocess the minimum value of the array suffix and record it in the `mi` array.

Then, we traverse the array from front to back, maintaining the maximum value `mx` of the array prefix. When we traverse to a certain position, if the maximum value of the array prefix is less than or equal to the minimum value of the array suffix, then the current position is the dividing point of the partition, and we can return it directly.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array `nums`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        mi = [inf] * (n + 1)
        for i in range(n - 1, -1, -1):
            mi[i] = min(nums[i], mi[i + 1])
        mx = 0
        for i, v in enumerate(nums, 1):
            mx = max(mx, v)
            if mx <= mi[i]:
                return i
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
