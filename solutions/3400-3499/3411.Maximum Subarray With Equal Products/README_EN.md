---
comments: true
difficulty: Easy
rating: 1443
source: Weekly Contest 431 Q1
tags:
    - Array
    - Math
    - Enumeration
    - Number Theory
    - Sliding Window
---

<!-- problem:start -->

# [3411. Maximum Subarray With Equal Products](https://leetcode.com/problems/maximum-subarray-with-equal-products)

## Description

<!-- description:start -->

<p>You are given an array of <strong>positive</strong> integers <code>nums</code>.</p>

<p>An array <code>arr</code> is called <strong>product equivalent</strong> if <code>prod(arr) == lcm(arr) * gcd(arr)</code>, where:</p>

<ul>
	<li><code>prod(arr)</code> is the product of all elements of <code>arr</code>.</li>
	<li><code>gcd(arr)</code> is the <span data-keyword="gcd-function">GCD</span> of all elements of <code>arr</code>.</li>
	<li><code>lcm(arr)</code> is the <span data-keyword="lcm-function">LCM</span> of all elements of <code>arr</code>.</li>
</ul>

<p>Return the length of the <strong>longest</strong> <strong>product equivalent</strong> <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong>&nbsp;</p>

<p>The longest product equivalent subarray is <code>[1, 2, 1, 1, 1]</code>, where&nbsp;<code>prod([1, 2, 1, 1, 1]) = 2</code>,&nbsp;<code>gcd([1, 2, 1, 1, 1]) = 1</code>, and&nbsp;<code>lcm([1, 2, 1, 1, 1]) = 2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4,5,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong>&nbsp;</p>

<p>The longest product equivalent subarray is <code>[3, 4, 5].</code></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1,4,5,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> The product equaling $\gcd\cdot\operatorname{lcm}$ is an algebraic test on a subarray. With $n\le 100$ and values $\le 10$, we can enumerate every subarray while maintaining product, GCD, and LCM.
>
> The product grows quickly. Once it exceeds $\operatorname{lcm}(\textit{nums})\cdot\max(\textit{nums})$, a longer suffix cannot satisfy the identity, so the inner loop should stop.
>
> We fix the left end $i$, extend rightward updating $p$, $g$, and $l$, record the length when $p=g\cdot l$, and break when $p$ is already too large.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_p = lcm(*nums) * max(nums)
        for i in range(n):
            p, g, l = 1, 0, 1
            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == g * l:
                    ans = max(ans, j - i + 1)
                if p > max_p:
                    break
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
