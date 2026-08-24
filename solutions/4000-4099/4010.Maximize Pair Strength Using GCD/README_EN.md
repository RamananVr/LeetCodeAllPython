---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/4000-4099/4010.Maximize%20Pair%20Strength%20Using%20GCD/README_EN.md
rating: 1216
source: Weekly Contest 513 Q1
tags:
    - Array
    - Math
    - Enumeration
    - Number Theory
---

<!-- problem:start -->

# [4010. Maximize Pair Strength Using GCD](https://leetcode.com/problems/maximize-pair-strength-using-gcd)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>Choose exactly one pair of distinct indices <code>i</code> and <code>j</code>. The strength of the pair is defined as <code>(nums[i] * nums[j]) / <span data-keyword="gcd-function">gcd(nums[i], nums[j])</span><sup>2</sup></code>.</p>

<p>Return the maximum strength over all possible pairs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>Choosing <code>i = 1</code> and <code>j = 2</code> gives strength <code>(3 * 5) / gcd(3, 5)<sup>2</sup> = 15 / 1 = 15</code>, which is the maximum over all pairs.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,6,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>Choosing <code>i = 1</code> and <code>j = 2</code> gives strength <code>(6 * 8) / gcd(6, 8)<sup>2</sup> = 48 / 4 = 12</code>, which is the maximum over all pairs.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Choosing <code>i = 0</code> and <code>j = 1</code> gives strength <code>(3 * 3) / gcd(3, 3)<sup>2</sup> = 9 / 9 = 1</code>, the maximum over all pairs.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

We directly enumerate all pairs $(i, j)$ where $i < j$, calculate the strength of each pair $\frac{\textit{nums}[i] \times \textit{nums}[j]}{\gcd(\textit{nums}[i], \textit{nums}[j])^2}$, and take the maximum.

The greatest common divisor $\gcd$ can be computed using the Euclidean algorithm.

The time complexity is $O(n^2 \times \log M)$, where $n$ is the length of the array $\textit{nums}$ and $M$ is the maximum value in the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                x = nums[i] * nums[j] // gcd(nums[i], nums[j]) ** 2
                ans = max(ans, x)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
