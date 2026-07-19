---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3405.Count%20the%20Number%20of%20Arrays%20with%20K%20Matching%20Adjacent%20Elements/README_EN.md
rating: 2309
source: Weekly Contest 430 Q4
tags:
    - Math
    - Combinatorics
---

<!-- problem:start -->

# [3405. Count the Number of Arrays with K Matching Adjacent Elements](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements)

## Description

<!-- description:start -->

<p>You are given three integers <code>n</code>, <code>m</code>, <code>k</code>. A <strong>good array</strong> <code>arr</code> of size <code>n</code> is defined as follows:</p>

<ul>
	<li>Each element in <code>arr</code> is in the <strong>inclusive</strong> range <code>[1, m]</code>.</li>
	<li><em>Exactly</em> <code>k</code> indices <code>i</code> (where <code>1 &lt;= i &lt; n</code>) satisfy the condition <code>arr[i - 1] == arr[i]</code>.</li>
</ul>

<p>Return the number of <strong>good arrays</strong> that can be formed.</p>

<p>Since the answer may be very large, return it <strong>modulo </strong><code>10<sup>9 </sup>+ 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, m = 2, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There are 4 good arrays. They are <code>[1, 1, 2]</code>, <code>[1, 2, 2]</code>, <code>[2, 1, 1]</code> and <code>[2, 2, 1]</code>.</li>
	<li>Hence, the answer is 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, m = 2, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The good arrays are <code>[1, 1, 1, 2]</code>, <code>[1, 1, 2, 2]</code>, <code>[1, 2, 2, 2]</code>, <code>[2, 1, 1, 1]</code>, <code>[2, 2, 1, 1]</code> and <code>[2, 2, 2, 1]</code>.</li>
	<li>Hence, the answer is 6.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, m = 2, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The good arrays are <code>[1, 2, 1, 2, 1]</code> and <code>[2, 1, 2, 1, 2]</code>. Hence, the answer is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= n - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Combinatorics + Fast Power

For an array of length $n$, there are $n - 1$ pairs of adjacent elements. We need to select $k$ of these $n - 1$ adjacent pairs such that the two elements in each of these $k$ pairs are equal, and the remaining $n - 1 - k$ adjacent pairs have different elements.

This is equivalent to splitting the array $n - 1 - k$ times, resulting in $n - k$ segments, where all elements in each segment are equal. The number of ways to split is $C_{n - 1}^{n - 1 - k} = C_{n - 1}^{k}$.

For the first segment, we can choose any element from $[1, m]$. For the remaining $n - k - 1$ segments, we just need to ensure that the element in each segment is different from the previous segment, so each of these segments has $m - 1$ choices. In total, there are $m \times (m - 1)^{n - k - 1}$ ways to choose.

Combining the two parts above, we get the answer:

$$
C_{n - 1}^{k} \times m \times (m - 1)^{n - k - 1} \bmod (10^9 + 7)
$$

In the code implementation, we can precompute factorials and inverses, and use fast power to calculate combinations.

Ignoring the preprocessing time and space, the time complexity is $O(\log (n - k))$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
mx = 10**5 + 10
mod = 10**9 + 7
f = [1] + [0] * mx
g = [1] + [0] * mx

for i in range(1, mx):
    f[i] = f[i - 1] * i % mod
    g[i] = pow(f[i], mod - 2, mod)

def comb(m: int, n: int) -> int:
    return f[m] * g[n] * g[m - n] % mod

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n - 1, k) * m * pow(m - 1, n - k - 1, mod) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
