---
comments: true
difficulty: Easy
tags:
    - Array
    - Binary Search
---

<!-- problem:start -->

# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position)

## Description

<!-- description:start -->

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

<!-- thinking:start -->

> **Thinking**
>
> The first idea is to scan left to right until the first index $\ge target$. Correct, and $n \le 10^4$ would pass, but the array is strictly increasing, so a linear scan wastes the order.
>
> The insertion point is exactly the first index not smaller than $target$ — a standard lower bound.
>
> Keep a half-open interval $[l,r)$: if $nums[mid] \ge target$ the answer lies in the left half (including $mid$), otherwise it lies to the right of $mid$. When $l=r$, $l$ is the insertion index.

<!-- thinking:end -->

Since the array $nums$ is already sorted, we can use the binary search method to find the insertion position of the target value $target$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Search (Built-in Function)

<!-- thinking:start -->

> **Thinking**
>
> Method 1 is already $O(\log n)$; what it still lacks is only that we need not write the binary search by hand. Languages already expose a lower bound: Python's `bisect_left`, C++'s `lower_bound`, Java's `Arrays.binarySearch` (returning $-i-1$ when absent). The meaning matches Method 1; we just call the builtin.

<!-- thinking:end -->

We can also directly use the built-in function for binary search.

The time complexity is $O(\log n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
