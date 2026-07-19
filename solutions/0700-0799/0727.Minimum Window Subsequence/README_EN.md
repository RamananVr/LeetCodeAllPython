---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0727.Minimum%20Window%20Subsequence/README_EN.md
tags:
    - String
    - Dynamic Programming
    - Sliding Window
---

<!-- problem:start -->

# [727. Minimum Window Subsequence 🔒](https://leetcode.com/problems/minimum-window-subsequence)

## Description

<!-- description:start -->

<p>Given strings <code>s1</code> and <code>s2</code>, return <em>the minimum contiguous&nbsp;substring part of </em><code>s1</code><em>, so that </em><code>s2</code><em> is a subsequence of the part</em>.</p>

<p>If there is no such window in <code>s1</code> that covers all characters in <code>s2</code>, return the empty string <code>&quot;&quot;</code>. If there are multiple such minimum-length windows, return the one with the <strong>left-most starting index</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcdebdde&quot;, s2 = &quot;bde&quot;
<strong>Output:</strong> &quot;bcde&quot;
<strong>Explanation:</strong> 
&quot;bcde&quot; is the answer because it occurs before &quot;bdde&quot; which has the same length.
&quot;deb&quot; is not a smaller window because the elements of s2 in the window must occur in order.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;jmeqksfrsdcmsiwvaovztaqenprpvnbstl&quot;, s2 = &quot;u&quot;
<strong>Output:</strong> &quot;&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= s2.length &lt;= 100</code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ to represent the starting position of the shortest substring of the first $i$ characters of string $\textit{s1}$ that contains the first $j$ characters of string $\textit{s2}$. If it does not exist, it is $0$.

We can derive the state transition equation:

$$
f[i][j] = \begin{cases}
i, & j = 1 \textit{ and } s1[i-1] = s2[j] \\
f[i - 1][j - 1], & j > 1 \textit{ and } s1[i-1] = s2[j-1] \\
f[i - 1][j], & s1[i-1] \ne s2[j-1]
\end{cases}
$$

Next, we only need to traverse $\textit{s1}$. If $f[i][n] \gt 0$, update the starting position and length of the shortest substring. Finally, return the shortest substring.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the lengths of strings $\textit{s1}$ and $\textit{s2}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, a in enumerate(s1, 1):
            for j, b in enumerate(s2, 1):
                if a == b:
                    f[i][j] = i if j == 1 else f[i - 1][j - 1]
                else:
                    f[i][j] = f[i - 1][j]
        p, k = 0, m + 1
        for i, a in enumerate(s1, 1):
            if a == s2[n - 1] and f[i][n]:
                j = f[i][n] - 1
                if i - j < k:
                    k = i - j
                    p = j
        return "" if k > m else s1[p : p + k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
