---
comments: true
difficulty: Easy
tags:
    - Memoization
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs)

## Description

<!-- description:start -->

<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

<!-- thinking:start -->

> **Thinking**
>
> The first idea is recursion: the last step is $1$ or $2$, so $f(n) = f(n-1) + f(n-2)$. $n \le 45$, and a naive recursion re-expands the same subproblems, which explodes.
>
> The bottleneck is overlap. This is the Fibonacci sequence, so we can compute it bottom-up.
>
> $f[i]$ depends only on the previous two terms, so two rolling variables suffice: $O(n)$ time and $O(1)$ extra space.

<!-- thinking:end -->

We define $f[i]$ to represent the number of ways to climb to the $i$-th step, then $f[i]$ can be transferred from $f[i - 1]$ and $f[i - 2]$, that is:

$$
f[i] = f[i - 1] + f[i - 2]
$$

The initial conditions are $f[0] = 1$ and $f[1] = 1$, that is, the number of ways to climb to the 0th step is 1, and the number of ways to climb to the 1st step is also 1.

The answer is $f[n]$.

Since $f[i]$ is only related to $f[i - 1]$ and $f[i - 2]$, we can use two variables $a$ and $b$ to maintain the current number of ways, reducing the space complexity to $O(1)$.

The time complexity is $O(n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Matrix Quick Power to Accelerate Recursion

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 is already $O(n)$, which is enough for $n \le 45$, but a linear recurrence is still slow when $n$ grows.
>
> A linear homogeneous recurrence is matrix multiplication: $F_n$ comes from $F_{n-1}$ times a fixed $2 \times 2$ transition. Fast matrix exponentiation compresses $n$ steps into $O(\log n)$. Constants are larger; use it when the same recurrence needs to be sped up.

<!-- thinking:end -->

We set $Fib(n)$ to represent a $1 \times 2$ matrix $\begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}$, where $F_n$ and $F_{n - 1}$ are the $n$-th and $(n - 1)$-th Fibonacci numbers respectively.

We hope to derive $Fib(n)$ based on $Fib(n-1) = \begin{bmatrix} F_{n - 1} & F_{n - 2} \end{bmatrix}$. That is to say, we need a matrix $base$, so that $Fib(n - 1) \times base = Fib(n)$, that is:

$$
\begin{bmatrix}
F_{n - 1} & F_{n - 2}
\end{bmatrix} \times base = \begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}
$$

Since $F_n = F_{n - 1} + F_{n - 2}$, the first column of the matrix $base$ is:

$$
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

The second column is:

$$
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

Therefore:

$$
\begin{bmatrix} F_{n - 1} & F_{n - 2} \end{bmatrix} \times \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix} = \begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}
$$

We define the initial matrix $res = \begin{bmatrix} 1 & 1 \end{bmatrix}$, then $F_n$ is equal to the first element of the first row of the result matrix of $res$ multiplied by $base^{n - 1}$. We can solve it using matrix quick power.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
import numpy as np

class Solution:
    def climbStairs(self, n: int) -> int:
        res = np.asmatrix([(1, 1)], np.dtype("O"))
        factor = np.asmatrix([(1, 1), (1, 0)], np.dtype("O"))
        n -= 1
        while n:
            if n & 1:
                res *= factor
            factor *= factor
            n >>= 1
        return res[0, 0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
