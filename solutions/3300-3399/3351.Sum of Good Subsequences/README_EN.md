---
comments: true
difficulty: Hard
rating: 2085
source: Weekly Contest 423 Q3
tags:
    - Array
    - Hash Table
    - Dynamic Programming
---

<!-- problem:start -->

# [3351. Sum of Good Subsequences](https://leetcode.com/problems/sum-of-good-subsequences)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. A <strong>good </strong><span data-keyword="subsequence-array">subsequence</span> is defined as a subsequence of <code>nums</code> where the absolute difference between any <strong>two</strong> consecutive elements in the subsequence is <strong>exactly</strong> 1.</p>

<p>Return the <strong>sum</strong> of all <em>possible</em> <strong>good subsequences</strong> of <code>nums</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note </strong>that a subsequence of size 1 is considered good by definition.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Good subsequences are: <code>[1]</code>, <code>[2]</code>, <code>[1]</code>, <code>[1,2]</code>, <code>[2,1]</code>, <code>[1,2,1]</code>.</li>
	<li>The sum of elements in these subsequences is 14.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">40</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Good subsequences are: <code>[3]</code>, <code>[4]</code>, <code>[5]</code>, <code>[3,4]</code>, <code>[4,5]</code>, <code>[3,4,5]</code>.</li>
	<li>The sum of elements in these subsequences is 40.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A good subsequence has consecutive absolute differences equal to $1$. With $n \le 10^5$ we cannot list subsequences; we DP on values.
>
> Let $g[x]$ be the number of good subsequences ending with $x$ and $f[x]$ their element sum. A new $x$ starts a singleton or appends to existing $x-1$ or $x+1$.
>
> Appending adds “old sum + old count $\times x$”. Updates follow input order so earlier copies of $x$ are included. The answer is the sum of all $f$, modulo $10^9+7$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        f = defaultdict(int)
        g = defaultdict(int)
        for x in nums:
            f[x] += x
            g[x] += 1
            f[x] += f[x - 1] + g[x - 1] * x
            g[x] += g[x - 1]
            f[x] += f[x + 1] + g[x + 1] * x
            g[x] += g[x + 1]
        return sum(f.values()) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
