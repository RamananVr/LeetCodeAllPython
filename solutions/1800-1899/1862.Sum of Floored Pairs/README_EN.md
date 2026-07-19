---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1862.Sum%20of%20Floored%20Pairs/README_EN.md
rating: 2170
source: Biweekly Contest 52 Q4
tags:
    - Array
    - Math
    - Binary Search
    - Counting
    - Enumeration
    - Prefix Sum
---

<!-- problem:start -->

# [1862. Sum of Floored Pairs](https://leetcode.com/problems/sum-of-floored-pairs)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return the sum of <code>floor(nums[i] / nums[j])</code> for all pairs of indices <code>0 &lt;= i, j &lt; nums.length</code> in the array. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>The <code>floor()</code> function returns the integer part of the division.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,9]
<strong>Output:</strong> 10
<strong>Explanation:</strong>
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 49
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum of Value Range + Optimized Enumeration

First, we count the occurrences of each element in the array $nums$ and record them in the array $cnt$. Then, we calculate the prefix sum of the array $cnt$ and record it in the array $s$, i.e., $s[i]$ represents the count of elements less than or equal to $i$.

Next, we enumerate the denominator $y$ and the quotient $d$. Using the prefix sum array, we can calculate the count of the numerator $s[\min(mx, d \times y + y - 1)] - s[d \times y - 1]$, where $mx$ represents the maximum value in the array $nums$. Then, we multiply the count of the numerator by the count of the denominator $cnt[y]$, and then multiply by the quotient $d$. This gives us the value of all fractions that meet the conditions. By summing these values, we can get the answer.

The time complexity is $O(M \times \log M)$, and the space complexity is $O(M)$. Here, $M$ is the maximum value in the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        cnt = Counter(nums)
        mx = max(nums)
        s = [0] * (mx + 1)
        for i in range(1, mx + 1):
            s[i] = s[i - 1] + cnt[i]
        ans = 0
        for y in range(1, mx + 1):
            if cnt[y]:
                d = 1
                while d * y <= mx:
                    ans += cnt[y] * d * (s[min(mx, d * y + y - 1)] - s[d * y - 1])
                    ans %= mod
                    d += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
