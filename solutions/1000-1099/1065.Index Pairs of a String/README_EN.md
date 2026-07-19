---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1065.Index%20Pairs%20of%20a%20String/README_EN.md
rating: 1389
source: Biweekly Contest 1 Q2
tags:
    - Trie
    - Array
    - String
    - Sorting
---

<!-- problem:start -->

# [1065. Index Pairs of a String 🔒](https://leetcode.com/problems/index-pairs-of-a-string)

## Description

<!-- description:start -->

<p>Given a string <code>text</code> and an array of strings <code>words</code>, return <em>an array of all index pairs </em><code>[i, j]</code><em> so that the substring </em><code>text[i...j]</code><em> is in <code>words</code></em>.</p>

<p>Return the pairs <code>[i, j]</code> in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;thestoryofleetcodeandme&quot;, words = [&quot;story&quot;,&quot;fleet&quot;,&quot;leetcode&quot;]
<strong>Output:</strong> [[3,7],[9,13],[10,17]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;ababa&quot;, words = [&quot;aba&quot;,&quot;ab&quot;]
<strong>Output:</strong> [[0,1],[0,2],[2,3],[2,4]]
<strong>Explanation:</strong> Notice that matches can overlap, see &quot;aba&quot; is found in [0,2] and [2,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 100</code></li>
	<li><code>1 &lt;= words.length &lt;= 20</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>text</code> and <code>words[i]</code> consist of lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        words = set(words)
        n = len(text)
        return [
            [i, j] for i in range(n) for j in range(i, n) if text[i : j + 1] in words
        ]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        n = len(text)
        ans = []
        for i in range(n):
            node = trie
            for j in range(i, n):
                idx = ord(text[j]) - ord('a')
                if node.children[idx] is None:
                    break
                node = node.children[idx]
                if node.is_end:
                    ans.append([i, j])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
