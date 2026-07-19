---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2787.Ways%20to%20Express%20an%20Integer%20as%20Sum%20of%20Powers/README_EN.md
rating: 1817
source: Biweekly Contest 109 Q4
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [2787. Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers)

## Description

<!-- description:start -->

<p>Given two <strong>positive</strong> integers <code>n</code> and <code>x</code>.</p>

<p>Return <em>the number of ways </em><code>n</code><em> can be expressed as the sum of the </em><code>x<sup>th</sup></code><em> power of <strong>unique</strong> positive integers, in other words, the number of sets of unique integers </em><code>[n<sub>1</sub>, n<sub>2</sub>, ..., n<sub>k</sub>]</code><em> where </em><code>n = n<sub>1</sub><sup>x</sup> + n<sub>2</sub><sup>x</sup> + ... + n<sub>k</sub><sup>x</sup></code><em>.</em></p>

<p>Since the result can be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>For example, if <code>n = 160</code> and <code>x = 3</code>, one way to express <code>n</code> is <code>n = 2<sup>3</sup> + 3<sup>3</sup> + 5<sup>3</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10, x = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can express n as the following: n = 3<sup>2</sup> + 1<sup>2</sup> = 10.
It can be shown that it is the only way to express 10 as the sum of the 2<sup>nd</sup> power of unique integers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, x = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can express n in the following ways:
- n = 4<sup>1</sup> = 4.
- n = 3<sup>1</sup> + 1<sup>1</sup> = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>1 &lt;= x &lt;= 5</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the number of ways to select some numbers from the first $i$ positive integers such that the sum of their $x$-th powers equals $j$. Initially, $f[0][0] = 1$, and all others are $0$. The answer is $f[n][n]$.

For each positive integer $i$, we can choose to either include it or not:

- Not include it: the number of ways is $f[i-1][j]$;
- Include it: the number of ways is $f[i-1][j-i^x]$ (provided that $j \geq i^x$).

Therefore, the state transition equation is:

$$
f[i][j] = f[i-1][j] + (j \geq i^x ? f[i-1][j-i^x] : 0)
$$

Note that the answer can be very large, so we need to take modulo $10^9 + 7$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$, where $n$ is the given integer in the

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        f = [[0] * (n + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            k = pow(i, x)
            for j in range(n + 1):
                f[i][j] = f[i - 1][j]
                if k <= j:
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
        return f[n][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
