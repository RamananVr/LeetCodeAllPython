---
comments: true
difficulty: Medium
rating: 1848
source: Weekly Contest 476 Q3
tags:
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [3747. Count Distinct Integers After Removing Zeros](https://leetcode.com/problems/count-distinct-integers-after-removing-zeros)

## Description

<!-- description:start -->

<p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>For every integer <code>x</code> from 1 to <code>n</code>, we write down the integer obtained by removing all zeros from the decimal representation of <code>x</code>.</p>

<p>Return an integer denoting the number of <strong>distinct</strong> integers written down.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>15</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

<!-- thinking:start -->

> **Thinking**
>
> $n\le 10^{15}$ forbids stripping zeros from every $x$. After zeros are removed the result contains no $0$ and is at most the original number, so the distinct images in $[1,n]$ are exactly the zero-free integers in that range, which a digit DP counts.

<!-- thinking:end -->

The problem essentially asks us to count the number of integers in the range $[1, n]$ that do not contain the digit 0. We can solve this problem using digit DP.

We design a function $\textit{dfs}(i, \textit{zero}, \textit{lead}, \textit{limit})$, which represents the number of valid solutions when we are currently processing the $i$-th digit of the number. We use $\textit{zero}$ to indicate whether a non-zero digit has appeared in the current number, $\textit{lead}$ to indicate whether we are still processing leading zeros, and $\textit{limit}$ to indicate whether the current number is constrained by the upper bound. The answer is $\textit{dfs}(0, 0, 1, 1)$.

In the function $\textit{dfs}(i, \textit{zero}, \textit{lead}, \textit{limit})$, if $i$ is greater than or equal to the length of the number, we can check $\textit{zero}$ and $\textit{lead}$. If $\textit{zero}$ is false and $\textit{lead}$ is false, it means the current number does not contain 0, so we return $1$; otherwise, we return $0$.

For $\textit{dfs}(i, \textit{zero}, \textit{lead}, \textit{limit})$, we can enumerate the value of the current digit $d$, then recursively calculate $\textit{dfs}(i+1, \textit{nxt\_zero}, \textit{nxt\_lead}, \textit{nxt\_limit})$, where $\textit{nxt\_zero}$ indicates whether a non-zero digit has appeared in the current number, $\textit{nxt\_lead}$ indicates whether we are still processing leading zeros, and $\textit{nxt\_limit}$ indicates whether the current number is constrained by the upper bound. If $\textit{limit}$ is true, then $up$ is the upper bound of the current digit; otherwise, $up$ is $9$.

The time complexity is $O(D \log_{10} n)$, and the space complexity is $O(\log_{10} n)$, where $D$ represents the count of digits from 0 to 9.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countDistinct(self, n: int) -> int:
        @cache
        def dfs(i: int, zero: bool, lead: bool, lim: bool) -> int:
            if i >= len(s):
                return 1 if (not zero and not lead) else 0
            up = int(s[i]) if lim else 9
            ans = 0
            for j in range(up + 1):
                nxt_zero = zero or (j == 0 and not lead)
                nxt_lead = lead and j == 0
                nxt_lim = lim and j == up
                ans += dfs(i + 1, nxt_zero, nxt_lead, nxt_lim)
            return ans

        s = str(n)
        return dfs(0, False, True, True)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
