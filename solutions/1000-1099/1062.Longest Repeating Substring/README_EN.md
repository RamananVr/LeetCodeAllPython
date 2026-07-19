---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1062.Longest%20Repeating%20Substring/README_EN.md
tags:
    - String
    - Binary Search
    - Dynamic Programming
    - Suffix Array
    - Hash Function
    - Rolling Hash
---

<!-- problem:start -->

# [1062. Longest Repeating Substring 🔒](https://leetcode.com/problems/longest-repeating-substring)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the length of the longest repeating substrings</em>. If no repeating substring exists, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;
<strong>Output:</strong> 0
<strong>Explanation: </strong>There is no repeating substring.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbaba&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>The longest repeating substrings are &quot;ab&quot; and &quot;ba&quot;, each of which occurs twice.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabcaabdaab&quot;
<strong>Output:</strong> 3
<strong>Explanation: </strong>The longest repeating substring is &quot;aab&quot;, which occurs <code>3</code> times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ to represent the length of the longest repeating substring ending with $s[i]$ and $s[j]$. Initially, $f[i][j]=0$.

We enumerate $i$ in the range $[1, n)$ and enumerate $j$ in the range $[0, i)$. If $s[i]=s[j]$, then we have:

$$
f[i][j]=
\begin{cases}
f[i-1][j-1]+1, & j>0 \\
1, & j=0
\end{cases}
$$

The answer is the maximum value of all $f[i][j]$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Where $n$ is the length of the string $s$.

Similar problems:

- [1044. Longest Duplicate Substring 🔒](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1044.Longest%20Duplicate%20Substring/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j]:
                    f[i][j] = 1 + (f[i - 1][j - 1] if j else 0)
                    ans = max(ans, f[i][j])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
