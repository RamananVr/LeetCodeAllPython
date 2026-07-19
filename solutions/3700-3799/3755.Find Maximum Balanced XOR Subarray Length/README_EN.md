---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3755.Find%20Maximum%20Balanced%20XOR%20Subarray%20Length/README_EN.md
rating: 1663
source: Weekly Contest 477 Q2
tags:
    - Bit Manipulation
    - Array
    - Hash Table
    - Prefix Sum
---

<!-- problem:start -->

# [3755. Find Maximum Balanced XOR Subarray Length](https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return the <strong>length</strong> of the <strong>longest <span data-keyword="subarray-nonempty">subarray</span></strong> that has a bitwise XOR of zero and contains an <strong>equal</strong> number of <strong>even</strong> and <strong>odd</strong> numbers. If no such subarray exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,3,2,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>[1, 3, 2, 0]</code> has bitwise XOR <code>1 XOR 3 XOR 2 XOR 0 = 0</code> and contains 2 even and 2 odd numbers.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,8,5,4,14,9,15]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The whole array has bitwise XOR <code>0</code> and contains 4 even and 4 odd numbers.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No non-empty subarray satisfies both conditions.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Hash Table

We use a hash table to record the first occurrence position of each state $(a, b)$, where $a$ represents the prefix XOR sum, and $b$ represents the prefix even count minus the prefix odd count. When we encounter the same state $(a, b)$ while traversing the array, it means that the subarray from the last occurrence of this state to the current position satisfies both bitwise XOR equals 0 and equal counts of even and odd numbers. We can then update the answer by taking the maximum length. Otherwise, we store this state and the current position in the hash table.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        d = {(0, 0): -1}
        a = b = 0
        ans = 0
        for i, x in enumerate(nums):
            a ^= x
            b += 1 if x % 2 == 0 else -1
            if (a, b) in d:
                ans = max(ans, i - d[(a, b)])
            else:
                d[(a, b)] = i
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
