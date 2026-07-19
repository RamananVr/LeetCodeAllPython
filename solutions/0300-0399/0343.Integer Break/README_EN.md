---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0343.Integer%20Break/README_EN.md
tags:
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [343. Integer Break](https://leetcode.com/problems/integer-break)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 &times; 1 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i]$ as the maximum product that can be obtained by splitting the positive integer $i$, with an initial condition of $f[1] = 1$. The answer is $f[n]$.

Consider the last number $j$ split from $i$, where $j \in [1, i)$. For the number $j$ split from $i$, there are two cases:

1. Split $i$ into the sum of $i - j$ and $j$, without further splitting, where the product is $(i - j) \times j$;
2. Split $i$ into the sum of $i - j$ and $j$, and continue splitting, where the product is $f[i - j] \times j$.

Therefore, we can derive the state transition equation:

$$
f[i] = \max(f[i], f[i - j] \times j, (i - j) \times j) \quad (j \in [0, i))
$$

Finally, returning $f[n]$ will suffice.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Here, $n$ is the given positive integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        f = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                f[i] = max(f[i], f[i - j] * j, (i - j) * j)
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 1: Mathematics

When $n < 4$, since the problem requires splitting into at least two integers, $n - 1$ yields the maximum product. When $n \geq 4$, we split into as many $3$s as possible. If the last segment remaining is $4$, we split it into $2 + 2$ for the maximum product.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n % 3 == 0:
            return pow(3, n // 3)
        if n % 3 == 1:
            return pow(3, n // 3 - 1) * 4
        return pow(3, n // 3) * 2
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
