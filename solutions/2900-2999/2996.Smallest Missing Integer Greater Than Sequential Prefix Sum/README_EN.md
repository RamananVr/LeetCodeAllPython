---
comments: true
difficulty: Easy
rating: 1405
source: Biweekly Contest 121 Q1
tags:
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code>.</p>

<p>A prefix <code>nums[0..i]</code> is <strong>sequential</strong> if, for all <code>1 &lt;= j &lt;= i</code>, <code>nums[j] = nums[j - 1] + 1</code>. In particular, the prefix consisting only of <code>nums[0]</code> is <strong>sequential</strong>.</p>

<p>Return <em>the <strong>smallest</strong> integer</em> <code>x</code> <em>missing from</em> <code>nums</code> <em>such that</em> <code>x</code> <em>is greater than or equal to the sum of the <strong>longest</strong> sequential prefix.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,2,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,12,14,13]
<strong>Output:</strong> 15
<strong>Explanation:</strong> The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> The longest sequential prefix starts at index $0$; let $s$ be its sum. We want the least integer $\ge s$ absent from the array. $n \le 50$: scan the prefix sum, then test $s,s+1,\ldots$ against a set.
>
> The domain is tiny, so a linear increment hits the gap.

<!-- thinking:end -->

First, we calculate the sum $s$ of the longest sequential prefix of the array $nums$. Then, starting from $s$, we enumerate the integer $x$. If $x$ is not in the array $nums$, then $x$ is the answer.

Since $nums[i] \leq 50$ in this problem, we can use an array of length $51$ (or a hash table) to record the integers that appear in the array, so as to quickly determine whether an integer is in the array $nums$.

The time complexity is $O(n + M)$, and the space complexity is $O(M)$. Where $n$ is the length of the array $nums$, and $M$ is the upper bound of the array elements, which is $51$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        for x, y in pairwise(nums):
            if x + 1 != y:
                break
            s += y
        st = set(nums)
        while s in st:
            s += 1
        return s
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
