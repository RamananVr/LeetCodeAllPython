---
comments: true
difficulty: Hard
rating: 2123
source: Weekly Contest 469 Q3
---

<!-- problem:start -->

# [3699. Number of ZigZag Arrays I](https://leetcode.com/problems/number-of-zigzag-arrays-i)

## Description

<!-- description:start -->

<p>You are given three integers <code>n</code>, <code>l</code>, and <code>r</code>.</p>

<p>A <strong>ZigZag</strong> array of length <code>n</code> is defined as follows:</p>

<ul>
	<li>Each element lies in the range <code>[l, r]</code>.</li>
	<li>No <strong>two</strong> adjacent elements are equal.</li>
	<li>No <strong>three</strong> consecutive elements form a <strong>strictly increasing</strong> or <strong>strictly decreasing</strong> sequence.</li>
</ul>

<p>Return the total number of valid <strong>ZigZag</strong> arrays.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>sequence</strong> is said to be <strong>strictly increasing</strong> if each element is strictly greater than its previous one (if exists).</p>

<p>A <strong>sequence</strong> is said to be <strong>strictly decreasing</strong> if each element is strictly smaller than its previous one (if exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, l = 4, r = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There are only 2 valid ZigZag arrays of length <code>n = 3</code> using values in the range <code>[4, 5]</code>:</p>

<ul>
	<li><code>[4, 5, 4]</code></li>
	<li><code>[5, 4, 5]</code>​​​​​​​</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, l = 1, r = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 10 valid ZigZag arrays of length <code>n = 3</code> using values in the range <code>[1, 3]</code>:</p>

<ul>
	<li><code>[1, 2, 1]</code>, <code>[1, 3, 1]</code>, <code>[1, 3, 2]</code></li>
	<li><code>[2, 1, 2]</code>, <code>[2, 1, 3]</code>, <code>[2, 3, 1]</code>, <code>[2, 3, 2]</code></li>
	<li><code>[3, 1, 2]</code>, <code>[3, 1, 3]</code>, <code>[3, 2, 3]</code></li>
</ul>

<p>All arrays meet the ZigZag conditions.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= l &lt; r &lt;= 2000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> A zigzag array alternates the sign of consecutive differences. Values lie in $[l,r]$ and $n\le 2000$, so we shift the range to $[0,m-1]$ and DP.
>
> $\textit{up}[i]$ and $\textit{down}[i]$ count arrays ending at $i$ whose last step rises or falls. A descent sums all larger $\textit{up}$; an ascent sums all smaller $\textit{down}$.
>
> Prefix and suffix sums make each of the $n-1$ rounds $O(m)$. Length $1$ seeds both directions with $1$. Reduce the total modulo $10^9+7$.

<!-- thinking:end -->

Let $m = r - l + 1$ and map the range $[l, r]$ to $[0, m - 1]$.

Let $up[i]$ be the number of arrays of the current length that end with $i$ whose last step is an increase, and $down[i]$ the number whose last step is a decrease. For length $1$ there is no direction, so initialize $up[i] = down[i] = 1$.

Transitions:

- If the array ends at $i$ with a decrease, the previous value must be greater than $i$ and the previous step must be an increase: $down'[i] = \sum_{j > i} up[j]$;
- If the last step is an increase: $up'[i] = \sum_{j < i} down[j]$.

Prefix and suffix sums make each transition $O(m)$. Repeat $n - 1$ times. The answer is the sum of all $up[i] + down[i]$.

The time complexity is $O(n \times m)$, and the space complexity is $O(m)$, where $n$ is the array length and $m$ is the size of the value range.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        m = r - l + 1
        up = [1] * m
        down = [1] * m
        for _ in range(n - 1):
            pre = [0] * (m + 1)
            suf = [0] * (m + 1)
            for i in range(m):
                pre[i + 1] = (pre[i] + down[i]) % mod
            for i in range(m - 1, -1, -1):
                suf[i] = (suf[i + 1] + up[i]) % mod
            up = pre[:m]
            down = suf[1:]
        return sum(up + down) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
