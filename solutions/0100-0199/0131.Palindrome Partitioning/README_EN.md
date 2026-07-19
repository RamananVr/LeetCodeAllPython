---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0131.Palindrome%20Partitioning/README_EN.md
tags:
    - String
    - Dynamic Programming
    - Backtracking
---

<!-- problem:start -->

# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string"><strong>palindrome</strong></span>. Return <em>all possible palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + DFS (Backtracking)

We can use dynamic programming to preprocess whether any substring in the string is a palindrome, i.e., $f[i][j]$ indicates whether the substring $s[i..j]$ is a palindrome.

Next, we design a function $dfs(i)$, which represents starting from the $i$-th character of the string and partitioning it into several palindromic substrings, with the current partition scheme being $t$.

If $i = |s|$, it means the partitioning is complete, and we add $t$ to the answer array and then return.

Otherwise, we can start from $i$ and enumerate the end position $j$ from small to large. If $s[i..j]$ is a palindrome, we add $s[i..j]$ to $t$, then continue to recursively call $dfs(j+1)$. When backtracking, we need to pop $s[i..j]$.

The time complexity is $O(n \times 2^n)$, and the space complexity is $O(n^2)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i: int):
            if i == n:
                ans.append(t[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    t.append(s[i : j + 1])
                    dfs(j + 1)
                    t.pop()

        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]
        ans = []
        t = []
        dfs(0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
