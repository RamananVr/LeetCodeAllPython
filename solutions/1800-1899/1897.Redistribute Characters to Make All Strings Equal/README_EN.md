---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1897.Redistribute%20Characters%20to%20Make%20All%20Strings%20Equal/README_EN.md
rating: 1309
source: Weekly Contest 245 Q1
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [1897. Redistribute Characters to Make All Strings Equal](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal)

## Description

<!-- description:start -->

<p>You are given an array of strings <code>words</code> (<strong>0-indexed</strong>).</p>

<p>In one operation, pick two <strong>distinct</strong> indices <code>i</code> and <code>j</code>, where <code>words[i]</code> is a non-empty string, and move <strong>any</strong> character from <code>words[i]</code> to <strong>any</strong> position in <code>words[j]</code>.</p>

<p>Return <code>true</code> <em>if you can make<strong> every</strong> string in </em><code>words</code><em> <strong>equal </strong>using <strong>any</strong> number of operations</em>,<em> and </em><code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abc&quot;,&quot;aabc&quot;,&quot;bc&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Move the first &#39;a&#39; in <code>words[1] to the front of words[2],
to make </code><code>words[1]</code> = &quot;abc&quot; and words[2] = &quot;abc&quot;.
All the strings are now equal to &quot;abc&quot;, so return <code>true</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;ab&quot;,&quot;a&quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make all the strings equal using the operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

According to the problem description, as long as the occurrence count of each character can be divided by the length of the string array, it is possible to redistribute the characters to make all strings equal.

Therefore, we use a hash table or an integer array of length $26$ $\textit{cnt}$ to count the occurrences of each character. Finally, we check if the occurrence count of each character can be divided by the length of the string array.

The time complexity is $O(L)$, and the space complexity is $O(|\Sigma|)$. Here, $L$ is the total length of all strings in the array $\textit{words}$, and $\Sigma$ is the character set, which is the set of lowercase letters, so $|\Sigma|=26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = Counter()
        for w in words:
            for c in w:
                cnt[c] += 1
        n = len(words)
        return all(v % n == 0 for v in cnt.values())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
