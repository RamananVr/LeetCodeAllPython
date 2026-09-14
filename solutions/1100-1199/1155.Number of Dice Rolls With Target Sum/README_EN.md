---
comments: true
difficulty: Medium
rating: 1653
source: Weekly Contest 149 Q2
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [1155. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum)

## Description

<!-- description:start -->

<p>You have <code>n</code> dice, and each dice has <code>k</code> faces numbered from <code>1</code> to <code>k</code>.</p>

<p>Given three integers <code>n</code>, <code>k</code>, and <code>target</code>, return <em>the number of possible ways (out of the </em><code>k<sup>n</sup></code><em> total ways) </em><em>to roll the dice, so the sum of the face-up numbers equals </em><code>target</code>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 6, target = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> You throw one die with 6 faces.
There is only one way to get a sum of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 6, target = 7
<strong>Output:</strong> 6
<strong>Explanation:</strong> You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 30, k = 30, target = 500
<strong>Output:</strong> 222616187
<strong>Explanation:</strong> The answer must be returned modulo 10<sup>9</sup> + 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 30</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Naively assigning $n$ $k$-faced dice to sum to $target$ is $k^n$. Let $f[i][j]$ be the ways for $i$ dice to sum to $j$; face $h$ on the last die comes from $f[i-1][j-h]$. One way uses zero dice to make $0$. Reduce modulo $10^9+7$.

<!-- thinking:end -->

We define $f[i][j]$ as the number of ways to get a sum of $j$ using $i$ dice. Then, we can obtain the following state transition equation:

$$
f[i][j] = \sum_{h=1}^{\min(j, k)} f[i-1][j-h]
$$

where $h$ represents the number of points on the $i$-th die.

Initially, we have $f[0][0] = 1$, and the final answer is $f[n][target]$.

The time complexity is $O(n \times k \times target)$, and the space complexity is $O(n \times target)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, n + 1):
            for j in range(1, min(i * k, target) + 1):
                for h in range(1, min(j, k) + 1):
                    f[i][j] = (f[i][j] + f[i - 1][j - h]) % mod
        return f[n][target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming (Rolling Array)

<!-- thinking:start -->

> **Thinking**
>
> Row $i$ of method 1 depends only on row $i-1$. Two rolling arrays cut space from $O(n\times target)$ to $O(target)$ with the same transition.

<!-- thinking:end -->

$f[i][j]$ depends only on the previous row, so two arrays $f$ and $g$ of length $target+1$ are enough. The space complexity becomes $O(target)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        f = [1] + [0] * target
        mod = 10**9 + 7
        for i in range(1, n + 1):
            g = [0] * (target + 1)
            for j in range(1, min(i * k, target) + 1):
                for h in range(1, min(j, k) + 1):
                    g[j] = (g[j] + f[j - h]) % mod
            f = g
        return f[target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
