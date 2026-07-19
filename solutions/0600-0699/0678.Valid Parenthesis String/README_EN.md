---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0678.Valid%20Parenthesis%20String/README_EN.md
tags:
    - Stack
    - Greedy
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> containing only three types of characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> and <code>&#39;*&#39;</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is <strong>valid</strong></em>.</p>

<p>The following rules define a <strong>valid</strong> string:</p>

<ul>
	<li>Any left parenthesis <code>&#39;(&#39;</code> must have a corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li>Any right parenthesis <code>&#39;)&#39;</code> must have a corresponding left parenthesis <code>&#39;(&#39;</code>.</li>
	<li>Left parenthesis <code>&#39;(&#39;</code> must go before the corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li><code>&#39;*&#39;</code> could be treated as a single right parenthesis <code>&#39;)&#39;</code> or a single left parenthesis <code>&#39;(&#39;</code> or an empty string <code>&quot;&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

Let `dp[i][j]` be true if and only if the interval `s[i], s[i+1], ..., s[j]` can be made valid. Then `dp[i][j]` is true only if:

- `s[i]` is `'*'`, and the interval `s[i+1], s[i+2], ..., s[j]` can be made valid;
- or, `s[i]` can be made to be `'('`, and there is some `k` in `[i+1, j]` such that `s[k]` can be made to be `')'`, plus the two intervals cut by `s[k]` (`s[i+1: k] and s[k+1: j+1]`) can be made valid;

- Time Complexity: $O(n^3)$, where $n$ is the length of the string. There are $O(n^2)$ states corresponding to entries of dp, and we do an average of $O(n)$ work on each state.
- Space Complexity: $O(n^2)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i, c in enumerate(s):
            dp[i][i] = c == '*'
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (
                    s[i] in '(*' and s[j] in '*)' and (i + 1 == j or dp[i + 1][j - 1])
                )
                dp[i][j] = dp[i][j] or any(
                    dp[i][k] and dp[k + 1][j] for k in range(i, j)
                )
        return dp[0][-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Greedy

Scan twice, first from left to right to make sure that each of the closing brackets is matched successfully, and second from right to left to make sure that each of the opening brackets is matched successfully.

- Time Complexity: $O(n)$, where $n$ is the length of the string.
- Space Complexity: $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        x = 0
        for c in s:
            if c in '(*':
                x += 1
            elif x:
                x -= 1
            else:
                return False
        x = 0
        for c in s[::-1]:
            if c in '*)':
                x += 1
            elif x:
                x -= 1
            else:
                return False
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
