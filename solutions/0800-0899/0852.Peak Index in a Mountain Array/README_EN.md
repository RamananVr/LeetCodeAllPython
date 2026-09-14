---
comments: true
difficulty: Medium
tags:
    - Array
    - Binary Search
    - Ternary Search
---

<!-- problem:start -->

# [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array)

## Description

<!-- description:start -->

<p>You are given an integer <strong>mountain</strong> array <code>arr</code> of length <code>n</code> where the values increase to a <strong>peak element</strong> and then decrease.</p>

<p>Return the index of the peak element.</p>

<p>Your task is to solve it in <code>O(log(n))</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [0,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [0,2,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [0,10,5,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>arr</code> is <strong>guaranteed</strong> to be a mountain array.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> The array rises strictly then falls strictly; we need the peak index. A linear scan works, but $n\le 10^5$ and the peak test is monotone: left of the peak $arr[i]<arr[i+1]$, right of it the opposite.
>
> Binary search $[1,n-2]$: if $arr[mid]>arr[mid+1]$ the peak is in the left half (including $mid$), otherwise in the right. The left endpoint is the peak.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
