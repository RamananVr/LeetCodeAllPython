---
comments: true
difficulty: Hard
rating: 2025
source: Biweekly Contest 1 Q4
tags:
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [1067. Digit Count in Range 🔒](https://leetcode.com/problems/digit-count-in-range)

## Description

<!-- description:start -->

<p>Given a single-digit integer <code>d</code> and two integers <code>low</code> and <code>high</code>, return <em>the number of times that </em><code>d</code><em> occurs as a digit in all integers in the inclusive range </em><code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> d = 1, low = 1, high = 13
<strong>Output:</strong> 6
<strong>Explanation:</strong> The digit d = 1 occurs 6 times in 1, 10, 11, 12, 13.
Note that the digit d = 1 occurs twice in the number 11.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> d = 3, low = 100, high = 250
<strong>Output:</strong> 35
<strong>Explanation:</strong> The digit d = 3 occurs 35 times in 103,113,123,130,131,...,238,239,243.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= d &lt;= 9</code></li>
	<li><code>1 &lt;= low &lt;= high &lt;= 2 * 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Counting digit $d$ on $[\textit{low},\textit{high}]$ cannot enumerate values up to $2\times 10^8$. The range is $f(\textit{high})-f(\textit{low}-1)$, where $f(n)$ counts occurrences in $1..n$.
>
> Digit DP tracks how many times $d$ is already used, leading zeros, and the upper bound. Leading zeros must not count a $0$ when $d=0$.
>
> Split $n$ into digits and memoize $\textit{dfs}(\textit{pos},\textit{cnt},\textit{lead},\textit{limit})$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        return self.f(high, d) - self.f(low - 1, d)

    def f(self, n, d):
        @cache
        def dfs(pos, cnt, lead, limit):
            if pos <= 0:
                return cnt
            up = a[pos] if limit else 9
            ans = 0
            for i in range(up + 1):
                if i == 0 and lead:
                    ans += dfs(pos - 1, cnt, lead, limit and i == up)
                else:
                    ans += dfs(pos - 1, cnt + (i == d), False, limit and i == up)
            return ans

        a = [0] * 11
        l = 0
        while n:
            l += 1
            a[l] = n % 10
            n //= 10
        return dfs(l, 0, True, True)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
