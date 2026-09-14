---
comments: true
difficulty: Easy
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array)

## Description

<!-- description:start -->

<p>Given a non-empty array of non-negative integers <code>nums</code>, the <b>degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>

<p>Your task is to find the smallest possible length of a (contiguous) subarray of <code>nums</code>, that has the same degree as <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3,1,4,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length</code> will be between 1 and 50,000.</li>
	<li><code>nums[i]</code> will be an integer between 0 and 49,999.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> The degree is the maximum frequency. A shortest subarray with the same degree must cover the first and last occurrence of some mode.
>
> Count frequencies and record endpoints. For values that attain the degree, take the minimum $right-left+1$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        degree = cnt.most_common()[0][1]
        left, right = {}, {}
        for i, v in enumerate(nums):
            if v not in left:
                left[v] = i
            right[v] = i
        ans = inf
        for v in nums:
            if cnt[v] == degree:
                t = right[v] - left[v] + 1
                if ans > t:
                    ans = t
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Method 1 records endpoints in one pass. We can also collect the modes first and scan first/last indices per mode. The helpers are longer, the complexity is the same.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
