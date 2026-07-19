---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0072.Edit%20Distance/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [72. Edit Distance](https://leetcode.com/problems/edit-distance)

## Description

<!-- description:start -->

<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the minimum number of operations to convert $word1$ of length $i$ to $word2$ of length $j$. $f[i][0] = i$, $f[0][j] = j$, $i \in [1, m], j \in [0, n]$.

We consider $f[i][j]$:

- If $word1[i - 1] = word2[j - 1]$, then we only need to consider the minimum number of operations to convert $word1$ of length $i - 1$ to $word2$ of length $j - 1$, so $f[i][j] = f[i - 1][j - 1]$;
- Otherwise, we can consider insert, delete, and replace operations, then $f[i][j] = \min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1$.

Finally, we can get the state transition equation:

$$
f[i][j] = \begin{cases}
i, & \textit{if } j = 0 \\
j, & \textit{if } i = 0 \\
f[i - 1][j - 1], & \textit{if } word1[i - 1] = word2[j - 1] \\
\min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1, & \textit{otherwise}
\end{cases}
$$

Finally, we return $f[m][n]$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. $m$ and $n$ are the lengths of $word1$ and $word2$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            f[0][j] = j
        for i, a in enumerate(word1, 1):
            f[i][0] = i
            for j, b in enumerate(word2, 1):
                if a == b:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
