---
comments: true
difficulty: Medium
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
    - Sliding Window
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements)

## Description

<!-- description:start -->

<p>Given a <strong>sorted</strong> integer array <code>arr</code>, two integers <code>k</code> and <code>x</code>, return the <code>k</code> closest integers to <code>x</code> in the array. The result should also be sorted in ascending order.</p>

<p>An integer <code>a</code> is closer to <code>x</code> than an integer <code>b</code> if:</p>

<ul>
	<li><code>|a - x| &lt; |b - x|</code>, or</li>
	<li><code>|a - x| == |b - x|</code> and <code>a &lt; b</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [1,2,3,4,5], k = 4, x = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,3,4]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [1,1,2,3,4,5], k = 4, x = -1</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1,2,3]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>arr</code> is sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= arr[i], x &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sort

<!-- thinking:start -->

> **Thinking**
>
> We need the $k$ closest values to $x$, reported in sorted order. Sorting by distance then taking $k$ is $O(n\log n)$.
>
> Sort by $|v-x|$, keep $k$ elements, and sort those by value.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: abs(v - x))
        return sorted(arr[:k])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> The answer is a contiguous slice. Shrink the farther endpoint until the window has length $k$; the slice is already sorted.

<!-- thinking:end -->

The $k$ elements closest to $x$ in a sorted array form one contiguous subarray.

Set pointers $l$ and $r$ at the two ends. Compare $x - arr[l]$ with $arr[r - 1] - x$ and drop the farther end until $r - l = k$.

The time complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)
        while r - l > k:
            if x - arr[l] <= arr[r - 1] - x:
                r -= 1
            else:
                l += 1
        return arr[l:r]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Binary Search

<!-- thinking:start -->

> **Thinking**
>
> Two pointers are linear. The best left bound in $[0,n-k]$ is monotone: compare $x-arr[mid]$ with $arr[mid+k]-x$ and binary-search it.

<!-- thinking:end -->

On top of method 2, binary-search the left boundary of the window of length $k$ over $[0, n - k]$. At $\textit{mid}$, move the window left when $x - arr[\textit{mid}] \le arr[\textit{mid} + k] - x$, and right otherwise.

The time complexity is $O(\log n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) >> 1
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left : left + k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
