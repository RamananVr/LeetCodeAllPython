---
comments: true
difficulty: Easy
tags:
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The element 1 occurs at the indices 0 and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements are distinct.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,3,3,4,3,2,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

<!-- thinking:start -->

> **Thinking**
>
> Comparing every pair works but is slow for large $n$. Equal values become adjacent after sorting.
>
> Sort the array, then check whether any two neighbors are equal.

<!-- thinking:end -->

First, we sort the array `nums`.

Then, we traverse the array. If there are two adjacent elements that are the same, it means that there are duplicate elements in the array, and we directly return `true`.

Otherwise, when the traversal ends, we return `false`.

The time complexity is $O(n \times \log n)$, where $n$ is the length of the array `nums`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(a == b for a, b in pairwise(sorted(nums)))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table

<!-- thinking:start -->

> **Thinking**
>
> Sorting is $O(n\log n)$ and reorders the array. Membership alone can be tracked with a hash set in one pass.
>
> A value that is already in the set is a duplicate.

<!-- thinking:end -->

We traverse the array and record the elements that have appeared in the hash table $s$. If an element appears for the second time, it means that there are duplicate elements in the array, and we directly return `true`.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array `nums`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
