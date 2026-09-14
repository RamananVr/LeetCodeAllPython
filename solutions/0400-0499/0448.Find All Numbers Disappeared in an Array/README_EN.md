---
comments: true
difficulty: Easy
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Values lie in $[1,n]$; missing numbers are a set difference. Store seen values in a hash set and scan $1..n$. Linear time, $O(n)$ extra space.
>
> The follow-up wants constant extra memory; this solution establishes correctness first.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in s]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 uses a set. Value $x$ can negate index $|x|-1$ to mark “seen”; a still-positive slot $i$ means $i+1$ is missing. Absolute value before indexing avoids treating a mark as a subscript.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
