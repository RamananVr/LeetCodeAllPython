---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2941.Maximum%20GCD-Sum%20of%20a%20Subarray/README_EN.md
tags:
    - Array
    - Math
    - Binary Search
    - Number Theory
---

<!-- problem:start -->

# [2941. Maximum GCD-Sum of a Subarray 🔒](https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray)

## Description

<!-- description:start -->

<p>You are given an array of integers <code>nums</code> and an integer <code>k</code>.</p>

<p>The <strong>gcd-sum</strong> of an array <code>a</code> is calculated as follows:</p>

<ul>
	<li>Let <code>s</code> be the sum of all the elements of <code>a</code>.</li>
	<li>Let <code>g</code> be the <strong>greatest common divisor</strong> of all the elements of <code>a</code>.</li>
	<li>The gcd-sum of <code>a</code> is equal to <code>s * g</code>.</li>
</ul>

<p>Return <em>the <strong>maximum gcd-sum</strong> of a subarray of</em> <code>nums</code> <em>with at least</em> <code>k</code> <em>elements.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,4,4,4,2], k = 2
<strong>Output:</strong> 48
<strong>Explanation:</strong> We take the subarray [4,4,4], the gcd-sum of this array is 4 * (4 + 4 + 4) = 48.
It can be shown that we can not select any other subarray with a gcd-sum greater than 48.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,3,9,4], k = 1
<strong>Output:</strong> 81
<strong>Explanation:</strong> We take the subarray [9], the gcd-sum of this array is 9 * 9 = 81.
It can be shown that we can not select any other subarray with a gcd-sum greater than 81.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        f = []
        ans = 0
        for i, v in enumerate(nums):
            g = []
            for j, x in f:
                y = gcd(x, v)
                if not g or g[-1][1] != y:
                    g.append((j, y))
            f = g
            f.append((i, v))
            for j, x in f:
                if i - j + 1 >= k:
                    ans = max(ans, (s[i + 1] - s[j]) * x)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- solution:end -->

<!-- problem:end -->
