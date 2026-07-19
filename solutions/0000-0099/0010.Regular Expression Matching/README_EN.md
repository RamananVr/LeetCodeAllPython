---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0010.Regular%20Expression%20Matching/README_EN.md
tags:
    - Recursion
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)

## Description

<!-- description:start -->

<p>Given an input string <code>s</code>&nbsp;and a pattern <code>p</code>, implement regular expression matching with support for <code>&#39;.&#39;</code> and <code>&#39;*&#39;</code> where:</p>

<ul>
	<li><code>&#39;.&#39;</code> Matches any single character.​​​​</li>
	<li><code>&#39;*&#39;</code> Matches zero or more of the preceding element.</li>
</ul>

<p>Return a boolean indicating whether the matching covers the entire input string (not partial).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, p = &quot;a*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &#39;*&#39; means zero or more of the preceding element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;, p = &quot;.*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 20</code></li>
	<li><code>1 &lt;= p.length&nbsp;&lt;= 20</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters, <code>&#39;.&#39;</code>, and&nbsp;<code>&#39;*&#39;</code>.</li>
	<li>It is guaranteed for each appearance of the character <code>&#39;*&#39;</code>, there will be a previous valid character to match.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We design a function $dfs(i, j)$, which indicates whether the $i$-th character of $s$ matches the $j$-th character of $p$. The answer is $dfs(0, 0)$.

The calculation process of the function $dfs(i, j)$ is as follows:

- If $j$ has reached the end of $p$, then if $i$ has also reached the end of $s$, the match is successful, otherwise, the match fails.
- If the next character of $j$ is `'*'`, we can choose to match $0$ $s[i]$ characters, which is $dfs(i, j + 2)$. If $i \lt m$ and $s[i]$ matches $p[j]$, we can choose to match $1$ $s[i]$ character, which is $dfs(i + 1, j)$.
- If the next character of $j$ is not `'*'`, then if $i \lt m$ and $s[i]$ matches $p[j]$, it is $dfs(i + 1, j + 1)$. Otherwise, the match fails.

During the process, we can use memoization search to avoid repeated calculations.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the lengths of $s$ and $p$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j >= n:
                return i == m
            if j + 1 < n and p[j + 1] == '*':
                return dfs(i, j + 2) or (
                    i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j)
                )
            return i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j + 1)

        m, n = len(s), len(p)
        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We can convert the memoization search in Solution 1 into dynamic programming.

Define $f[i][j]$ to represent whether the first $i$ characters of string $s$ match the first $j$ characters of string $p$. The answer is $f[m][n]$. Initialize $f[0][0] = true$, indicating that the empty string and the empty regular expression match.

Similar to Solution 1, we can discuss different cases.

- If $p[j - 1]$ is `'*'`, we can choose to match $0$ $s[i - 1]$ characters, which is $f[i][j] = f[i][j - 2]$. If $s[i - 1]$ matches $p[j - 2]$, we can choose to match $1$ $s[i - 1]$ character, which is $f[i][j] = f[i][j] \lor f[i - 1][j]$.
- If $p[j - 1]$ is not `'*'`, then if $s[i - 1]$ matches $p[j - 1]$, it is $f[i][j] = f[i - 1][j - 1]$. Otherwise, the match fails.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the lengths of $s$ and $p$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    f[i][j] = f[i][j - 2]
                    if i > 0 and (p[j - 2] == "." or s[i - 1] == p[j - 2]):
                        f[i][j] |= f[i - 1][j]
                elif i > 0 and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                    f[i][j] = f[i - 1][j - 1]
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
