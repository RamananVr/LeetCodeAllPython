---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1243.Array%20Transformation/README_EN.md
rating: 1558
source: Biweekly Contest 12 Q2
tags:
    - Array
    - Simulation
---

<!-- problem:start -->

# [1243. Array Transformation 🔒](https://leetcode.com/problems/array-transformation)

## Description

<!-- description:start -->

<p>Given an initial array <code>arr</code>, every day you produce a new array using the array of the previous day.</p>

<p>On the <code>i</code>-th day, you do the following operations on the array of day&nbsp;<code>i-1</code>&nbsp;to produce the array of day <code>i</code>:</p>

<ol>
	<li>If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.</li>
	<li>If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.</li>
	<li>The first&nbsp;and last elements never change.</li>
</ol>

<p>After some days, the array does not change. Return that final array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [6,2,3,4]
<strong>Output:</strong> [6,3,3,4]
<strong>Explanation: </strong>
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,6,3,4,3,5]
<strong>Output:</strong> [1,4,4,4,4,5]
<strong>Explanation: </strong>
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

Simulate each day. For each element, if it is greater than its left and right neighbors, it decreases by 1, otherwise, it increases by 1. If the array no longer changes on a certain day, return that array.

The time complexity is $O(n \times m)$, and the space complexity is $O(n)$. Where $n$ is the length of the array, and $m$ is the maximum value in the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        f = True
        while f:
            f = False
            t = arr[:]
            for i in range(1, len(t) - 1):
                if t[i] > t[i - 1] and t[i] > t[i + 1]:
                    arr[i] -= 1
                    f = True
                if t[i] < t[i - 1] and t[i] < t[i + 1]:
                    arr[i] += 1
                    f = True
        return arr
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
