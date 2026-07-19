---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0097.Interleaving%20String/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [97. Interleaving String](https://leetcode.com/problems/interleaving-string)

## Description

<!-- description:start -->

<p>Given strings <code>s1</code>, <code>s2</code>, and <code>s3</code>, find whether <code>s3</code> is formed by an <strong>interleaving</strong> of <code>s1</code> and <code>s2</code>.</p>

<p>An <strong>interleaving</strong> of two strings <code>s</code> and <code>t</code> is a configuration where <code>s</code> and <code>t</code> are divided into <code>n</code> and <code>m</code> <span data-keyword="substring-nonempty">substrings</span> respectively, such that:</p>

<ul>
	<li><code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code></li>
	<li><code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code></li>
	<li><code>|n - m| &lt;= 1</code></li>
	<li>The <strong>interleaving</strong> is <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> or <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code></li>
</ul>

<p><strong>Note:</strong> <code>a + b</code> is the concatenation of strings <code>a</code> and <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0097.Interleaving%20String/images/interleave.jpg" style="width: 561px; height: 203px;" />
<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, s3 = &quot;aadbbcbcac&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> One way to obtain s3 is:
Split s1 into s1 = &quot;aa&quot; + &quot;bc&quot; + &quot;c&quot;, and s2 into s2 = &quot;dbbc&quot; + &quot;a&quot;.
Interleaving the two splits, we get &quot;aa&quot; + &quot;dbbc&quot; + &quot;bc&quot; + &quot;a&quot; + &quot;c&quot; = &quot;aadbbcbcac&quot;.
Since s3 can be obtained by interleaving s1 and s2, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, s3 = &quot;aadbbbaccc&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> Notice how it is impossible to interleave s2 with any other string to obtain s3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;&quot;, s2 = &quot;&quot;, s3 = &quot;&quot;
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>0 &lt;= s3.length &lt;= 200</code></li>
	<li><code>s1</code>, <code>s2</code>, and <code>s3</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it using only <code>O(s2.length)</code> additional memory space?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

Let's denote the length of string $s_1$ as $m$ and the length of string $s_2$ as $n$. If $m + n \neq |s_3|$, then $s_3$ is definitely not an interleaving string of $s_1$ and $s_2$, so we return `false`.

Next, we design a function $dfs(i, j)$, which represents whether the remaining part of $s_3$ can be interleaved from the $i$th character of $s_1$ and the $j$th character of $s_2$. The answer is $dfs(0, 0)$.

The calculation process of function $dfs(i, j)$ is as follows:

If $i \geq m$ and $j \geq n$, it means that both $s_1$ and $s_2$ have been traversed, so we return `true`.

If $i < m$ and $s_1[i] = s_3[i + j]$, it means that the character $s_1[i]$ is part of $s_3[i + j]$. Therefore, we recursively call $dfs(i + 1, j)$ to check whether the next character of $s_1$ can match the current character of $s_2$. If it can match, we return `true`.

Similarly, if $j < n$ and $s_2[j] = s_3[i + j]$, it means that the character $s_2[j]$ is part of $s_3[i + j]$. Therefore, we recursively call $dfs(i, j + 1)$ to check whether the next character of $s_2$ can match the current character of $s_1$. If it can match, we return `true`.

Otherwise, we return `false`.

To avoid repeated calculations, we can use memoization search.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the lengths of strings $s_1$ and $s_2$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True
            k = i + j
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1):
                return True
            return False

        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We can convert the memoization search in Solution 1 into dynamic programming.

We define $f[i][j]$ to represent whether the first $i$ characters of string $s_1$ and the first $j$ characters of string $s_2$ can interleave to form the first $i + j$ characters of string $s_3$. When transitioning states, we can consider whether the current character is obtained from the last character of $s_1$ or the last character of $s_2$. Therefore, we have the state transition equation:

$$
f[i][j] = \begin{cases}
f[i - 1][j] & \textit{if } s_1[i - 1] = s_3[i + j - 1] \\
\textit{or } f[i][j - 1] & \textit{if } s_2[j - 1] = s_3[i + j - 1] \\
\textit{false} & \textit{otherwise}
\end{cases}
$$

where $f[0][0] = \textit{true}$ indicates that an empty string is an interleaving string of two empty strings.

The answer is $f[m][n]$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the lengths of strings $s_1$ and $s_2$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                k = i + j - 1
                if i and s1[i - 1] == s3[k]:
                    f[i][j] = f[i - 1][j]
                if j and s2[j - 1] == s3[k]:
                    f[i][j] |= f[i][j - 1]
        return f[m][n]
```

<!-- tabs:end -->

We notice that the state $f[i][j]$ is only related to the states $f[i - 1][j]$, $f[i][j - 1]$, and $f[i - 1][j - 1]$. Therefore, we can use a rolling array to optimize the space complexity, reducing the original space complexity from $O(m \times n)$ to $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        f = [True] + [False] * n
        for i in range(m + 1):
            for j in range(n + 1):
                k = i + j - 1
                if i:
                    f[j] &= s1[i - 1] == s3[k]
                if j:
                    f[j] |= f[j - 1] and s2[j - 1] == s3[k]
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
