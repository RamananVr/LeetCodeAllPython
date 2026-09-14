---
comments: true
difficulty: Medium
tags:
    - Breadth-First Search
    - Math
    - Dynamic Programming
    - Knapsack
    - Unbounded Knapsack
---

<!-- problem:start -->

# [279. Perfect Squares](https://leetcode.com/problems/perfect-squares)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em>the least number of perfect square numbers that sum to</em> <code>n</code>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, <code>1</code>, <code>4</code>, <code>9</code>, and <code>16</code> are perfect squares while <code>3</code> and <code>11</code> are not.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong> 12 = 4 + 4 + 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 2
<strong>Explanation:</strong> 13 = 4 + 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming (Complete Knapsack)

<!-- thinking:start -->

> **Thinking**
>
> Perfect squares may be reused, so the fewest that sum to $n$ is an unbounded knapsack with items $1^2,\ldots,m^2$ where $m=\lfloor\sqrt{n}\rfloor$.
>
> $f[i][j]$ is the fewest squares among the first $i$ kinds that sum to $j$: skip $i^2$, or take one more copy.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numSquares(self, n: int) -> int:
        m = int(sqrt(n))
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            for j in range(n + 1):
                f[i][j] = f[i - 1][j]
                if j >= i * i:
                    f[i][j] = min(f[i][j], f[i][j - i * i] + 1)
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Optimized Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> $f[i][j]$ depends only on $f[i-1][j]$ and $f[i][j-i^2]$, so a 1-D array updated in increasing $j$ is enough.

<!-- thinking:end -->

$f[i][j]$ depends only on $f[i - 1][j]$ and $f[i][j - i^2]$, so the table can be rolled into a 1D array of space $O(n)$. The time complexity stays $O(m \times n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numSquares(self, n: int) -> int:
        m = int(sqrt(n))
        f = [0] + [inf] * n
        for i in range(1, m + 1):
            for j in range(i * i, n + 1):
                f[j] = min(f[j], f[j - i * i] + 1)
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
