---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1016.Binary%20String%20With%20Substrings%20Representing%201%20To%20N/README_EN.md
rating: 1779
source: Weekly Contest 129 Q4
tags:
    - Bit Manipulation
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [1016. Binary String With Substrings Representing 1 To N](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n)

## Description

<!-- description:start -->

<p>Given a binary string <code>s</code> and a positive integer <code>n</code>, return <code>true</code><em> if the binary representation of all the integers in the range </em><code>[1, n]</code><em> are <strong>substrings</strong> of </em><code>s</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "0110", n = 3
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "0110", n = 4
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Brain Teaser

We observe that the length of string $s$ does not exceed $1000$, so string $s$ can represent at most $1000$ binary integers. Therefore, if $n \gt 1000$, then $s$ definitely cannot represent the binary representation of all integers in the range $[1,.. n]$.

Additionally, for an integer $x$, if the binary representation of $x$ is a substring of $s$, then the binary representation of $\lfloor x / 2 \rfloor$ is also a substring of $s$. Therefore, we only need to check whether the binary representations of integers in the range $[\lfloor n / 2 \rfloor + 1,.. n]$ are substrings of $s$.

The time complexity is $O(m^2 \times \log m)$ and the space complexity is $O(\log n)$, where $m$ is the length of string $s$ and $n$ is the positive integer given in the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n > 1000:
            return False
        return all(bin(i)[2:] in s for i in range(n, n // 2, -1))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
