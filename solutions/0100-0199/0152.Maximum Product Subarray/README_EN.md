---
comments: true
difficulty: Medium
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, find a <span data-keyword="subarray-nonempty">subarray</span> that has the largest product, and return <em>the product</em>.</p>

<p>The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p><strong>Note</strong> that the product of an array with a single element is the value of that element.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,-2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [2,3] has the largest product 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The result cannot be 2, because [-2,-1] is not a subarray.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>The product of any subarray of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Kadane works for sums; products flip when a negative appears, and a zero resets the run. $n\le 2\times 10^4$. Keep the max and min product ending here; the new value may multiply either or start a new segment. The answer is the best max seen.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = f = g = nums[0]
        for x in nums[1:]:
            ff, gg = f, g
            f = max(x, ff * x, gg * x)
            g = min(x, ff * x, gg * x)
            ans = max(ans, f)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
