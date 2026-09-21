---
comments: true
difficulty: Easy
tags:
    - Two Pointers
    - String
    - String Matching
    - KMP
    - Boyer–Moore
    - Extended KMP
---

<!-- problem:start -->

# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)

## Description

<!-- description:start -->

<p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;sad&quot; occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Traversal

<!-- thinking:start -->

> **Thinking**
>
> The first idea is to try every start $i$ in $haystack$ and test whether the length-$m$ slice equals $needle$. With $n,m \le 10^4$, the worst case $O((n-m)m)$ is about $10^8$ and usually passes.
>
> The bottleneck is paying $m$ character comparisons at many near-matches. Smarter matchers amortize toward linear time, but this size does not force them yet.
>
> We only need the first hit; a mismatch just moves on to the next $i$.
>
> So scan $i$ from $0$ to $n-m$, return $i$ on equality, else $-1$. Extra space is $O(1)$.

<!-- thinking:end -->

We compare the string `needle` with each character of the string `haystack` as the starting point. If we find a matching index, we return it directly.

Assuming the length of the string `haystack` is $n$ and the length of the string `needle` is $m$, the time complexity is $O((n-m) \times m)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Rabin-Karp String Matching Algorithm

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 may compare all $m$ characters at every start, approaching $O(nm)$. We want the next window to reuse work from the last one.
>
> A fixed-length substring can be rolling-hashed: add the incoming character, drop the outgoing one, update in $O(1)$. When the window hash equals $needle$'s hash, compare the raw strings to rule out a collision.
>
> One scan of $haystack$ then costs expected $O(n+m)$.

<!-- thinking:end -->

The [Rabin-Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) essentially uses a sliding window combined with a hash function to compare the hashes of fixed-length strings, which can reduce the time complexity of comparing whether two strings are the same to $O(1)$.

Assuming the length of the string `haystack` is $n$ and the length of the string `needle` is $m$, the time complexity is $O(n+m)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        mod = (1 << 31) - 1
        target = sha = 0
        multi = 1
        for i in range(m):
            target = (target * 256 + ord(needle[i])) % mod
        for _ in range(1, m):
            multi = multi * 256 % mod
        left = 0
        for right in range(n):
            sha = (sha * 256 + ord(haystack[right])) % mod
            if right - left + 1 < m:
                continue
            if sha == target and haystack[left : right + 1] == needle:
                return left
            sha = (sha - ord(haystack[left]) * multi % mod + mod) % mod
            left += 1
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: KMP

<!-- thinking:start -->

> **Thinking**
>
> Solution 2 makes a window comparison expected $O(1)$, but it still hashes modulo a prime and must verify the raw strings on a collision. We want a worst-case linear scan without hashing.
>
> After a mismatch we need not rewind $\textit{haystack}$ to the start of the window. The prefix function of $\textit{needle}$ stores the longest proper border of the matched prefix, so we know where in the pattern to resume.
>
> Build $\textit{next}$ for $\textit{needle}$, then scan $\textit{haystack}$ once, falling back only along $\textit{next}$. Time $O(n+m)$ and extra space $O(m)$.

<!-- thinking:end -->

Compute the prefix function $\textit{next}$ of $\textit{needle}$, where $\textit{next}[i]$ is the longest proper border of $\textit{needle}[0..i]$. Scan $\textit{haystack}$: equal characters grow the match length, and a mismatch jumps it to $\textit{next}[j-1]$. When the match length reaches $m$, return the start index $i-m+1$.

The time complexity is $O(n+m)$ and the space complexity is $O(m)$, where $n$ and $m$ are the lengths of $\textit{haystack}$ and $\textit{needle}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        nxt = [0] * m
        j = 0
        for i in range(1, m):
            while j and needle[i] != needle[j]:
                j = nxt[j - 1]
            if needle[i] == needle[j]:
                j += 1
            nxt[i] = j
        j = 0
        for i, ch in enumerate(haystack):
            while j and ch != needle[j]:
                j = nxt[j - 1]
            if ch == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
