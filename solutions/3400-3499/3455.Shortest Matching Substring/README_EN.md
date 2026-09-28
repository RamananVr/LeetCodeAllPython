---
comments: true
difficulty: Hard
rating: 2303
source: Biweekly Contest 150 Q4
tags:
    - Two Pointers
    - String
    - Binary Search
    - String Matching
---

<!-- problem:start -->

# [3455. Shortest Matching Substring](https://leetcode.com/problems/shortest-matching-substring)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> and a pattern string <code>p</code>, where <code>p</code> contains <strong>exactly two</strong> <code>&#39;*&#39;</code> characters.</p>

<p>The <code>&#39;*&#39;</code> in <code>p</code> matches any sequence of zero or more characters.</p>

<p>Return the length of the <strong>shortest</strong> <span data-keyword="substring">substring</span> in <code>s</code> that matches <code>p</code>. If there is no such substring, return -1.</p>
<strong>Note:</strong> The empty substring is considered valid.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abaacbaecebce&quot;, p = &quot;ba*c*ce&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The shortest matching substring of <code>p</code> in <code>s</code> is <code>&quot;<u><strong>ba</strong></u>e<u><strong>c</strong></u>eb<u><strong>ce</strong></u>&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baccbaadbc&quot;, p = &quot;cc*baa*adb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no matching substring in <code>s</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;a&quot;, p = &quot;**&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The empty substring is the shortest matching substring.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;madlogic&quot;, p = &quot;*adlogi*&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The shortest matching substring of <code>p</code> in <code>s</code> is <code>&quot;<strong><u>adlogi</u></strong>&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= p.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
	<li><code>p</code> contains only lowercase English letters and exactly two <code>&#39;*&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> $p$ contains exactly two stars and splits into three literals $a$, $b$, $c$. $|s|,|p|\le 10^5$ forbids a naive search from every start.
>
> The shortest match is determined by occurrence positions: after one $a$, take the earliest later $b$, then the earliest later $c$.
>
> KMP or Z-algorithm lists every occurrence of the three pieces. A two-pointer sweep over $a$'s starts advances $b$ and $c$. The length is the right end of $c$ minus the left end of $a$, or $-1$ if none exists.

<!-- thinking:end -->

Split the pattern on its two stars into literals $a$, $b$, and $c$. Any of them may be empty. KMP lists every starting index of each literal in $s$. An empty literal matches at every index $0,1,\ldots,n$.

For each start $i$ of $a$, advance a pointer to the earliest start $j$ of $b$ with $j\ge i+|a|$, then to the earliest start $k$ of $c$ with $k\ge j+|b|$. That match has length $k+|c|-i$. The minimum over all starts is the answer, or $-1$ when no match exists.

A later $b$ can only push $c$ further right, so the earliest $b$ and the earliest $c$ are optimal for a fixed $i$.

The time complexity is $O(n+m)$ and the space complexity is $O(n)$, where $n$ and $m$ are the lengths of $s$ and $p$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        def starts(pat: str):
            if not pat:
                return list(range(len(s) + 1))
            m = len(pat)
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    i += 1
            res = []
            i = j = 0
            n = len(s)
            while i < n:
                if s[i] == pat[j]:
                    i += 1
                    j += 1
                    if j == m:
                        res.append(i - m)
                        j = lps[j - 1]
                elif j:
                    j = lps[j - 1]
                else:
                    i += 1
            return res

        a, b, c = p.split('*')
        A, B, C = starts(a), starts(b), starts(c)
        la, lb, lc = len(a), len(b), len(c)
        ans = len(s) + 1
        j = k = 0
        for i in A:
            while j < len(B) and B[j] < i + la:
                j += 1
            if j == len(B):
                break
            while k < len(C) and C[k] < B[j] + lb:
                k += 1
            if k == len(C):
                break
            ans = min(ans, C[k] + lc - i)
        return -1 if ans > len(s) else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
