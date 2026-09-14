---
comments: true
difficulty: Hard
rating: 2296
source: Biweekly Contest 170 Q4
tags:
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [3753. Total Waviness of Numbers in Range II](https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii)

## Description

<!-- description:start -->

<p>You are given two integers <code>num1</code> and <code>num2</code> representing an <strong>inclusive</strong> range <code>[num1, num2]</code>.</p>

<p>The <strong>waviness</strong> of a number is defined as the total count of its <strong>peaks</strong> and <strong>valleys</strong>:</p>

<ul>
	<li>A digit is a <strong>peak</strong> if it is <strong>strictly greater</strong> than both of its immediate neighbors.</li>
	<li>A digit is a <strong>valley</strong> if it is <strong>strictly less</strong> than both of its immediate neighbors.</li>
	<li>The first and last digits of a number <strong>cannot</strong> be peaks or valleys.</li>
	<li>Any number with fewer than 3 digits has a waviness of 0.</li>
</ul>
Return the total sum of waviness for all numbers in the range <code>[num1, num2]</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 120, num2 = 130</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>In the range <code>[120, 130]</code>:</p>

<ul>
	<li><code>120</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>121</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>130</code>: middle digit 3 is a peak, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 198, num2 = 202</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>In the range <code>[198, 202]</code>:</p>

<ul>
	<li><code>198</code>: middle digit 9 is a peak, waviness = 1.</li>
	<li><code>201</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li><code>202</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 4848, num2 = 4848</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Number <code>4848</code>: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= num2 &lt;= 10<sup>15</sup></code>​​​​​​​</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

<!-- thinking:start -->

> **Thinking**
>
> The bound is $10^{15}$, so per-number simulation no longer works. The range sum is $calc(num2)-calc(num1-1)$. Filling digits from the high end, peaks and valleys depend only on the last two written digits. The DP state stores the position, those two digits, whether the number has started, and whether it is tight, and it accumulates both the count and the waviness.

<!-- thinking:end -->

We need the total waviness of all numbers in $[num1, num2]$. Convert the range query to $calc(num2) - calc(num1 - 1)$, where $calc(x)$ is the total waviness in $[1, x]$.

Use digit DP from the most significant digit. Let $dfs(pos, prev2, prev1, started, limit)$ be the number of valid numbers and their total waviness when we are filling position $pos$, the previous two digits are $prev2$ and $prev1$ (use $10$ if a digit is not yet filled), $started$ indicates whether a non-leading zero has been placed, and $limit$ indicates whether we are still bounded by the upper limit.

Enumerate the current digit $d$. If at least two digits have been placed and $prev1$ is strictly greater (or smaller) than both $prev2$ and $d$, then $prev1$ is a peak (or valley) and contributes $1$ to waviness, multiplied by the number of ways to fill the remaining digits.

The time complexity is $O(\log x)$, and the space complexity is $O(\log x)$, where $x$ is the upper bound.

Similar problems:

- [3751. Total Waviness of Numbers in Range I](https://github.com/doocs/leetcode/blob/main/solution/3700-3799/3751.Total%20Waviness%20of%20Numbers%20in%20Range%20I/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(x: int) -> int:
            if x < 0:
                return 0
            s = str(x)

            @cache
            def dfs(
                pos: int, prev2: int, prev1: int, started: int, limit: bool
            ) -> tuple:
                if pos == len(s):
                    return (started, 0)
                up = int(s[pos]) if limit else 9
                cnt = wav = 0
                for d in range(up + 1):
                    nlimit = limit and d == up
                    add = 0
                    if started == 0:
                        if d == 0:
                            ns, np2, np1 = 0, 10, 10
                        else:
                            ns, np2, np1 = 1, 10, d
                    else:
                        ns, np2, np1 = 1, prev1, d
                        if prev2 != 10 and (
                            (prev1 > prev2 and prev1 > d)
                            or (prev1 < prev2 and prev1 < d)
                        ):
                            add = 1
                    c, w = dfs(pos + 1, np2, np1, ns, nlimit)
                    cnt += c
                    wav += w + c * add
                return cnt, wav

            return dfs(0, 10, 10, 0, True)[1]

        return calc(num2) - calc(num1 - 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
