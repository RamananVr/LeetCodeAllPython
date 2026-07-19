---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2999.Count%20the%20Number%20of%20Powerful%20Integers/README_EN.md
rating: 2351
source: Biweekly Contest 121 Q4
tags:
    - Math
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [2999. Count the Number of Powerful Integers](https://leetcode.com/problems/count-the-number-of-powerful-integers)

## Description

<!-- description:start -->

<p>You are given three integers <code>start</code>, <code>finish</code>, and <code>limit</code>. You are also given a <strong>0-indexed</strong> string <code>s</code> representing a <strong>positive</strong> integer.</p>

<p>A <strong>positive</strong> integer <code>x</code> is called <strong>powerful</strong> if it ends with <code>s</code> (in other words, <code>s</code> is a <strong>suffix</strong> of <code>x</code>) and each digit in <code>x</code> is at most <code>limit</code>.</p>

<p>Return <em>the <strong>total</strong> number of powerful integers in the range</em> <code>[start..finish]</code>.</p>

<p>A string <code>x</code> is a suffix of a string <code>y</code> if and only if <code>x</code> is a substring of <code>y</code> that starts from some index (<strong>including </strong><code>0</code>) in <code>y</code> and extends to the index <code>y.length - 1</code>. For example, <code>25</code> is a suffix of <code>5125</code> whereas <code>512</code> is not.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> start = 1, finish = 6000, limit = 4, s = &quot;124&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The powerful integers in the range [1..6000] are 124, 1124, 2124, 3124, and, 4124. All these integers have each digit &lt;= 4, and &quot;124&quot; as a suffix. Note that 5124 is not a powerful integer because the first digit is 5 which is greater than 4.
It can be shown that there are only 5 powerful integers in this range.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> start = 15, finish = 215, limit = 6, s = &quot;10&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The powerful integers in the range [15..215] are 110 and 210. All these integers have each digit &lt;= 6, and &quot;10&quot; as a suffix.
It can be shown that there are only 2 powerful integers in this range.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> start = 1000, finish = 2000, limit = 4, s = &quot;3000&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> All integers in the range [1000..2000] are smaller than 3000, hence &quot;3000&quot; cannot be a suffix of any integer in this range.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= start &lt;= finish &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 9</code></li>
	<li><code>1 &lt;= s.length &lt;= floor(log<sub>10</sub>(finish)) + 1</code></li>
	<li><code>s</code> only consists of numeric digits which are at most <code>limit</code>.</li>
	<li><code>s</code> does not have leading zeros.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

This problem is essentially about finding the count of numbers in the given range $[l, .., r]$ that satisfy the conditions. The count depends on the number of digits and the value of each digit. We can solve this problem using the Digit DP approach, where the size of the number has minimal impact on the complexity.

For the range $[l, .., r]$, we typically transform it into two subproblems: $[1, .., r]$ and $[1, .., l - 1]$, i.e.,

$$
ans = \sum_{i=1}^{r} ans_i - \sum_{i=1}^{l-1} ans_i
$$

For this problem, we calculate the count of numbers in $[1, \textit{finish}]$ that satisfy the conditions, and subtract the count of numbers in $[1, \textit{start} - 1]$ that satisfy the conditions to get the final answer.

We use memoization to implement Digit DP. Starting from the topmost digit, we recursively calculate the number of valid numbers, accumulate the results layer by layer, and finally return the answer from the starting point.

The basic steps are as follows:

1. Convert $\textit{start}$ and $\textit{finish}$ to strings for easier manipulation in Digit DP.
2. Design a function $\textit{dfs}(\textit{pos}, \textit{lim})$, which represents the count of valid numbers starting from the $\textit{pos}$-th digit, with the current restriction condition $\textit{lim}$.
3. If the maximum number of digits is less than the length of $\textit{s}$, return 0.
4. If the remaining number of digits equals the length of $\textit{s}$, check if the current number satisfies the condition and return 1 or 0.
5. Otherwise, calculate the upper limit of the current digit as $\textit{up} = \min(\textit{lim} ? \textit{t}[\textit{pos}] : 9, \textit{limit})$. Then iterate through the digits $i$ from 0 to $\textit{up}$, recursively call $\textit{dfs}(\textit{pos} + 1, \textit{lim} \&\& i == \textit{t}[\textit{pos}])$, and accumulate the results.
6. If $\textit{lim}$ is false, store the current result in the cache to avoid redundant calculations.
7. Finally, return the result.

The answer is the count of valid numbers in $[1, \textit{finish}]$ minus the count of valid numbers in $[1, \textit{start} - 1]$.

Time complexity is $O(\log M \times D)$, and space complexity is $O(\log M)$, where $M$ is the upper limit of the number, and $D = 10$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @cache
        def dfs(pos: int, lim: int) -> int:
            if len(t) < n:
                return 0
            if len(t) - pos == n:
                return int(s <= t[pos:]) if lim else 1
            up = min(int(t[pos]) if lim else 9, limit)
            ans = 0
            for i in range(up + 1):
                ans += dfs(pos + 1, lim and i == int(t[pos]))
            return ans

        n = len(s)
        t = str(start - 1)
        a = dfs(0, True)
        dfs.cache_clear()
        t = str(finish)
        b = dfs(0, True)
        return b - a
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
