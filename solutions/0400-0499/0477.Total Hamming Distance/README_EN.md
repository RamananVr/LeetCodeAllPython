---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0477.Total%20Hamming%20Distance/README_EN.md
tags:
    - Bit Manipulation
    - Array
    - Math
---

<!-- problem:start -->

# [477. Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance)

## Description

<!-- description:start -->

<p>The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.</p>

<p>Given an integer array <code>nums</code>, return <em>the sum of <strong>Hamming distances</strong> between all the pairs of the integers in</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,14,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,14,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The answer for the given input will fit in a <strong>32-bit</strong> integer.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bit Manipulation

We enumerate each bit in the range $[0, 31]$. For the current enumerated bit $i$, we count the number of numbers where the $i$-th bit is $1$, denoted as $a$. Therefore, the number of numbers where the $i$-th bit is $0$ is $b = n - a$, where $n$ is the length of the array. In this way, the sum of the Hamming distance on the $i$-th bit is $a \times b$. We add the Hamming distances of all bits to get the answer.

The time complexity is $O(n \times \log M)$, where $n$ and $M$ are the length of the array and the maximum value in the array, respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(32):
            a = sum(x >> i & 1 for x in nums)
            b = n - a
            ans += a * b
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
