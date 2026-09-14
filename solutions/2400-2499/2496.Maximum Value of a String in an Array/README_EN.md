---
comments: true
difficulty: Easy
rating: 1292
source: Biweekly Contest 93 Q1
tags:
    - Array
    - String
---

<!-- problem:start -->

# [2496. Maximum Value of a String in an Array](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array)

## Description

<!-- description:start -->

<p>The <strong>value</strong> of an alphanumeric string can be defined as:</p>

<ul>
	<li>The <strong>numeric</strong> representation of the string in base <code>10</code>, if it comprises of digits <strong>only</strong>.</li>
	<li>The <strong>length</strong> of the string, otherwise.</li>
</ul>

<p>Given an array <code>strs</code> of alphanumeric strings, return <em>the <strong>maximum value</strong> of any string in </em><code>strs</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;alic3&quot;,&quot;bob&quot;,&quot;3&quot;,&quot;4&quot;,&quot;00000&quot;]
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
- &quot;alic3&quot; consists of both letters and digits, so its value is its length, i.e. 5.
- &quot;bob&quot; consists only of letters, so its value is also its length, i.e. 3.
- &quot;3&quot; consists only of digits, so its value is its numeric equivalent, i.e. 3.
- &quot;4&quot; also consists only of digits, so its value is 4.
- &quot;00000&quot; consists only of digits, so its value is 0.
Hence, the maximum value is 5, of &quot;alic3&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;1&quot;,&quot;01&quot;,&quot;001&quot;,&quot;0001&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
Each string in the array has value 1. Hence, we return 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 9</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters and digits.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A string is either its decimal value or, if it contains a letter, its length. Lengths are at most $9$. Test $\textit{isdigit}$ then take $\textit{int}$ or $\textit{len}$, and keep the maximum.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def f(s: str) -> int:
            return int(s) if all(c.isdigit() for c in s) else len(s)

        return max(f(s) for s in strs)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Method 1 parses the whole string after an all-digit check. Accumulating digit by digit returns the length on the first letter and otherwise builds the integer, without a separate scan.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def f(s: str) -> int:
            x = 0
            for c in s:
                if c.isalpha():
                    return len(s)
                x = x * 10 + ord(c) - ord("0")
            return x

        return max(f(s) for s in strs)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3

<!-- thinking:start -->

> **Thinking**
>
> Same rule as method 1 via a built-in parse: on success use the number, on failure use the length. The error path is exactly “contains a non-digit”.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
