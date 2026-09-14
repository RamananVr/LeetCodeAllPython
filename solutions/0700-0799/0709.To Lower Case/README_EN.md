---
comments: true
difficulty: Easy
tags:
    - String
---

<!-- problem:start -->

# [709. To Lower Case](https://leetcode.com/problems/to-lower-case)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the string after replacing every uppercase letter with the same lowercase letter</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Hello&quot;
<strong>Output:</strong> &quot;hello&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;here&quot;
<strong>Output:</strong> &quot;here&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;LOVELY&quot;
<strong>Output:</strong> &quot;lovely&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of printable ASCII characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Convert uppercase letters to lowercase; $n \le 100$. A library call works, and so does an ASCII walk.
>
> Each uppercase letter is $32$ below its lowercase counterpart, i.e. bit $5$ of the code point. Bitwise-or with $32$ lowercases it; other characters stay unchanged.
>
> Map every character: if it is uppercase, emit $\operatorname{ord}(c)\,|\,32$. Time $O(n)$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(ord(c) | 32) if c.isupper() else c for c in s])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 branches on `isupper`. Lowercase ASCII already has bit $5$ set, so or-ing $32$ is a no-op there and we can apply it uniformly.
>
> The TypeScript tab ors every character; the Rust tab still guards $A$–$Z$ so non-letters are untouched. Neither version calls a locale-aware lowercasing API.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
