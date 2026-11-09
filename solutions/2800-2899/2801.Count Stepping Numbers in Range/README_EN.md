---
comments: true
difficulty: Hard
rating: 2367
source: Weekly Contest 356 Q4
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [2801. Count Stepping Numbers in Range](https://leetcode.com/problems/count-stepping-numbers-in-range)

## Description

<!-- description:start -->

<p>Given two positive integers <code>low</code> and <code>high</code> represented as strings, find the count of <strong>stepping numbers</strong> in the inclusive range <code>[low, high]</code>.</p>

<p>A <strong>stepping number</strong> is an integer such that all of its adjacent digits have an absolute difference of <strong>exactly</strong> <code>1</code>.</p>

<p>Return <em>an integer denoting the count of stepping numbers in the inclusive range</em> <code>[low, high]</code><em>. </em></p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note:</strong> A stepping number should not have a leading zero.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = &quot;1&quot;, high = &quot;11&quot;
<strong>Output:</strong> 10
<strong>Explanation: </strong>The stepping numbers in the range [1,11] are 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10. There are a total of 10 stepping numbers in the range. Hence, the output is 10.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = &quot;90&quot;, high = &quot;101&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>The stepping numbers in the range [90,101] are 98 and 101. There are a total of 2 stepping numbers in the range. Hence, the output is 2. </pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= int(low) &lt;= int(high) &lt; 10<sup>100</sup></code></li>
	<li><code>1 &lt;= low.length, high.length &lt;= 100</code></li>
	<li><code>low</code> and <code>high</code> consist of only digits.</li>
	<li><code>low</code> and <code>high</code> don&#39;t have any leading zeros.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

<!-- thinking:start -->

> **Thinking**
>
> $\textit{low}$ and $\textit{high}$ are given as digit strings, so enumerating every integer in the range is infeasible. The count on $[\textit{low},\textit{high}]$ equals $F(\textit{high})-F(\textit{low}-1)$. A stepping number only constrains adjacent digits, which is a standard digit-DP setting. We memoize on position $\textit{pos}$, previous digit $\textit{pre}$, leading-zero flag $\textit{lead}$, and upper-bound flag $\textit{limit}$: leading zeros skip the adjacency check, and a nonzero digit $i$ is allowed only when there is no previous digit or $|i-\textit{pre}|=1$.

<!-- thinking:end -->

We notice that the problem is asking for the number of stepping numbers in the interval $[\textit{low}, \textit{high}]$. For such an interval $[l,..r]$ problem, we can usually consider transforming it into finding the answers for $[1, r]$ and $[1, l-1]$, and then subtracting the latter from the former. Moreover, the problem only involves the relationship between different digits, not the specific values, so we can consider using Digit DP to solve it.

We design a function $\textit{dfs}(\textit{pos}, \textit{pre}, \textit{lead}, \textit{limit})$, which represents the number of schemes when we are currently processing the $\textit{pos}$-th digit, the previous digit is $\textit{pre}$, whether the current number only contains leading zeros is $\textit{lead}$, and whether the current number has reached the upper limit is $\textit{limit}$. The range of $\textit{pos}$ is $[0, \textit{len}(\textit{num}))$.

The execution logic of the function $\textit{dfs}(\textit{pos}, \textit{pre}, \textit{lead}, \textit{limit})$ is as follows:

If $\textit{pos}$ exceeds the length of $\textit{num}$, it means that we have processed all the digits. If $\textit{lead}$ is true at this time, it means that the current number only contains leading zeros and is not a valid number. We can return $0$ to indicate that the number of schemes is $0$; otherwise, we return $1$ to indicate that the number of schemes is $1$.

Otherwise, we calculate the upper limit $up$ of the current digit, and then enumerate the digit $i$ in the range $[0,..up]$:

- If $i=0$ and $\textit{lead}$ is true, it means that the current number only contains leading zeros. We recursively calculate the value of $\textit{dfs}(\textit{pos}+1,\textit{pre}, \textit{true}, \textit{limit}\ \text{and}\ i=up)$ and add it to the answer.
- Otherwise, if $\textit{pre}$ is $-1$, or the absolute difference between $i$ and $\textit{pre}$ is $1$, it means that the current number is a valid stepping number. We recursively calculate the value of $\textit{dfs}(\textit{pos}+1,i, \textit{false}, \textit{limit}\ \text{and}\ i=up)$ and add it to the answer.

Finally, we return the answer.

In the main function, we calculate the answers $a$ and $b$ for $[1, \textit{high}]$ and $[1, \textit{low}-1]$ respectively. The final answer is $a-b$. Note the modulo operation of the answer.

The time complexity is $O(|\Sigma|^2 \log M)$, and the space complexity is $O(|\Sigma| \log M)$, where $M$ represents the size of the number $\textit{high}$, and $|\Sigma|$ represents the digit set.

Similar problems:

- [2719. Count of Integers](https://github.com/doocs/leetcode/blob/main/solution/2700-2799/2719.Count%20of%20Integers/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        @cache
        def dfs(pos: int, pre: int, lead: bool, limit: bool) -> int:
            if pos >= len(num):
                return int(not lead)
            up = int(num[pos]) if limit else 9
            ans = 0
            for i in range(up + 1):
                if i == 0 and lead:
                    ans += dfs(pos + 1, pre, True, limit and i == up)
                elif pre == -1 or abs(i - pre) == 1:
                    ans += dfs(pos + 1, i, False, limit and i == up)
            return ans % mod

        mod = 10**9 + 7
        num = high
        a = dfs(0, -1, True, True)
        dfs.cache_clear()
        num = str(int(low) - 1)
        b = dfs(0, -1, True, True)
        return (a - b) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
