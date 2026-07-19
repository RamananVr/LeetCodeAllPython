---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3334.Find%20the%20Maximum%20Factor%20Score%20of%20Array/README_EN.md
rating: 1518
source: Weekly Contest 421 Q1
tags:
    - Array
    - Math
    - Number Theory
---

<!-- problem:start -->

# [3334. Find the Maximum Factor Score of Array](https://leetcode.com/problems/find-the-maximum-factor-score-of-array)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>The <strong>factor score</strong> of an array is defined as the <em>product</em> of the LCM and GCD of all elements of that array.</p>

<p>Return the <strong>maximum factor score</strong> of <code>nums</code> after removing <strong>at most</strong> one element from it.</p>

<p><strong>Note</strong> that <em>both</em> the <span data-keyword="lcm-function">LCM</span> and <span data-keyword="gcd-function">GCD</span> of a single number are the number itself, and the <em>factor score</em> of an <strong>empty</strong> array is 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,4,8,16]</span></p>

<p><strong>Output:</strong> <span class="example-io">64</span></p>

<p><strong>Explanation:</strong></p>

<p>On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of <code>4 * 16 = 64</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">60</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum factor score of 60 can be obtained without removing any elements.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3]</span></p>

<p><strong>Output:</strong> 9</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 30</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        suf_gcd = [0] * (n + 1)
        suf_lcm = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            suf_gcd[i] = gcd(suf_gcd[i + 1], nums[i])
            suf_lcm[i] = lcm(suf_lcm[i + 1], nums[i])
        ans = suf_gcd[0] * suf_lcm[0]
        pre_gcd, pre_lcm = 0, 1
        for i, x in enumerate(nums):
            ans = max(ans, gcd(pre_gcd, suf_gcd[i + 1]) * lcm(pre_lcm, suf_lcm[i + 1]))
            pre_gcd = gcd(pre_gcd, x)
            pre_lcm = lcm(pre_lcm, x)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
