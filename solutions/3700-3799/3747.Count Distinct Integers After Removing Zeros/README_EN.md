---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3747.Count%20Distinct%20Integers%20After%20Removing%20Zeros/README_EN.md
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

The problem essentially asks us to count the number of integers in the range $[1, n]$ that do not contain the digit 0. We can solve this problem using digit DP.

We design a function $\text{dfs}(i, \text{zero}, \text{lead}, \text{limit})$, which represents the number of valid solutions when we are currently processing the $i$-th digit of the number. We use $\text{zero}$ to indicate whether a non-zero digit has appeared in the current number, $\text{lead}$ to indicate whether we are still processing leading zeros, and $\text{limit}$ to indicate whether the current number is constrained by the upper bound. The answer is $\text{dfs}(0, 0, 1, 1)$.

In the function $\text{dfs}(i, \text{zero}, \text{lead}, \text{limit})$, if $i$ is greater than or equal to the length of the number, we can check $\text{zero}$ and $\text{lead}$. If $\text{zero}$ is false and $\text{lead}$ is false, it means the current number does not contain 0, so we return $1$; otherwise, we return $0$.

For $\text{dfs}(i, \text{zero}, \text{lead}, \text{limit})$, we can enumerate the value of the current digit $d$, then recursively calculate $\text{dfs}(i+1, \text{nxt\_zero}, \text{nxt\_lead}, \text{nxt\_limit})$, where $\text{nxt\_zero}$ indicates whether a non-zero digit has appeared in the current number, $\text{nxt\_lead}$ indicates whether we are still processing leading zeros, and $\text{nxt\_limit}$ indicates whether the current number is constrained by the upper bound. If $\text{limit}$ is true, then $up$ is the upper bound of the current digit; otherwise, $up$ is $9$.

The time complexity is $O(\log_{10} n \times D)$ and the space complexity is $O(\log_{10} n)$, where $D$ represents the count of digits from 0 to 9.

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
