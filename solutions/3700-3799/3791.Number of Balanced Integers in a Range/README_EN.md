---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3791.Number%20of%20Balanced%20Integers%20in%20a%20Range/README_EN.md
rating: 2132
source: Weekly Contest 482 Q4
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [3791. Number of Balanced Integers in a Range](https://leetcode.com/problems/number-of-balanced-integers-in-a-range)

## Description

<!-- description:start -->

<p>You are given two integers <code>low</code> and <code>high</code>.</p>

<p>An integer is called <strong>balanced</strong> if it satisfies <strong>both</strong> of the following conditions:</p>

<ul>
	<li>It contains <strong>at least</strong> two digits.</li>
	<li>The <strong>sum of digits at even positions</strong> is equal to the <strong>sum of digits at odd positions</strong> (the leftmost digit has position 1).</li>
</ul>

<p>Return an integer representing the number of balanced integers in the range <code>[low, high]</code> (both inclusive).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">low = 1, high = 100</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>The 9 balanced numbers between 1 and 100 are 11, 22, 33, 44, 55, 66, 77, 88, and 99.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">low = 120, high = 129</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Only 121 is balanced because the sum of digits at even and odd positions are both 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">low = 1234, high = 1234</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>1234 is not balanced because the sum of digits at odd positions <code>(1 + 3 = 4)</code> does not equal the sum at even positions <code>(2 + 4 = 6)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>15</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

First, if $\textit{high} < 11$, there are no balanced integers in the range, so we directly return $0$. Otherwise, we update $\textit{low}$ to $\max(\textit{low}, 11)$.

Then we design a function $\textit{dfs}(\textit{pos}, \textit{diff}, \textit{lim})$, which represents processing the $\textit{pos}$-th digit of the number, where $\textit{diff}$ is the difference between the sum of digits at odd positions and the sum of digits at even positions, and $\textit{lim}$ indicates whether the current digit is constrained by the upper bound. The function returns the number of balanced integers that can be constructed from the current state.

The execution logic of the function is as follows:

- If $\textit{pos}$ exceeds the length of the number, it means all digits have been processed. If $\textit{diff} = 0$, the current number is a balanced integer, return $1$; otherwise, return $0$.
- Calculate the upper bound $\textit{up}$ for the current digit. If constrained, it equals the current digit of the number; otherwise, it is $9$.
- Iterate through all possible digits $i$ for the current position. For each digit $i$, recursively call $\textit{dfs}(\textit{pos} + 1, \textit{diff} + i \times (\text{1 if pos \% 2 == 0 else -1}), \textit{lim} \&\& i == \textit{up})$, and accumulate the results.
- Return the accumulated result.

We first calculate the number of balanced integers $\textit{a}$ in the range $[1, \textit{low} - 1]$, then calculate the number of balanced integers $\textit{b}$ in the range $[1, \textit{high}]$, and finally return $\textit{b} - \textit{a}$.

To avoid redundant calculations, we use memoization to store previously computed states.

The time complexity is $O(\log^2 M \times D^2)$, and the space complexity is $O(\log^2 M \times D)$. Here, $M$ is the value of $\textit{high}$, and $D = 10$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        @cache
        def dfs(pos: int, diff: int, lim: int) -> int:
            if pos >= len(num):
                return 1 if diff == 0 else 0
            res = 0
            up = int(num[pos]) if lim else 9
            for i in range(up + 1):
                res += dfs(
                    pos + 1, diff + i * (1 if pos % 2 == 0 else -1), lim and i == up
                )
            return res

        if high < 11:
            return 0
        low = max(low, 11)
        num = str(low - 1)
        a = dfs(0, 0, True)
        dfs.cache_clear()
        num = str(high)
        b = dfs(0, 0, True)
        return b - a
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
