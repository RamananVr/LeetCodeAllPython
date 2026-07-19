---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0132.Palindrome%20Partitioning%20II/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string">palindrome</span>.</p>

<p>Return <em>the <strong>minimum</strong> cuts needed for a palindrome partitioning of</em> <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The palindrome partitioning [&quot;aa&quot;,&quot;b&quot;] could be produced using 1 cut.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase English letters only.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

First, we preprocess the string $s$ to determine whether each substring $s[i..j]$ is a palindrome, and record this in a 2D array $g[i][j]$, where $g[i][j]$ indicates whether the substring $s[i..j]$ is a palindrome.

Next, we define $f[i]$ to represent the minimum number of cuts needed for the substring $s[0..i-1]$. Initially, $f[i] = i$.

Next, we consider how to transition the state for $f[i]$. We can enumerate the previous cut point $j$. If the substring $s[j..i]$ is a palindrome, then $f[i]$ can be transitioned from $f[j]$. If $j = 0$, it means that $s[0..i]$ itself is a palindrome, and no cuts are needed, i.e., $f[i] = 0$. Therefore, the state transition equation is as follows:

$$
f[i] = \min_{0 \leq j \leq i} \begin{cases} f[j-1] + 1, & \textit{if}\ g[j][i] = \textit{True} \\ 0, & \textit{if}\ g[0][i] = \textit{True} \end{cases}
$$

The answer is $f[n]$, where $n$ is the length of the string $s$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Here, $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = s[i] == s[j] and g[i + 1][j - 1]
        f = list(range(n))
        for i in range(1, n):
            for j in range(i + 1):
                if g[j][i]:
                    f[i] = min(f[i], 1 + f[j - 1] if j else 0)
        return f[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
