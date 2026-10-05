---
comments: true
difficulty: Hard
rating: 2428
source: Weekly Contest 136 Q4
tags:
    - String
    - Binary Search
    - Suffix Array
    - Suffix Tree
    - Sliding Window
    - Hash Function
    - Rolling Hash
    - Boyer–Moore
    - Extended KMP
    - Suffix Automato
---

<!-- problem:start -->

# [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, consider all <em>duplicated substrings</em>: (contiguous) substrings of s that occur 2 or more times.&nbsp;The occurrences&nbsp;may overlap.</p>

<p>Return <strong>any</strong> duplicated&nbsp;substring that has the longest possible length.&nbsp;If <code>s</code> does not have a duplicated substring, the answer is <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "banana"
<strong>Output:</strong> "ana"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> ""
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Inserting every substring into a set is quadratic and fails for $n\le 3\times 10^4$. If a duplicate of length $L$ exists, shorter duplicates exist as well, so length is monotonic.
>
> Binary search the length. The check inserts every slice of length $\textit{mid}$ into a set and returns on the first collision. A hit tries a longer length; a miss shortens it.
>
> The implementation uses ordinary Python slices and a hash set, remembering the last hit as the answer.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(l: int) -> str:
            vis = set()
            for i in range(1, n - l + 2):
                j = i + l - 1
                t = h[j] - h[i - 1] * p[j - i + 1]
                if t in vis:
                    return s[i - 1 : j]
                vis.add(t)
            return ''

        base, n = 131, len(s)
        p = [0] * (n + 10)
        h = [0] * (n + 10)
        p[0] = 1
        for i, c in enumerate(s):
            p[i + 1] = p[i] * base
            h[i + 1] = h[i] * base + ord(c)
        left, right = 0, n
        ans = ''
        while left < right:
            mid = (left + right + 1) >> 1
            t = check(mid)
            if t:
                left = mid
                ans = t
            else:
                right = mid - 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
