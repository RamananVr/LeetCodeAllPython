---
comments: true
difficulty: Medium
rating: 1697
source: Weekly Contest 130 Q2
tags:
    - Math
---

<!-- problem:start -->

# [1017. Convert to Base -2](https://leetcode.com/problems/convert-to-base-2)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em>a binary string representing its representation in base</em> <code>-2</code>.</p>

<p><strong>Note</strong> that the returned string should not have leading zeros unless the string is <code>&quot;0&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> &quot;110&quot;
<strong>Explantion:</strong> (-2)<sup>2</sup> + (-2)<sup>1</sup> = 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> &quot;111&quot;
<strong>Explantion:</strong> (-2)<sup>2</sup> + (-2)<sup>1</sup> + (-2)<sup>0</sup> = 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> &quot;100&quot;
<strong>Explantion:</strong> (-2)<sup>2</sup> = 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Ordinary conversion to a positive base yields negative remainders for $-2$ and cannot be used as-is. $n\le 10^9$ gives $O(\log n)$ bits, so a digit-by-digit simulation is enough.
>
> The least bit is $n\bmod 2$. When it is $1$ we subtract the current place value $k$ (a power of $-1$ on odd positions) so the rest stays even, then divide by $2$ and flip the sign of $k$.
>
> Bits are collected from low to high and reversed. The number $0$ maps to $\texttt{0}$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def baseNeg2(self, n: int) -> str:
        k = 1
        ans = []
        while n:
            if n % 2:
                ans.append('1')
                n -= k
            else:
                ans.append('0')
            n //= 2
            k *= -1
        return ''.join(ans[::-1]) or '0'
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
