---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0260.Single%20Number%20III/README_EN.md
tags:
    - Bit Manipulation
    - Array
---

<!-- problem:start -->

# [260. Single Number III](https://leetcode.com/problems/single-number-iii)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in <strong>any order</strong>.</p>

<p>You must write an&nbsp;algorithm that runs in linear runtime complexity and uses&nbsp;only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,3,2,5]
<strong>Output:</strong> [3,5]
<strong>Explanation: </strong> [5, 3] is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0]
<strong>Output:</strong> [-1,0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [1,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Each integer in <code>nums</code> will appear twice, only two integers will appear once.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bitwise Operation

The XOR operation has the following properties:

- Any number XOR 0 is still the original number, i.e., $x \oplus 0 = x$;
- Any number XOR itself is 0, i.e., $x \oplus x = 0$;

Since all numbers in the array appear twice except for two numbers, we can perform XOR operation on all numbers in the array to get the XOR result of the two numbers that only appear once.

Since these two numbers are not equal, there is at least one bit that is 1 in the XOR result. We can use the `lowbit` operation to find the lowest bit of 1 in the XOR result, and divide all numbers in the array into two groups based on whether this bit is 1 or not. This way, the two numbers that only appear once are separated into different groups.

Perform XOR operation on each group separately to obtain the two numbers $a$ and $b$ that only appear once.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xs = reduce(xor, nums)
        a = 0
        lb = xs & -xs
        for x in nums:
            if x & lb:
                a ^= x
        b = xs ^ a
        return [a, b]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table

<!-- solution:end -->

<!-- problem:end -->
