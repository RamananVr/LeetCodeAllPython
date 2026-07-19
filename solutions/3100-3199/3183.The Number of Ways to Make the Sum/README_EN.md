---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3183.The%20Number%20of%20Ways%20to%20Make%20the%20Sum/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3183. The Number of Ways to Make the Sum 🔒](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum)

## Description

<!-- description:start -->

<p>You have an <strong>infinite</strong> number of coins with values 1, 2, and 6, and <strong>only</strong> 2 coins with value 4.</p>

<p>Given an integer <code>n</code>, return the number of ways to make the sum of <code>n</code> with the coins you have.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note</strong> that the order of the coins doesn&#39;t matter and <code>[2, 2, 3]</code> is the same as <code>[2, 3, 2]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Here are the four combinations: <code>[1, 1, 1, 1]</code>, <code>[1, 1, 2]</code>, <code>[2, 2]</code>, <code>[4]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 12</span></p>

<p><strong>Output:</strong> <span class="example-io">22</span></p>

<p><strong>Explanation:</strong></p>

<p>Note that <code>[4, 4, 4]</code> is <strong>not</strong> a valid combination since we cannot use 4 three times.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Here are the four combinations: <code>[1, 1, 1, 1, 1]</code>, <code>[1, 1, 1, 2]</code>, <code>[1, 2, 2]</code>, <code>[1, 4]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming (Complete Knapsack)

We can start by ignoring coin $4$, defining the coin array `coins = [1, 2, 6]`, and then using the idea of the complete knapsack problem. We define $f[j]$ as the number of ways to make up amount $j$ using the first $i$ types of coins, initially $f[0] = 1$. Then, we iterate through the coin array `coins`, and for each coin $x$, we iterate through amounts from $x$ to $n$, updating $f[j] = f[j] + f[j - x]$.

Finally, $f[n]$ is the number of ways to make up amount $n$ using coins $1, 2, 6$. Then, if $n \geq 4$, we consider choosing one coin $4$, so the number of ways becomes $f[n] + f[n - 4]$, and if $n \geq 8$, we consider choosing two coins $4$, so the number of ways becomes $f[n] + f[n - 4] + f[n - 8]$.

Note the modulus operation for the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the amount.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [1, 2, 6]
        f = [0] * (n + 1)
        f[0] = 1
        for x in coins:
            for j in range(x, n + 1):
                f[j] = (f[j] + f[j - x]) % mod
        ans = f[n]
        if n >= 4:
            ans = (ans + f[n - 4]) % mod
        if n >= 8:
            ans = (ans + f[n - 8]) % mod
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Preprocessing + Dynamic Programming (Complete Knapsack)

We can start by preprocessing the number of ways to make up every amount from $1$ to $10^5$, and then return the corresponding number of ways based on the value of $n$:

- If $n < 4$, directly return $f[n]$;
- If $4 \leq n < 8$, return $f[n] + f[n - 4]$;
- If $n \geq 8$, return $f[n] + f[n - 4] + f[n - 8]$.

Note the modulus operation for the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the amount.

<!-- tabs:start -->

#### Python3

```python
m = 10**5 + 1
mod = 10**9 + 7
coins = [1, 2, 6]
f = [0] * (m)
f[0] = 1
for x in coins:
    for j in range(x, m):
        f[j] = (f[j] + f[j - x]) % mod

class Solution:
    def numberOfWays(self, n: int) -> int:
        ans = f[n]
        if n >= 4:
            ans = (ans + f[n - 4]) % mod
        if n >= 8:
            ans = (ans + f[n - 8]) % mod
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
