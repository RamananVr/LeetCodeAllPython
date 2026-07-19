---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1220.Count%20Vowels%20Permutation/README_EN.md
rating: 1729
source: Weekly Contest 157 Q4
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [1220. Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, your task is to count how many strings of length <code>n</code> can be formed under the following rules:</p>

<ul>
	<li>Each character is a lower case vowel&nbsp;(<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, <code>&#39;u&#39;</code>)</li>
	<li>Each vowel&nbsp;<code>&#39;a&#39;</code> may only be followed by an <code>&#39;e&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;e&#39;</code> may only be followed by an <code>&#39;a&#39;</code>&nbsp;or an <code>&#39;i&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;i&#39;</code> <strong>may not</strong> be followed by another <code>&#39;i&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;o&#39;</code> may only be followed by an <code>&#39;i&#39;</code> or a&nbsp;<code>&#39;u&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;u&#39;</code> may only be followed by an <code>&#39;a&#39;</code>.</li>
</ul>

<p>Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;<code>10^9 + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> All possible strings are: &quot;a&quot;, &quot;e&quot;, &quot;i&quot; , &quot;o&quot; and &quot;u&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> All possible strings are: &quot;ae&quot;, &quot;ea&quot;, &quot;ei&quot;, &quot;ia&quot;, &quot;ie&quot;, &quot;io&quot;, &quot;iu&quot;, &quot;oi&quot;, &quot;ou&quot; and &quot;ua&quot;.
</pre>

<p><strong class="example">Example 3:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 68</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10^4</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

Based on the problem description, we can list the possible subsequent vowels for each vowel:

```bash
a [e]
e [a|i]
i [a|e|o|u]
o [i|u]
u [a]
```

From this, we can deduce the possible preceding vowels for each vowel:

```bash
[e|i|u]	a
[a|i]	e
[e|o]	i
[i]	o
[i|o]	u
```

We define $f[i]$ as the number of strings of the current length ending with the $i$-th vowel. If the length is $1$, then $f[i]=1$.

When the length is greater than $1$, we define $g[i]$ as the number of strings of the current length ending with the $i$-th vowel. Then $g[i]$ can be derived from $f$, that is:

$$
g[i]=
\begin{cases}
f[1]+f[2]+f[4] & i=0 \\
f[0]+f[2] & i=1 \\
f[1]+f[3] & i=2 \\
f[2] & i=3 \\
f[2]+f[3] & i=4
\end{cases}
$$

The final answer is $\sum_{i=0}^{4}f[i]$. Note that the answer may be very large, so we need to take the modulus of $10^9+7$.

The time complexity is $O(n)$, and the space complexity is $O(C)$. Here, $n$ is the length of the string, and $C$ is the number of vowels. In this problem, $C=5$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        f = [1] * 5
        mod = 10**9 + 7
        for _ in range(n - 1):
            g = [0] * 5
            g[0] = (f[1] + f[2] + f[4]) % mod
            g[1] = (f[0] + f[2]) % mod
            g[2] = (f[1] + f[3]) % mod
            g[3] = f[2]
            g[4] = (f[2] + f[3]) % mod
            f = g
        return sum(f) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Matrix Exponentiation to Accelerate Recursion

The time complexity is $O(C^3 \times \log n)$, and the space complexity is $O(C^2)$. Here, $C$ is the number of vowels. In this problem, $C=5$.

<!-- tabs:start -->

#### Python3

```python
import numpy as np

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        factor = np.asmatrix(
            [
                (0, 1, 0, 0, 0),
                (1, 0, 1, 0, 0),
                (1, 1, 0, 1, 1),
                (0, 0, 1, 0, 1),
                (1, 0, 0, 0, 0),
            ],
            np.dtype("O"),
        )
        res = np.asmatrix([(1, 1, 1, 1, 1)], np.dtype("O"))
        n -= 1
        while n:
            if n & 1:
                res = res * factor % mod
            factor = factor * factor % mod
            n >>= 1
        return res.sum() % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
