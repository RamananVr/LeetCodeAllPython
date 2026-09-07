---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0940.Distinct%20Subsequences%20II/README_EN.md
tags:
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii)

## Description

<!-- description:start -->

<p>Given a string s, return <em>the number of <strong>distinct non-empty subsequences</strong> of</em> <code>s</code>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>
A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code> while <code>&quot;aec&quot;</code> is not.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> The 7 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;ab&quot;, &quot;ac&quot;, &quot;bc&quot;, and &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> The 6 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;ab&quot;, &quot;aa&quot;, &quot;ba&quot;, and &quot;aba&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaa&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 3 distinct subsequences are &quot;a&quot;, &quot;aa&quot; and &quot;aaa&quot;.
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

We define $f[i]$ as the number of distinct subsequences ending with the $i$-th lowercase letter. Initially, all elements in $f$ are $0$.

Traverse the string $s$. For the current character $c$, update $f[c]$ to $\sum_{i=0}^{25} f[i] + 1$. Here $\sum_{i=0}^{25} f[i]$ is the number of distinct subsequences obtained so far, and $+1$ means the character $c$ itself can also be a subsequence.

Finally, the answer is $\sum_{i=0}^{25} f[i]$ modulo $10^9 + 7$.

The time complexity is $O(n \times C)$, and the space complexity is $O(C)$, where $n$ is the length of $s$ and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        f = [0] * 26
        for c in s:
            f[ord(c) - ord("a")] = (sum(f) + 1) % mod
        return sum(f) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Optimized Dynamic Programming

Based on Solution 1, we can maintain a variable $\textit{ans}$ as the sum of all elements in $f$. Each time we update $f[i]$, the number of newly added distinct subsequences is $\textit{ans} - f[i] + 1$. We then update both $\textit{ans}$ and $f[i]$ accordingly.

The time complexity is $O(n)$, and the space complexity is $O(C)$.

Similar problems:

- [1987. Number of Unique Good Subsequences](https://github.com/doocs/leetcode/blob/main/solution/1900-1999/1987.Number%20of%20Unique%20Good%20Subsequences/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        f = [0] * 26
        ans = 0
        for c in s:
            i = ord(c) - ord("a")
            add = (ans + 1 - f[i]) % mod
            ans = (ans + add) % mod
            f[i] = (f[i] + add) % mod
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
