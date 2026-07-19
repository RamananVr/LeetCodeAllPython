---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1771.Maximize%20Palindrome%20Length%20From%20Subsequences/README_EN.md
rating: 2182
source: Weekly Contest 229 Q4
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [1771. Maximize Palindrome Length From Subsequences](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences)

## Description

<!-- description:start -->

<p>You are given two strings, <code>word1</code> and <code>word2</code>. You want to construct a string in the following manner:</p>

<ul>
	<li>Choose some <strong>non-empty</strong> subsequence <code>subsequence1</code> from <code>word1</code>.</li>
	<li>Choose some <strong>non-empty</strong> subsequence <code>subsequence2</code> from <code>word2</code>.</li>
	<li>Concatenate the subsequences: <code>subsequence1 + subsequence2</code>, to make the string.</li>
</ul>

<p>Return <em>the <strong>length</strong> of the longest <strong>palindrome</strong> that can be constructed in the described manner. </em>If no palindromes can be constructed, return <code>0</code>.</p>

<p>A <strong>subsequence</strong> of a string <code>s</code> is a string that can be made by deleting some (possibly none) characters from <code>s</code> without changing the order of the remaining characters.</p>

<p>A <strong>palindrome</strong> is a string that reads the same forward&nbsp;as well as backward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;cacb&quot;, word2 = &quot;cbba&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> Choose &quot;ab&quot; from word1 and &quot;cba&quot; from word2 to make &quot;abcba&quot;, which is a palindrome.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;ab&quot;, word2 = &quot;ab&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Choose &quot;ab&quot; from word1 and &quot;a&quot; from word2 to make &quot;aba&quot;, which is a palindrome.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;aa&quot;, word2 = &quot;bb&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> You cannot construct a palindrome from the described method, so return 0.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 1000</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

First, we concatenate strings `word1` and `word2` to get string $s$. Then we can transform the problem into finding the length of the longest palindromic subsequence in string $s$. However, when calculating the final answer, we need to ensure that at least one character in the palindrome string comes from `word1` and another character comes from `word2`.

We define $f[i][j]$ as the length of the longest palindromic subsequence in the substring of string $s$ with index range $[i, j]$.

If $s[i] = s[j]$, then $s[i]$ and $s[j]$ must be in the longest palindromic subsequence, at this time $f[i][j] = f[i + 1][j - 1] + 2$. At this point, we also need to judge whether $s[i]$ and $s[j]$ come from `word1` and `word2`. If so, we update the maximum value of the answer to $ans=\max(ans, f[i][j])$.

If $s[i] \neq s[j]$, then $s[i]$ and $s[j]$ will definitely not appear in the longest palindromic subsequence at the same time, at this time $f[i][j] = max(f[i + 1][j], f[i][j - 1])$.

Finally, we return the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Here, $n$ is the length of string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1
        ans = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                    if i < len(word1) <= j:
                        ans = max(ans, f[i][j])
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
