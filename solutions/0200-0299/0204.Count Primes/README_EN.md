---
comments: true
difficulty: Medium
tags:
    - Array
    - Math
    - Enumeration
    - Number Theory
    - Primality Test
    - Sieve
    - Sieve of Eratosthenes
---

<!-- problem:start -->

# [204. Count Primes](https://leetcode.com/problems/count-primes)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em>the number of prime numbers that are strictly less than</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Trial division up to $\sqrt{x}$ counts primes, but $n$ can be $5\times 10^6$, so repeated tests are slow. If $x$ is prime, its multiples $2x,3x,\ldots$ are composite.
>
> The Sieve of Eratosthenes marks those multiples as we scan upward, then counts unmarked values. Each composite is crossed off by a factor, in about $O(n\log\log n)$ time.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        ans = 0
        for i in range(2, n):
            if primes[i]:
                ans += 1
                for j in range(i + i, n, i):
                    primes[j] = False
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
