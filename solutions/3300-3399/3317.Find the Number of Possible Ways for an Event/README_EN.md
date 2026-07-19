---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3317.Find%20the%20Number%20of%20Possible%20Ways%20for%20an%20Event/README_EN.md
rating: 2413
source: Biweekly Contest 141 Q4
tags:
    - Math
    - Dynamic Programming
    - Combinatorics
---

<!-- problem:start -->

# [3317. Find the Number of Possible Ways for an Event](https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event)

## Description

<!-- description:start -->

<p>You are given three integers <code>n</code>, <code>x</code>, and <code>y</code>.</p>

<p>An event is being held for <code>n</code> performers. When a performer arrives, they are <strong>assigned</strong> to one of the <code>x</code> stages. All performers assigned to the <strong>same</strong> stage will perform together as a band, though some stages <em>might</em> remain <strong>empty</strong>.</p>

<p>After all performances are completed, the jury will <strong>award</strong> each band a score in the range <code>[1, y]</code>.</p>

<p>Return the <strong>total</strong> number of possible ways the event can take place.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note</strong> that two events are considered to have been held <strong>differently</strong> if <strong>either</strong> of the following conditions is satisfied:</p>

<ul>
	<li><strong>Any</strong> performer is <em>assigned</em> a different stage.</li>
	<li><strong>Any</strong> band is <em>awarded</em> a different score.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1, x = 2, y = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There are 2 ways to assign a stage to the performer.</li>
	<li>The jury can award a score of either 1, 2, or 3 to the only band.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, x = 2, y = 1</span></p>

<p><strong>Output:</strong> 32</p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Each performer will be assigned either stage 1 or stage 2.</li>
	<li>All bands will be awarded a score of 1.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, x = 3, y = 4</span></p>

<p><strong>Output:</strong> 684</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, x, y &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ to represent the number of ways to arrange the first $i$ performers into $j$ programs. Initially, $f[0][0] = 1$, and the rest $f[i][j] = 0$.

For $f[i][j]$, where $1 \leq i \leq n$ and $1 \leq j \leq x$, we consider the $i$-th performer:

- If the performer is assigned to a program that already has performers, there are $j$ choices, i.e., $f[i - 1][j] \times j$;
- If the performer is assigned to a program that has no performers, there are $x - (j - 1)$ choices, i.e., $f[i - 1][j - 1] \times (x - (j - 1))$.

So the state transition equation is:

$$
f[i][j] = f[i - 1][j] \times j + f[i - 1][j - 1] \times (x - (j - 1))
$$

For each $j$, there are $y^j$ choices, so the final answer is:

$$
\sum_{j = 1}^{x} f[n][j] \times y^j
$$

Note that since the answer can be very large, we need to take the modulo $10^9 + 7$.

The time complexity is $O(n \times x)$, and the space complexity is $O(n \times x)$. Here, $n$ and $x$ represent the number of performers and the number of programs, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 10**9 + 7
        f = [[0] * (x + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, x + 1):
                f[i][j] = (f[i - 1][j] * j + f[i - 1][j - 1] * (x - (j - 1))) % mod
        ans, p = 0, 1
        for j in range(1, x + 1):
            p = p * y % mod
            ans = (ans + f[n][j] * p) % mod
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
