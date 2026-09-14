---
comments: true
difficulty: Medium
tags:
    - Recursion
    - Math
---

<!-- problem:start -->

# [50. Pow(x, n)](https://leetcode.com/problems/powx-n)

## Description

<!-- description:start -->

<p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x<sup>n</sup></code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = 10
<strong>Output:</strong> 1024.00000
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2.10000, n = 3
<strong>Output:</strong> 9.26100
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = -2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100.0 &lt; x &lt; 100.0</code></li>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li>
	<li><code>n</code> is an integer.</li>
	<li>Either <code>x</code> is not zero or <code>n &gt; 0</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Mathematics (Fast Powering)

<!-- thinking:start -->

> **Thinking**
>
> The first idea is multiply $x$ by itself $|n|$ times. $|n|$ reaches $2^{31}$, so a linear loop times out; negative $n$ also needs a reciprocal.
>
> The bottleneck is multiplying by one $x$ at a time. $x^{2k} = (x^k)^2$ and $x^{2k+1} = x \cdot (x^k)^2$ — the exponent halves each step.
>
> Walk the bits of $n$: square the base, and when a bit is $1$ multiply into the answer. For negative $n$, compute the positive power then take the reciprocal. Fast powering drops $O(|n|)$ to $O(\log |n|)$.

<!-- thinking:end -->

The core idea of the fast powering algorithm is to decompose the exponent $n$ into the sum of $1$s on several binary bits, and then transform the $n$th power of $x$ into the product of several powers of $x$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$. Here, $n$ is the exponent.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            ans = 1
            while n:
                if n & 1:
                    ans *= a
                a *= a
                n >>= 1
            return ans

        return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
