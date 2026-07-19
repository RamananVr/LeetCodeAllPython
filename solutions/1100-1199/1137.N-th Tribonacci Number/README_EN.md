---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1137.N-th%20Tribonacci%20Number/README_EN.md
rating: 1142
source: Weekly Contest 147 Q1
tags:
    - Memoization
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number)

## Description

<!-- description:start -->

<p>The Tribonacci sequence T<sub>n</sub> is defined as follows:&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n &gt;= 0.</p>

<p>Given <code>n</code>, return the value of T<sub>n</sub>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 25
<strong>Output:</strong> 1389537
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer &lt;= 2^31 - 1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

According to the recurrence relation given in the problem, we can use dynamic programming to solve it.

We define three variables $a$, $b$, $c$ to represent $T_{n-3}$, $T_{n-2}$, $T_{n-1}$, respectively, with initial values of $0$, $1$, $1$.

Then we decrease $n$ to $0$, updating the values of $a$, $b$, $c$ each time, until $n$ is $0$, at which point the answer is $a$.

The time complexity is $O(n)$, and the space complexity is $O(1)$. Here, $n$ is the given integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Matrix Exponentiation to Accelerate Recurrence

We define $Tib(n)$ as a $1 \times 3$ matrix $\begin{bmatrix} T_n & T_{n - 1} & T_{n - 2} \end{bmatrix}$, where $T_n$, $T_{n - 1}$ and $T_{n - 2}$ represent the $n$th, $(n - 1)$th and $(n - 2)$th Tribonacci numbers, respectively.

We hope to derive $Tib(n)$ from $Tib(n-1) = \begin{bmatrix} T_{n - 1} & T_{n - 2} & T_{n - 3} \end{bmatrix}$. That is, we need a matrix $base$ such that $Tib(n - 1) \times base = Tib(n)$, i.e.,

$$
\begin{bmatrix}
T_{n - 1} & T_{n - 2} & T_{n - 3}
\end{bmatrix} \times base = \begin{bmatrix} T_n & T_{n - 1} & T_{n - 2} \end{bmatrix}
$$

Since $T_n = T_{n - 1} + T_{n - 2} + T_{n - 3}$, the matrix $base$ is:

$$
\begin{bmatrix}
 1 & 1 & 0 \\
 1 & 0 & 1 \\
 1 & 0 & 0
\end{bmatrix}
$$

We define the initial matrix $res = \begin{bmatrix} 1 & 1  & 0 \end{bmatrix}$, then $T_n$ is equal to the sum of all elements in the result matrix of $res$ multiplied by $base^{n - 3}$. This can be solved using matrix exponentiation.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
import numpy as np

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        factor = np.asmatrix([(1, 1, 0), (1, 0, 1), (1, 0, 0)], np.dtype("O"))
        res = np.asmatrix([(1, 1, 0)], np.dtype("O"))
        n -= 3
        while n:
            if n & 1:
                res *= factor
            factor *= factor
            n >>= 1
        return res.sum()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
