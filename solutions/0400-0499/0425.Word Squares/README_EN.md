---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0425.Word%20Squares/README_EN.md
tags:
    - Trie
    - Array
    - String
    - Backtracking
---

<!-- problem:start -->

# [425. Word Squares 🔒](https://leetcode.com/problems/word-squares)

## Description

<!-- description:start -->

<p>Given an array of <strong>unique</strong> strings <code>words</code>, return <em>all the </em><strong><a href="https://en.wikipedia.org/wiki/Word_square" target="_blank">word squares</a></strong><em> you can build from </em><code>words</code>. The same word from <code>words</code> can be used <strong>multiple times</strong>. You can return the answer in <strong>any order</strong>.</p>

<p>A sequence of strings forms a valid <strong>word square</strong> if the <code>k<sup>th</sup></code> row and column read the same string, where <code>0 &lt;= k &lt; max(numRows, numColumns)</code>.</p>

<ul>
	<li>For example, the word sequence <code>[&quot;ball&quot;,&quot;area&quot;,&quot;lead&quot;,&quot;lady&quot;]</code> forms a word square because each word reads the same both horizontally and vertically.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;area&quot;,&quot;lead&quot;,&quot;wall&quot;,&quot;lady&quot;,&quot;ball&quot;]
<strong>Output:</strong> [[&quot;ball&quot;,&quot;area&quot;,&quot;lead&quot;,&quot;lady&quot;],[&quot;wall&quot;,&quot;area&quot;,&quot;lead&quot;,&quot;lady&quot;]]
<strong>Explanation:</strong>
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abat&quot;,&quot;baba&quot;,&quot;atan&quot;,&quot;atal&quot;]
<strong>Output:</strong> [[&quot;baba&quot;,&quot;abat&quot;,&quot;baba&quot;,&quot;atal&quot;],[&quot;baba&quot;,&quot;abat&quot;,&quot;baba&quot;,&quot;atan&quot;]]
<strong>Explanation:</strong>
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 4</code></li>
	<li>All <code>words[i]</code> have the same length.</li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li>All <code>words[i]</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.v = []

    def insert(self, w, i):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.v.append(i)

    def search(self, w):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return []
            node = node.children[idx]
        return node.v

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def dfs(t):
            if len(t) == len(words[0]):
                ans.append(t[:])
                return
            idx = len(t)
            pref = [v[idx] for v in t]
            indexes = trie.search(''.join(pref))
            for i in indexes:
                t.append(words[i])
                dfs(t)
                t.pop()

        trie = Trie()
        ans = []
        for i, w in enumerate(words):
            trie.insert(w, i)
        for w in words:
            dfs([w])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
