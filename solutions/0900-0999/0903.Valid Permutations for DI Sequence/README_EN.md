---
comments: true
difficulty: Hard
tags:
    - String
    - Dynamic Programming
    - Prefix Sum
---

<!-- problem:start -->

# [903. Valid Permutations for DI Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> of length <code>n</code> where <code>s[i]</code> is either:</p>

<ul>
	<li><code>&#39;D&#39;</code> means decreasing, or</li>
	<li><code>&#39;I&#39;</code> means increasing.</li>
</ul>

<p>A permutation <code>perm</code> of <code>n + 1</code> integers of all the integers in the range <code>[0, n]</code> is called a <strong>valid permutation</strong> if for all valid <code>i</code>:</p>

<ul>
	<li>If <code>s[i] == &#39;D&#39;</code>, then <code>perm[i] &gt; perm[i + 1]</code>, and</li>
	<li>If <code>s[i] == &#39;I&#39;</code>, then <code>perm[i] &lt; perm[i + 1]</code>.</li>
</ul>

<p>Return <em>the number of <strong>valid permutations</strong> </em><code>perm</code>. Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;DID&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;D&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>s[i]</code> is either <code>&#39;I&#39;</code> or <code>&#39;D&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> A DI string of length $n$ asks for permutations of $0..n$. $n$ can be $200$, so listing permutations is impossible. After $i$ numbers are placed, only the rank $j$ among the remaining values matters for the next rise or fall.
>
> Let $f[i][j]$ be the number of ways for the first $i$ characters ending at rank $j$. `'D'` sums from larger ranks and `'I'` from smaller ones, after ranks are compressed into $[0,i]$. The resulting recurrence is cubic.

<!-- thinking:end -->

We define $f[i][j]$ as the number of permutations that satisfy the problem's requirements with the first $i$ characters of the string ending with the number $j$. Initially, $f[0][0]=1$, and the rest $f[0][j]=0$. The answer is $\sum_{j=0}^n f[n][j]$.

Consider $f[i][j]$, where $j \in [0, i]$.

If the $i$th character $s[i-1]$ is `'D'`, then $f[i][j]$ can be transferred from $f[i-1][k]$, where $k \in [j+1, i]$. Since $k-1$ can only be up to $i-1$, we move $k$ one place to the left, so $k \in [j, i-1]$. Therefore, we have $f[i][j] = \sum_{k=j}^{i-1} f[i-1][k]$.

If the $i$th character $s[i-1]$ is `'I'`, then $f[i][j]$ can be transferred from $f[i-1][k]$, where $k \in [0, j-1]$. Therefore, we have $f[i][j] = \sum_{k=0}^{j-1} f[i-1][k]$.

The final answer is $\sum_{j=0}^n f[n][j]$.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, c in enumerate(s, 1):
            if c == "D":
                for j in range(i + 1):
                    for k in range(j, i):
                        f[i][j] = (f[i][j] + f[i - 1][k]) % mod
            else:
                for j in range(i + 1):
                    for k in range(j):
                        f[i][j] = (f[i][j] + f[i - 1][k]) % mod
        return sum(f[n][j] for j in range(n + 1)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Prefix Sum Optimization

<!-- thinking:start -->

> **Thinking**
>
> Method 1 scans a range of $k$ for every $j$, and adjacent $j$ share almost the same interval sum. A directional prefix sum evaluates $\sum f[i-1][k]$ in constant time, dropping the time to quadratic without changing the state.

<!-- thinking:end -->

We can optimize the state transitions with prefix sums, reducing the time complexity to $O(n^2)$. The space complexity remains $O(n^2)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, c in enumerate(s, 1):
            pre = 0
            if c == "D":
                for j in range(i, -1, -1):
                    pre = (pre + f[i - 1][j]) % mod
                    f[i][j] = pre
            else:
                for j in range(i + 1):
                    f[i][j] = pre
                    pre = (pre + f[i - 1][j]) % mod
        return sum(f[n][j] for j in range(n + 1)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Rolling Array Optimization

<!-- thinking:start -->

> **Thinking**
>
> $f[i]$ depends only on $f[i-1]$, so the second dimension of the table can be discarded. Roll a one-dimensional array and write the next layer from a running sum in the `'D'` or `'I'` direction, using linear extra space.

<!-- thinking:end -->

Based on Solution 2, we use a rolling array to reduce the space complexity to $O(n)$. The time complexity remains $O(n^2)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        f = [1] + [0] * n
        for i, c in enumerate(s, 1):
            pre = 0
            g = [0] * (n + 1)
            if c == "D":
                for j in range(i, -1, -1):
                    pre = (pre + f[j]) % mod
                    g[j] = pre
            else:
                for j in range(i + 1):
                    g[j] = pre
                    pre = (pre + f[j]) % mod
            f = g
        return sum(f) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
