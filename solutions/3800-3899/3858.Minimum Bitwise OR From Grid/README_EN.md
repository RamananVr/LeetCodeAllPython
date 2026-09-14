---
comments: true
difficulty: Medium
rating: 1947
source: Weekly Contest 491 Q3
---

<!-- problem:start -->

# [3858. Minimum Bitwise OR From Grid](https://leetcode.com/problems/minimum-bitwise-or-from-grid)

## Description

<!-- description:start -->

<p>You are given a 2D integer array <code>grid</code> of size <code>m x n</code>.</p>

<p>You must select <strong>exactly one</strong> integer from each row of the grid.</p>

<p>Return an integer denoting the <strong>minimum possible bitwise OR</strong> of the selected integers from each row.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,5],[2,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose 1 from the first row and 2 from the second row.</li>
	<li>The bitwise OR of <code>1 | 2 = 3</code>​​​​​​​, which is the minimum possible.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[3,5],[6,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose 5 from the first row and 4 from the second row.</li>
	<li>The bitwise OR of <code>5 | 4 = 5</code>​​​​​​​, which is the minimum possible.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[7,9,8]]</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choosing 7 gives the minimum bitwise OR.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= n == grid[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup>​​​​​​​</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Pick one number per row to minimize the bitwise OR. At most $10^5$ cells, so selections cannot be enumerated.
>
> We want high bits of the OR to stay $0$. Try bits from high to low: given higher bits already fixed, ask whether every row still has a value compatible with those bits (lower bits free).
>
> For the trial mask $\textit{ans} \mid (2^i-1)$, if each row has an $x$ covered by the mask, the current bit may stay $0$; otherwise it must be set.
>
> High-bit-first filling yields the minimum OR.

<!-- thinking:end -->
<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        mx = max(map(max, grid))
        m = mx.bit_length()
        ans = 0
        for i in range(m - 1, -1, -1):
            mask = ans | ((1 << i) - 1)
            for row in grid:
                found = False
                for x in row:
                    if (x | mask) == mask:
                        found = True
                        break
                if not found:
                    ans |= 1 << i
                    break
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
