---
comments: true
difficulty: Easy
rating: 1184
source: Weekly Contest 255 Q1
tags:
    - Array
    - Math
    - Greatest Common Divisor
    - Number Theory
    - Euclidean Algorithm
---

<!-- problem:start -->

# [1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return<strong> </strong><em>the <strong>greatest common divisor</strong> of the smallest number and largest number in </em><code>nums</code>.</p>

<p>The <strong>greatest common divisor</strong> of two numbers is the largest positive integer that evenly divides both numbers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,6,9,10]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,5,6,8,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> The GCD of the whole array equals the GCD of its maximum and minimum. One pass finds both ends, then $\gcd$ finishes.

<!-- thinking:end -->

We can simulate according to the problem description. First, find the maximum and minimum values in the array $\textit{nums}$, then find the greatest common divisor of the maximum and minimum values.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
