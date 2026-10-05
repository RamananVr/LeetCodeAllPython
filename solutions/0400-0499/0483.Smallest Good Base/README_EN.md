---
comments: true
difficulty: Hard
tags:
    - Math
    - Binary Search
---

<!-- problem:start -->

# [483. Smallest Good Base](https://leetcode.com/problems/smallest-good-base)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code> represented as a string, return <em>the smallest <strong>good base</strong> of</em> <code>n</code>.</p>

<p>We call <code>k &gt;= 2</code> a <strong>good base</strong> of <code>n</code>, if all digits of <code>n</code> base <code>k</code> are <code>1</code>&#39;s.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;13&quot;
<strong>Output:</strong> &quot;3&quot;
<strong>Explanation:</strong> 13 base 3 is 111.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;4681&quot;
<strong>Output:</strong> &quot;8&quot;
<strong>Explanation:</strong> 4681 base 8 is 11111.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;1000000000000000000&quot;
<strong>Output:</strong> &quot;999999999999999999&quot;
<strong>Explanation:</strong> 1000000000000000000 base 999999999999999999 is 11.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n</code> is an integer in the range <code>[3, 10<sup>18</sup>]</code>.</li>
	<li><code>n</code> does not contain any leading zeros.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

<!-- thinking:start -->

> **Thinking**
>
> The smallest base $k\ge 2$ in which $n$ is all ones. $k=n-1$ always works ($11_k$), but $n$ can be $10^{18}$, so scanning $k$ is impossible.
>
> The number of ones $m+1$ satisfies $m<60$. Try $m$ from large to small and binary-search $k$ so that $1+k+\cdots+k^m=n$. A larger $m$ yields a smaller $k$, so going downward finds the smallest base first.
>
> The geometric sum is monotone in $k$, so the binary search is valid. If none hits, fall back to $n-1$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def cal(k, m):
            p = s = 1
            for i in range(m):
                p *= k
                s += p
            return s

        num = int(n)
        for m in range(63, 1, -1):
            l, r = 2, num - 1
            while l < r:
                mid = (l + r) >> 1
                if cal(mid, m) >= num:
                    r = mid
                else:
                    l = mid + 1
            if cal(l, m) == num:
                return str(l)
        return str(num - 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
