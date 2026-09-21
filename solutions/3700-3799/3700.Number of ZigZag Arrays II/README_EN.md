---
comments: true
difficulty: Hard
rating: 2435
source: Weekly Contest 469 Q4
---

<!-- problem:start -->

# [3700. Number of ZigZag Arrays II](https://leetcode.com/problems/number-of-zigzag-arrays-ii)

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
	<li><code>[5, 4, 5]</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, l = 1, r = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>​​​​​​​There are 10 valid ZigZag arrays of length <code>n = 3</code> using values in the range <code>[1, 3]</code>:</p>

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
	<li><code>3 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l &lt; r &lt;= 75</code>​​​​​​​</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> $n$ can reach $10^9$, so a length-by-length DP is impossible; the value range has length $m=r-l+1\le 75$, which keeps the state space small. A zigzag array forbids equal neighbors and any strictly monotone triple, which means the comparison direction must flip at every step. We therefore encode a state by the last value and last direction ($2m$ states). The transition is independent of the remaining length, so we build a $2m\times 2m$ matrix, raise it to the $(n-1)$-st power, and multiply by the length-$1$ initial vector.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        trans = [[0] * size for _ in range(size)]
        for x in range(m):
            for y in range(x):
                trans[y][m + x] = 1
        for x in range(m):
            for y in range(x + 1, m):
                trans[m + y][x] = 1

        def mul_mat(a, b):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if a[i][k] == 0:
                        continue
                    aik = a[i][k]
                    for j in range(size):
                        if b[k][j]:
                            res[i][j] = (res[i][j] + aik * b[k][j]) % mod
            return res

        def mul_vec(mat, vec):
            res = [0] * size
            for i in range(size):
                s = 0
                for j in range(size):
                    s = (s + mat[i][j] * vec[j]) % mod
                res[i] = s
            return res

        power = [[int(i == j) for j in range(size)] for i in range(size)]
        exp = n - 1
        while exp:
            if exp & 1:
                power = mul_mat(power, trans)
            trans = mul_mat(trans, trans)
            exp >>= 1
        init = [1] * size
        return sum(mul_vec(power, init)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
