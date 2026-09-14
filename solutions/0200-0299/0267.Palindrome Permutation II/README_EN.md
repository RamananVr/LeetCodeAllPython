---
comments: true
difficulty: Medium
tags:
    - Hash Table
    - String
    - Backtracking
---

<!-- problem:start -->

# [267. Palindrome Permutation II 🔒](https://leetcode.com/problems/palindrome-permutation-ii)

## Description

<!-- description:start -->

<p>Given a string s, return <em>all the palindromic permutations (without duplicates) of it</em>.</p>

<p>You may return the answer in <strong>any order</strong>. If <code>s</code> has no palindromic permutation, return an empty list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aabb"
<strong>Output:</strong> ["abba","baab"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> []
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> First check that at most one character has an odd count. Keep that character (if any) as the center and grow pairs outward.
>
> $dfs(t)$ picks a letter that still has two copies, wraps it around $t$, and stops when the length matches $s$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def dfs(t):
            if len(t) == len(s):
                ans.append(t)
                return
            for c, v in cnt.items():
                if v > 1:
                    cnt[c] -= 2
                    dfs(c + t + c)
                    cnt[c] += 2

        cnt = Counter(s)
        mid = ''
        for c, v in cnt.items():
            if v & 1:
                if mid:
                    return []
                mid = c
                cnt[c] -= 1
        ans = []
        dfs(mid)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
