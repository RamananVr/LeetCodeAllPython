---
comments: true
difficulty: Easy
rating: 1281
source: Weekly Contest 211 Q1
tags:
    - Hash Table
    - String
---

<!-- problem:start -->

# [1624. Largest Substring Between Two Equal Characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the length of the longest substring between two equal characters, excluding the two characters.</em> If there is no such substring return <code>-1</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The optimal substring here is an empty substring between the two <code>&#39;a&#39;s</code>.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abca&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The optimal substring here is &quot;bc&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbzxy&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no characters that appear twice in s.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> The length between two equal letters is the gap between that letter's first and a later occurrence. The string is short, but keeping only the first index of each letter already yields a linear solution.
>
> On seeing $c$ again, update the answer with $i - d[c] - 1$ and do not overwrite the first index, so the span stays maximal.
>
> A hash table (or a length-$26$ array) stores first positions; if nothing pairs, the answer stays $-1$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        ans = -1
        for i, c in enumerate(s):
            if c in d:
                ans = max(ans, i - d[c] - 1)
            else:
                d[c] = i
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
