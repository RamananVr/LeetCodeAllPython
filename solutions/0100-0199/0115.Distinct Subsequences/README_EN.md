---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0115.Distinct%20Subsequences/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences)

## Description

<!-- description:start -->

<p>Given two strings s and t, return <i>the number of distinct</i> <b><i>subsequences</i></b><i> of </i>s<i> which equals </i>t.</p>

<p>The test cases are generated so that the answer fits on a 32-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;rabbbit&quot;, t = &quot;rabbit&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from s.
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babgbag&quot;, t = &quot;bag&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong>
As shown below, there are 5 ways you can generate &quot;bag&quot; from s.
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the number of schemes where the first $i$ characters of string $s$ form the first $j$ characters of string $t$. Initially, $f[i][0]=1$ for all $i \in [0,m]$.

When $i > 0$, we consider the calculation of $f[i][j]$:

- When $s[i-1] \ne t[j-1]$, we cannot select $s[i-1]$, so $f[i][j]=f[i-1][j]$;
- Otherwise, we can select $s[i-1]$, so $f[i][j]=f[i-1][j-1]$.

Therefore, we have the following state transition equation:

$$
f[i][j]=\left\{
\begin{aligned}
&f[i-1][j], &s[i-1] \ne t[j-1] \\
&f[i-1][j-1]+f[i-1][j], &s[i-1]=t[j-1]
\end{aligned}
\right.
$$

The final answer is $f[m][n]$, where $m$ and $n$ are the lengths of strings $s$ and $t$ respectively.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$.

We notice that the calculation of $f[i][j]$ is only related to $f[i-1][..]$. Therefore, we can optimize the first dimension, reducing the space complexity to $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            f[i][0] = 1
        for i, a in enumerate(s, 1):
            for j, b in enumerate(t, 1):
                f[i][j] = f[i - 1][j]
                if a == b:
                    f[i][j] += f[i - 1][j - 1]
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        f = [1] + [0] * n
        for a in s:
            for j in range(n, 0, -1):
                if a == t[j - 1]:
                    f[j] += f[j - 1]
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
