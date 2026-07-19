---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2068.Check%20Whether%20Two%20Strings%20are%20Almost%20Equivalent/README_EN.md
rating: 1273
source: Biweekly Contest 65 Q1
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [2068. Check Whether Two Strings are Almost Equivalent](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent)

## Description

<!-- description:start -->

<p>Two strings <code>word1</code> and <code>word2</code> are considered <strong>almost equivalent</strong> if the differences between the frequencies of each letter from <code>&#39;a&#39;</code> to <code>&#39;z&#39;</code> between <code>word1</code> and <code>word2</code> is <strong>at most</strong> <code>3</code>.</p>

<p>Given two strings <code>word1</code> and <code>word2</code>, each of length <code>n</code>, return <code>true</code> <em>if </em><code>word1</code> <em>and</em> <code>word2</code> <em>are <strong>almost equivalent</strong>, or</em> <code>false</code> <em>otherwise</em>.</p>

<p>The <strong>frequency</strong> of a letter <code>x</code> is the number of times it occurs in the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;aaaa&quot;, word2 = &quot;bccb&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> There are 4 &#39;a&#39;s in &quot;aaaa&quot; but 0 &#39;a&#39;s in &quot;bccb&quot;.
The difference is 4, which is more than the allowed 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abcdeef&quot;, word2 = &quot;abaaacc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The differences between the frequencies of each letter in word1 and word2 are at most 3:
- &#39;a&#39; appears 1 time in word1 and 4 times in word2. The difference is 3.
- &#39;b&#39; appears 1 time in word1 and 1 time in word2. The difference is 0.
- &#39;c&#39; appears 1 time in word1 and 2 times in word2. The difference is 1.
- &#39;d&#39; appears 1 time in word1 and 0 times in word2. The difference is 1.
- &#39;e&#39; appears 2 times in word1 and 0 times in word2. The difference is 2.
- &#39;f&#39; appears 1 time in word1 and 0 times in word2. The difference is 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;cccddabba&quot;, word2 = &quot;babababab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The differences between the frequencies of each letter in word1 and word2 are at most 3:
- &#39;a&#39; appears 2 times in word1 and 4 times in word2. The difference is 2.
- &#39;b&#39; appears 2 times in word1 and 5 times in word2. The difference is 3.
- &#39;c&#39; appears 3 times in word1 and 0 times in word2. The difference is 3.
- &#39;d&#39; appears 2 times in word1 and 0 times in word2. The difference is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == word1.length == word2.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We can create an array $cnt$ of length $26$ to record the difference in the number of times each letter appears in the two strings. Then we traverse $cnt$, if any letter appears the difference in the number of times greater than $3$, then return `false`, otherwise return `true`.

The time complexity is $O(n)$ and the space complexity is $O(C)$. Where $n$ is the length of the string, and $C$ is the size of the character set, and in this question $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt = Counter(word1)
        for c in word2:
            cnt[c] -= 1
        return all(abs(x) <= 3 for x in cnt.values())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
