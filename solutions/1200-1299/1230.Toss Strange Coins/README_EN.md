---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1230.Toss%20Strange%20Coins/README_EN.md
rating: 1808
source: Biweekly Contest 11 Q3
tags:
    - Array
    - Math
    - Dynamic Programming
    - Probability and Statistics
---

<!-- problem:start -->

# [1230. Toss Strange Coins 🔒](https://leetcode.com/problems/toss-strange-coins)

## Description

<!-- description:start -->

<p>You have some coins.&nbsp; The <code>i</code>-th&nbsp;coin has a probability&nbsp;<code>prob[i]</code> of facing heads when tossed.</p>

<p>Return the probability that the number of coins facing heads equals <code>target</code> if you toss every coin exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> prob = [0.4], target = 1
<strong>Output:</strong> 0.40000
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> prob = [0.5,0.5,0.5,0.5,0.5], target = 0
<strong>Output:</strong> 0.03125
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prob.length &lt;= 1000</code></li>
	<li><code>0 &lt;= prob[i] &lt;= 1</code></li>
	<li><code>0 &lt;= target&nbsp;</code><code>&lt;= prob.length</code></li>
	<li>Answers will be accepted as correct if they are within <code>10^-5</code> of the correct answer.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

Let $f[i][j]$ represent the probability of having $j$ coins facing up in the first $i$ coins, and initially $f[0][0]=1$. The answer is $f[n][target]$.

Consider $f[i][j]$, where $i \geq 1$. If the current coin is facing down, then $f[i][j] = (1 - p) \times f[i - 1][j]$; If the current coin is facing up and $j \gt 0$, then $f[i][j] = p \times f[i - 1][j - 1]$. Therefore, the state transition equation is:

$$
f[i][j] = \begin{cases}
(1 - p) \times f[i - 1][j], & j = 0 \\
(1 - p) \times f[i - 1][j] + p \times f[i - 1][j - 1], & j \gt 0
\end{cases}
$$

where $p$ represents the probability of the $i$-th coin facing up.

We note that the state $f[i][j]$ is only related to $f[i - 1][j]$ and $f[i - 1][j - 1]$, so we can optimize the two-dimensional space into one-dimensional space.

The time complexity is $O(n \times target)$, and the space complexity is $O(target)$. Where $n$ is the number of coins.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, p in enumerate(prob, 1):
            for j in range(min(i, target) + 1):
                f[i][j] = (1 - p) * f[i - 1][j]
                if j:
                    f[i][j] += p * f[i - 1][j - 1]
        return f[n][target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        f = [0] * (target + 1)
        f[0] = 1
        for p in prob:
            for j in range(target, -1, -1):
                f[j] *= 1 - p
                if j:
                    f[j] += p * f[j - 1]
        return f[target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
