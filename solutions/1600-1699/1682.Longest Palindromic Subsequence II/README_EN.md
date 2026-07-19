---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1682.Longest%20Palindromic%20Subsequence%20II/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [1682. Longest Palindromic Subsequence II 🔒](https://leetcode.com/problems/longest-palindromic-subsequence-ii)

## Description

<!-- description:start -->

<p>A subsequence of a string <code>s</code> is considered a <strong>good palindromic subsequence</strong> if:</p>

<ul>
	<li>It is a subsequence of <code>s</code>.</li>
	<li>It is a palindrome (has the same value if reversed).</li>
	<li>It has an <strong>even</strong> length.</li>
	<li>No two consecutive characters are equal, except the two middle ones.</li>
</ul>

<p>For example, if <code>s = &quot;abcabcabb&quot;</code>, then <code>&quot;abba&quot;</code> is considered a <strong>good palindromic subsequence</strong>, while <code>&quot;bcb&quot;</code> (not even length) and <code>&quot;bbbb&quot;</code> (has equal consecutive characters) are not.</p>

<p>Given a string <code>s</code>, return <em>the <strong>length</strong> of the <strong>longest good palindromic subsequence</strong> in </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbabab&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest good palindromic subsequence of s is &quot;baab&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;dcbccacdb&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest good palindromic subsequence of s is &quot;dccd&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 250</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memorization Search

We design a function $dfs(i, j, x)$ to represent the length of the longest "good" palindrome subsequence ending with character $x$ in the index range $[i, j]$ of string $s$. The answer is $dfs(0, n - 1, 26)$.

The calculation process of the function $dfs(i, j, x)$ is as follows:

- If $i >= j$, then $dfs(i, j, x) = 0$;
- If $s[i] = s[j]$ and $s[i] \neq x$, then $dfs(i, j, x) = dfs(i + 1, j - 1, s[i]) + 2$;
- If $s[i] \neq s[j]$, then $dfs(i, j, x) = max(dfs(i + 1, j, x), dfs(i, j - 1, x))$.

During the process, we can use memorization search to avoid repeated calculations.

The time complexity is $O(n^2 \times C)$. Where $n$ is the length of the string $s$, and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i, j, x):
            if i >= j:
                return 0
            if s[i] == s[j] and s[i] != x:
                return dfs(i + 1, j - 1, s[i]) + 2
            return max(dfs(i + 1, j, x), dfs(i, j - 1, x))

        ans = dfs(0, len(s) - 1, '')
        dfs.cache_clear()
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
