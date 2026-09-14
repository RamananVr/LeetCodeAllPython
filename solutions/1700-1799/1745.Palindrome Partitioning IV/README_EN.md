---
comments: true
difficulty: Hard
rating: 1924
source: Weekly Contest 226 Q4
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [1745. Palindrome Partitioning IV](https://leetcode.com/problems/palindrome-partitioning-iv)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <code>true</code> <em>if it is possible to split the string</em> <code>s</code> <em>into three <strong>non-empty</strong> palindromic substrings. Otherwise, return </em><code>false</code>.​​​​​</p>

<p>A string is said to be palindrome if it the same string when reversed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcbdd&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>&quot;abcbdd&quot; = &quot;a&quot; + &quot;bcb&quot; + &quot;dd&quot;, and all three substrings are palindromes.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bcbddxy&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>s cannot be split into 3 palindromes.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code>​​​​​​ consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Split the string into three palindromes. Checking each candidate split from scratch is $O(n^3)$ palindrome tests. $n$ can be a few hundred, so precompute palindromes.
>
> $f[i][j]$ is whether $s[i..j]$ is a palindrome. After filling it by interval length, try two cuts; the total is $O(n^2)$.

<!-- thinking:end -->

We define $f[i][j]$ to indicate whether the substring of $s$ from the $i$-th character to the $j$-th character is a palindrome, initially $f[i][j] = \textit{true}$.

Then we can calculate $f[i][j]$ using the following state transition equation:

$$
f[i][j] = \begin{cases}
\textit{true}, & \text{if } s[i] = s[j] \text{ and } (i + 1 = j \text{ or } f[i + 1][j - 1]) \\
\textit{false}, & \text{otherwise}
\end{cases}
$$

Since $f[i][j]$ depends on $f[i + 1][j - 1]$, we need to enumerate $i$ from large to small and $j$ from small to large, so that when calculating $f[i][j]$, $f[i + 1][j - 1]$ has already been calculated.

Next, we enumerate the right endpoint $i$ of the first substring and the right endpoint $j$ of the second substring. The left endpoint of the third substring can be enumerated in the range $[j + 1, n - 1]$, where $n$ is the length of the string $s$. If the first substring $s[0..i]$, the second substring $s[i+1..j]$, and the third substring $s[j+1..n-1]$ are all palindromes, then we have found a feasible partitioning scheme and return $\textit{true}$.

After enumerating all partitioning schemes, if no valid partitioning scheme is found, return $\textit{false}$.

Time complexity is $O(n^2)$, and space complexity is $O(n^2)$. Where $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = s[i] == s[j] and (i + 1 == j or f[i + 1][j - 1])
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if f[0][i] and f[i + 1][j] and f[j + 1][-1]:
                    return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
