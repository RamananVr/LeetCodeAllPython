---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0014.Longest%20Common%20Prefix/README_EN.md
tags:
    - Trie
    - Array
    - String
---

<!-- problem:start -->

# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

## Description

<!-- description:start -->

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Character Comparison

We use the first string $strs[0]$ as a benchmark, and compare whether the $i$-th character of the subsequent strings is the same as the $i$-th character of $strs[0]$. If they are the same, we continue to compare the next character. Otherwise, we return the first $i$ characters of $strs[0]$.

If the traversal ends, it means that the first $i$ characters of all strings are the same, and we return $strs[0]$.

The time complexity is $O(n \times m)$, where $n$ and $m$ are the length of the string array and the minimum length of the strings, respectively. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if len(s) <= i or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
