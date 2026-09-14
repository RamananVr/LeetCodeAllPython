---
comments: true
difficulty: Medium
tags:
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> of length <code>n</code> where all the integers of <code>nums</code> are in the range <code>[1, n]</code> and each integer appears <strong>at most</strong> <strong>twice</strong>, return <em>an array of all the integers that appears <strong>twice</strong></em>.</p>

<p>You must write an algorithm that runs in <code>O(n)</code> time and uses only <em>constant</em> auxiliary space, excluding the space needed to store the output</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [2,3]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> [1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> []
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li>Each element in <code>nums</code> appears <strong>once</strong> or <strong>twice</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Values lie in $[1,n]$ and appear at most twice; the follow-up wants linear time and constant extra memory. A hash set finds duplicates but uses $O(n)$ space.
>
> Swap $v$ into index $v-1$ (cycle sort). Afterwards a value that is not $i+1$ at index $i$ is a leftover duplicate.
>
> The swap loop stops when $nums[i]=nums[nums[i]-1]$, so a duplicate collides with the value already in place and never cycles forever.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [v for i, v in enumerate(nums) if v != i + 1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
