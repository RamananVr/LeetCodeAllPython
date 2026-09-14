---
comments: true
difficulty: Hard
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive)

## Description

<!-- description:start -->

<p>Given an unsorted integer array <code>nums</code>. Return the <em>smallest positive integer</em> that is <em>not present</em> in <code>nums</code>.</p>

<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: In-place Swap

<!-- thinking:start -->

> **Thinking**
>
> The first idea is a hash set of seen numbers, then probe $1, 2, 3, \ldots$. Correct and $O(n)$ time, but $O(n)$ extra space. The problem asks for $O(n)$ time and constant extra space; $n \le 10^5$ makes the set fail the space bound.
>
> The bottleneck is recording whether $1..n$ appear with extra memory. The missing positive must lie in $[1, n+1]$, so we only care about $1..n$ — the array indices themselves can be that table.
>
> Swap value $x$ to index $x-1$ when $x \in [1, n]$. In-place swap turns the array into a hash; one more scan finds the first hole.

<!-- thinking:end -->

We assume the length of the array $nums$ is $n$, then the smallest positive integer must be in the range $[1, .., n + 1]$. We can traverse the array and swap each number $x$ to its correct position, that is, the position $x - 1$. If $x$ is not in the range $[1, n + 1]$, then we can ignore it.

After the traversal, we traverse the array again. If $i+1$ is not equal to $nums[i]$, then $i+1$ is the smallest positive integer we are looking for.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
