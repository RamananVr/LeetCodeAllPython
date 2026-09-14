---
comments: true
difficulty: Easy
rating: 1223
source: Weekly Contest 184 Q1
tags:
    - Array
    - String
    - String Matching
---

<!-- problem:start -->

# [1408. String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array)

## Description

<!-- description:start -->

<p>Given an array of string <code>words</code>, return all strings in<em> </em><code>words</code><em> </em>that are a <span data-keyword="substring-nonempty">substring</span> of another word. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;mass&quot;,&quot;as&quot;,&quot;hero&quot;,&quot;superhero&quot;]
<strong>Output:</strong> [&quot;as&quot;,&quot;hero&quot;]
<strong>Explanation:</strong> &quot;as&quot; is substring of &quot;mass&quot; and &quot;hero&quot; is substring of &quot;superhero&quot;.
[&quot;hero&quot;,&quot;as&quot;] is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;leetcode&quot;,&quot;et&quot;,&quot;code&quot;]
<strong>Output:</strong> [&quot;et&quot;,&quot;code&quot;]
<strong>Explanation:</strong> &quot;et&quot;, &quot;code&quot; are substring of &quot;leetcode&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;blue&quot;,&quot;green&quot;,&quot;bu&quot;]
<strong>Output:</strong> []
<strong>Explanation:</strong> No string of words is substring of another string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> contains only lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Brute Force Enumeration

<!-- thinking:start -->

> **Thinking**
>
> $n\le 100$ and each word has length at most $30$, so testing whether each word occurs in another is about $O(n^2\cdot L^2)$ and fits the limits.
>
> Words are unique, so a double loop with a substring test is enough; a trie or KMP is unnecessary.

<!-- thinking:end -->

We directly enumerate all strings $words[i]$, and check whether it is a substring of other strings. If it is, we add it to the answer.

The time complexity is $O(n^3)$, and the space complexity is $O(n)$. Where $n$ is the length of the string array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, s in enumerate(words):
            if any(i != j and s in t for j, t in enumerate(words)):
                ans.append(s)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
