---
comments: true
difficulty: Hard
rating: 2330
source: Weekly Contest 474 Q4
tags:
    - Two Pointers
    - String
    - Enumeration
---

<!-- problem:start -->

# [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target)

## Description

<!-- description:start -->

<p>You are given two strings <code>s</code> and <code>target</code>, each of length <code>n</code>, consisting of lowercase English letters.</p>

<p>Return the <strong><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> string</strong> that is <strong>both</strong> a <strong><span data-keyword="palindrome-string">palindromic</span> <span data-keyword="permutation">permutation</span></strong> of <code>s</code> and <strong>strictly</strong> greater than <code>target</code>. If no such permutation exists, return an empty string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baba&quot;, target = &quot;abba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;baab&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The palindromic permutations of <code>s</code> (in lexicographical order) are <code>&quot;abba&quot;</code> and <code>&quot;baab&quot;</code>.</li>
	<li>The lexicographically smallest permutation that is strictly greater than <code>target</code> is <code>&quot;baab&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baba&quot;, target = &quot;bbaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The palindromic permutations of <code>s</code> (in lexicographical order) are <code>&quot;abba&quot;</code> and <code>&quot;baab&quot;</code>.</li>
	<li>None of them is lexicographically strictly greater than <code>target</code>. Therefore, the answer is <code>&quot;&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;, target = &quot;abb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p><code>s</code> has no palindromic permutations. Therefore, the answer is <code>&quot;&quot;</code>.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aac&quot;, target = &quot;abb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aca&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The only palindromic permutation of <code>s</code> is <code>&quot;aca&quot;</code>.</li>
	<li><code>&quot;aca&quot;</code> is strictly greater than <code>target</code>. Therefore, the answer is <code>&quot;aca&quot;</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length == target.length &lt;= 300</code></li>
	<li><code>s</code> and <code>target</code> consist of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A palindromic permutation is determined by its left half and at most one odd center; more than one odd frequency is impossible. We want the smallest palindrome strictly larger than $\textit{target}$, so the left half is built like the next permutation: match the first half of $\textit{target}$ as far as possible, raise the first feasible position, and mirror the left half to the right.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        def build(left: str, middle: str, n: int) -> str:
            right = left[::-1]
            if n % 2:
                return left + middle + right
            return left + right

        n = len(s)
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        odd = 0
        middle = ""
        for i, v in enumerate(freq):
            if v % 2:
                odd += 1
                middle = chr(97 + i)
        if odd > 1:
            return ""

        half = [v // 2 for v in freq]
        half_len = n // 2
        target_half = target[:half_len]
        remaining = half[:]
        prefix = []
        matched = 0
        for i in range(half_len):
            x = ord(target_half[i]) - 97
            if remaining[x] == 0:
                break
            prefix.append(target_half[i])
            remaining[x] -= 1
            matched += 1

        if matched == half_len:
            cand = build("".join(prefix), middle, n)
            if cand > target:
                return cand

        last = half_len - 1 if matched == half_len else matched
        for pos in range(last, -1, -1):
            rem = half[:]
            valid = True
            for i in range(pos):
                x = ord(target_half[i]) - 97
                if rem[x] == 0:
                    valid = False
                    break
                rem[x] -= 1
            if not valid:
                continue
            target_char = ord(target_half[pos]) - 97
            for c in range(target_char + 1, 26):
                if rem[c] == 0:
                    continue
                left = target_half[:pos] + chr(97 + c)
                rem[c] -= 1
                for x in range(26):
                    left += chr(97 + x) * rem[x]
                    rem[x] = 0
                cand = build(left, middle, n)
                if cand > target:
                    return cand
                rem = half[:]
                for i in range(pos):
                    rem[ord(target_half[i]) - 97] -= 1
        return ""
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
