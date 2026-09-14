---
comments: true
difficulty: Medium
tags:
    - Hash Table
    - String
    - Hash Function
    - Rolling Hash
---

<!-- problem:start -->

# [1554. Strings Differ by One Character 🔒](https://leetcode.com/problems/strings-differ-by-one-character)

## Description

<!-- description:start -->

<p>Given a list of strings <code>dict</code> where all the strings are of the same length.</p>

<p>Return <code>true</code> if there are 2 strings that only differ by 1 character in the same index, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dict = [&quot;abcd&quot;,&quot;acbd&quot;, &quot;aacd&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Strings &quot;a<strong>b</strong>cd&quot; and &quot;a<strong>a</strong>cd&quot; differ only by one character in the index 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dict = [&quot;ab&quot;,&quot;cd&quot;,&quot;yz&quot;]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> dict = [&quot;abcd&quot;,&quot;cccc&quot;,&quot;abyd&quot;,&quot;abab&quot;]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of characters in <code>dict &lt;= 10<sup>5</sup></code></li>
	<li><code>dict[i].length == dict[j].length</code></li>
	<li><code>dict[i]</code> should be unique.</li>
	<li><code>dict[i]</code> contains only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Decide whether two words differ in exactly one position. The total number of characters is at most $10^5$, so pairwise scans are quadratic.
>
> Replace each index of a word by a wildcard to form a pattern that ignores that position. If the pattern is already in a set, another word differs from this one only there. A hash set makes the lookup expected constant time.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        s = set()
        for word in dict:
            for i in range(len(word)):
                t = word[:i] + "*" + word[i + 1 :]
                if t in s:
                    return True
                s.add(t)
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
