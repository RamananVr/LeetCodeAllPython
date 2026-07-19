---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1143.Longest%20Common%20Subsequence/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)

## Description

<!-- description:start -->

<p>Given two strings <code>text1</code> and <code>text2</code>, return <em>the length of their longest <strong>common subsequence</strong>. </em>If there is no <strong>common subsequence</strong>, return <code>0</code>.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code>.</li>
</ul>

<p>A <strong>common subsequence</strong> of two strings is a subsequence that is common to both strings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abcde&quot;, text2 = &quot;ace&quot; 
<strong>Output:</strong> 3  
<strong>Explanation:</strong> The longest common subsequence is &quot;ace&quot; and its length is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest common subsequence is &quot;abc&quot; and its length is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> text1 = &quot;abc&quot;, text2 = &quot;def&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no such common subsequence, so the result is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text1.length, text2.length &lt;= 1000</code></li>
	<li><code>text1</code> and <code>text2</code> consist of only lowercase English characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the length of the longest common subsequence of the first $i$ characters of $text1$ and the first $j$ characters of $text2$. Therefore, the answer is $f[m][n]$, where $m$ and $n$ are the lengths of $text1$ and $text2$, respectively.

If the $i$th character of $text1$ and the $j$th character of $text2$ are the same, then $f[i][j] = f[i - 1][j - 1] + 1$; if the $i$th character of $text1$ and the $j$th character of $text2$ are different, then $f[i][j] = max(f[i - 1][j], f[i][j - 1])$. The state transition equation is:

$$
f[i][j] =
\begin{cases}
f[i - 1][j - 1] + 1, & \textit{if } text1[i - 1] = text2[j - 1] \\
\max(f[i - 1][j], f[i][j - 1]), & \textit{if } text1[i - 1] \neq text2[j - 1]
\end{cases}
$$

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the lengths of $text1$ and $text2$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
