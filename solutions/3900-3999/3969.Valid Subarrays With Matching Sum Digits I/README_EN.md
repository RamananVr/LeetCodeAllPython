---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3969.Valid%20Subarrays%20With%20Matching%20Sum%20Digits%20I/README_EN.md
rating: 1397
source: Weekly Contest 507 Q2
tags:
    - Array
    - Hash Table
    - Enumeration
    - Prefix Sum
    - Sliding Window
---

<!-- problem:start -->

# [3969. Valid Subarrays With Matching Sum Digits I](https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and an integer digit <code>x</code>.</p>

<p>A <span data-keyword="subarray-nonempty"><strong>subarray</strong></span> <code>nums[l..r]</code> is considered <strong>valid</strong> if the sum of its elements satisfies both of the following conditions:</p>

<ul>
	<li>The first digit of the sum is equal to <code>x</code>.</li>
	<li>The last digit of the sum is equal to <code>x</code>.</li>
</ul>

<p>Return the number of valid subarrays.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,100,1], x = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The valid subarrays are:</p>

<ul>
	<li><code>nums[0..0]</code>: <code>sum = 1</code></li>
	<li><code>nums[0..1]</code>: <code>sum = 1 + 100 = 101</code></li>
	<li><code>nums[1..2]</code>: <code>sum = 100 + 1 = 101</code></li>
	<li><code>nums[2..2]</code>: <code>sum = 1</code></li>
</ul>

<p>Thus, the answer is 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The only subarray is <code>nums[0..0]</code> with a sum of 1, which does not satisfy the conditions.</p>

<p>Thus, the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= x &lt;= 9</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

We can enumerate the left endpoint $l$ of the subarray, and for each $l$, we enumerate the right endpoint $r$ in the range $[l, n)$, and calculate the sum of $nums[l..r]$. If it satisfies the conditions, the answer is increased by one.

The time complexity is $O(n^2)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            s = 0
            for r in range(l, n):
                s += nums[r]
                if s % 10 == x and int(str(s)[0]) == x:
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
