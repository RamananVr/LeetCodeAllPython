---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0208.Implement%20Trie%20%28Prefix%20Tree%29/README_EN.md
tags:
    - Design
    - Trie
    - Hash Table
    - String
---

<!-- problem:start -->

# [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)

## Description

<!-- description:start -->

<p>A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank"><strong>trie</strong></a> (pronounced as &quot;try&quot;) or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>

<p>Implement the Trie class:</p>

<ul>
	<li><code>Trie()</code> Initializes the trie object.</li>
	<li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
	<li><code>boolean search(String word)</code> Returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
	<li><code>boolean startsWith(String prefix)</code> Returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Trie&quot;, &quot;insert&quot;, &quot;search&quot;, &quot;search&quot;, &quot;startsWith&quot;, &quot;insert&quot;, &quot;search&quot;]
[[], [&quot;apple&quot;], [&quot;apple&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // return True
trie.search(&quot;app&quot;);     // return False
trie.startsWith(&quot;app&quot;); // return True
trie.insert(&quot;app&quot;);
trie.search(&quot;app&quot;);     // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> and <code>prefix</code> consist only of lowercase English letters.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

## Solution 1: Trie (Prefix Tree)

Each node in the trie contains two parts:

1. An array of pointers to child nodes `children`. For this problem, the array length is 26, representing the number of lowercase English letters. `children[0]` corresponds to lowercase letter 'a', ..., and `children[25]` corresponds to lowercase letter 'z'.
2. A boolean field `isEnd` indicating whether the node is the end of a string.

### 1. Insert a String

We start from the root of the trie and insert the string. For the child node corresponding to the current character, there are two cases:

- The child node exists. Move along the pointer to the child node and continue processing the next character.
- The child node does not exist. Create a new child node, record it in the corresponding position of the `children` array, then move along the pointer to the child node and continue searching for the next character.

Repeat the above steps until the last character of the string is processed, then mark the current node as the end of the string.

### 2. Search for a Prefix

We start from the root of the trie and search for the prefix. For the child node corresponding to the current character, there are two cases:

- The child node exists. Move along the pointer to the child node and continue searching for the next character.
- The child node does not exist. This means the trie does not contain the prefix, so return a null pointer.

Repeat the above steps until a null pointer is returned or the last character of the prefix is searched.

If we search to the end of the prefix, it means the trie contains the prefix. Additionally, if the `isEnd` of the node corresponding to the end of the prefix is true, it means the trie contains the string.

The time complexity for inserting a string is $O(m \times |\Sigma|)$, and the time complexity for searching a prefix is $O(m)$, where $m$ is the length of the string and $|\Sigma|$ is the size of the character set (26 in this problem). The space complexity is $O(q \times m \times |\Sigma|)$, where $q$ is the number of inserted strings.

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None

    def _search_prefix(self, prefix: str):
        node = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
