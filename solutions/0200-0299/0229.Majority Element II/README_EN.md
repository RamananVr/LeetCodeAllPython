---
comments: true
difficulty: Medium
tags:
    - Array
    - Hash Table
    - Counting
    - Sorting
    - Boyer-Moore Voting
---

<!-- problem:start -->

# [229. Majority Element II](https://leetcode.com/problems/majority-element-ii)

## Description

<!-- description:start -->

<p>Given an integer array of size <code>n</code>, find all elements that appear more than <code>&lfloor;n / 3&rfloor;</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> [3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> At most two values can appear more than $\lfloor n/3\rfloor$ times. Hashing works but uses extra memory. Boyer–Moore can keep two candidates and their offsetting counts.
>
> A match increments a count; otherwise both counts decrement when they are positive. A second pass verifies the true frequencies.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = 0
        m1, m2 = 0, 1
        for m in nums:
            if m == m1:
                n1 += 1
            elif m == m2:
                n2 += 1
            elif n1 == 0:
                m1, n1 = m, 1
            elif n2 == 0:
                m2, n2 = m, 1
            else:
                n1, n2 = n1 - 1, n2 - 1
        return [m for m in [m1, m2] if nums.count(m) > len(nums) // 3]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
