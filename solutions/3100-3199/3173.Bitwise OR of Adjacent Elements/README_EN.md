---
comments: true
difficulty: Easy
tags:
    - Bit Manipulation
    - Array
---

<!-- problem:start -->

# [3173. Bitwise OR of Adjacent Elements 🔒](https://leetcode.com/problems/bitwise-or-of-adjacent-elements)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of length <code>n</code>, return an array <code>answer</code> of length <code>n - 1</code> such that <code>answer[i] = nums[i] | nums[i + 1]</code> where <code>|</code> is the bitwise <code>OR</code> operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,7,15]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,7,15]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [8,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[12,6]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,9,11]</span></p>

<p><strong>Output:</strong> <span class="example-io">[5,13,11]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i]&nbsp;&lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Iteration

<!-- thinking:start -->

> **Thinking**
>
> Entry $i$ is $nums[i]\lor nums[i+1]$ and does not depend on farther elements.
>
> Each adjacent pair can be evaluated independently.
>
> Map `pairwise(nums)` through OR to obtain an array of length $n-1$.

<!-- thinking:end -->

We iterate through the first $n - 1$ elements of the array. For each element, we calculate the bitwise OR value of it and its next element, and store the result in the answer array.

The time complexity is $O(n)$, where $n$ is the length of the array. Ignoring the space consumption of the answer array, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [a | b for a, b in pairwise(nums)]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
