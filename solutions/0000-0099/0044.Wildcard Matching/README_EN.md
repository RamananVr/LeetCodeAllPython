---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0044.Wildcard%20Matching/README_EN.md
tags:
    - Greedy
    - Recursion
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching)

## Description

<!-- description:start -->

<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement wildcard pattern matching with support for <code>&#39;?&#39;</code> and <code>&#39;*&#39;</code> where:</p>

<ul>
	<li><code>&#39;?&#39;</code> Matches any single character.</li>
	<li><code>&#39;*&#39;</code> Matches any sequence of characters (including the empty sequence).</li>
</ul>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; matches any sequence.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cb&quot;, p = &quot;?a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;&#39;?&#39; matches &#39;c&#39;, but the second letter is &#39;a&#39;, which does not match &#39;b&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length, p.length &lt;= 2000</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>&#39;?&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We design a function $dfs(i, j)$, which represents whether the string $s$ starting from the $i$-th character matches the string $p$ starting from the $j$-th character. The answer is $dfs(0, 0)$.

The execution process of the function $dfs(i, j)$ is as follows:

- If $i \geq \textit{len}(s)$, then $dfs(i, j)$ is true only when $j \geq \textit{len}(p)$ or $p[j] = '*'$ and $dfs(i, j + 1)$ is true.
- If $j \geq \textit{len}(p)$, then $dfs(i, j)$ is false.
- If $p[j] = '*'$, then $dfs(i, j)$ is true if and only if $dfs(i + 1, j)$ or $dfs(i + 1, j + 1)$ or $dfs(i, j + 1)$ is true.
- Otherwise, $dfs(i, j)$ is true if and only if $p[j] = '?'$ or $s[i] = p[j]$ and $dfs(i + 1, j + 1)$ is true.

To avoid repeated calculations, we use the method of memoization search and store the result of $dfs(i, j)$ in a hash table.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the lengths of the strings $s$ and $p$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if i >= len(s):
                return j >= len(p) or (p[j] == "*" and dfs(i, j + 1))
            if j >= len(p):
                return False
            if p[j] == "*":
                return dfs(i + 1, j) or dfs(i + 1, j + 1) or dfs(i, j + 1)
            return (p[j] == "?" or s[i] == p[j]) and dfs(i + 1, j + 1)

        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We can convert the memoization search in Solution 1 into dynamic programming.

Define $f[i][j]$ to represent whether the first $i$ characters of string $s$ match the first $j$ characters of string $p$. Initially, $f[0][0] = \textit{true}$, indicating that two empty strings are matching. For $j \in [1, n]$, if $p[j-1] = '*'$, then $f[0][j] = f[0][j-1]$.

Next, we consider the case of $i \in [1, m]$ and $j \in [1, n]$:

- If $p[j-1] = '*'$, then $f[i][j] = f[i-1][j] \lor f[i][j-1] \lor f[i-1][j-1]$.
- Otherwise, $f[i][j] = (p[j-1] = '?' \lor s[i-1] = p[j-1]) \land f[i-1][j-1]$.

The final answer is $f[m][n]$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the lengths of the strings $s$ and $p$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                f[0][j] = f[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    f[i][j] = f[i - 1][j] or f[i][j - 1] or f[i - 1][j - 1]
                else:
                    f[i][j] = f[i - 1][j - 1] and (
                        p[j - 1] == "?" or s[i - 1] == p[j - 1]
                    )
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
