---
comments: true
difficulty: Easy
tags:
    - String
    - String Matching
    - KMP
    - Extended KMP
---

<!-- problem:start -->

# [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;ab&quot; twice.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcabcabc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;abc&quot; four times or the substring &quot;abcabc&quot; twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> We ask whether $s$ is a proper prefix repeated. Trying every prefix length is $O(n^2)$.
>
> Build $s+s$ and search for $s$ starting at index $1$. A hit before $n$ means $s$ lines up inside the concatenation, hence a period exists.
>
> Starting at $1$ skips the trivial match at $0$; a hit at $n$ is only the middle copy, so there is no smaller period.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).index(s, 1) < len(s)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
