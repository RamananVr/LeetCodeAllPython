---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0616.Add%20Bold%20Tag%20in%20String/README_EN.md
tags:
    - Trie
    - Array
    - Hash Table
    - String
    - String Matching
---

<!-- problem:start -->

# [616. Add Bold Tag in String 🔒](https://leetcode.com/problems/add-bold-tag-in-string)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> and an array of strings <code>words</code>.</p>

<p>You should add a closed pair of bold tag <code>&lt;b&gt;</code> and <code>&lt;/b&gt;</code> to wrap the substrings in <code>s</code> that exist in <code>words</code>.</p>

<ul>
	<li>If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.</li>
	<li>If two substrings wrapped by bold tags are consecutive, you should combine them.</li>
</ul>

<p>Return <code>s</code> <em>after adding the bold tags</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcxyz123&quot;, words = [&quot;abc&quot;,&quot;123&quot;]
<strong>Output:</strong> &quot;&lt;b&gt;abc&lt;/b&gt;xyz&lt;b&gt;123&lt;/b&gt;&quot;
<strong>Explanation:</strong> The two strings of words are substrings of s as following: &quot;<u>abc</u>xyz<u>123</u>&quot;.
We add &lt;b&gt; before each substring and &lt;/b&gt; after each substring.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabbb&quot;, words = [&quot;aa&quot;,&quot;b&quot;]
<strong>Output:</strong> &quot;&lt;b&gt;aaabbb&lt;/b&gt;&quot;
<strong>Explanation:</strong> 
&quot;aa&quot; appears as a substring two times: &quot;<u>aa</u>abbb&quot; and &quot;a<u>aa</u>bbb&quot;.
&quot;b&quot; appears as a substring three times: &quot;aaa<u>b</u>bb&quot;, &quot;aaab<u>b</u>b&quot;, and &quot;aaabb<u>b</u>&quot;.
We add &lt;b&gt; before each substring and &lt;/b&gt; after each substring: &quot;&lt;b&gt;a&lt;b&gt;a&lt;/b&gt;a&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&quot;.
Since the first two &lt;b&gt;&#39;s overlap, we merge them: &quot;&lt;b&gt;aaa&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&quot;.
Since now the four &lt;b&gt;&#39;s are consecutive, we merge them: &quot;&lt;b&gt;aaabbb&lt;/b&gt;&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>0 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>s</code> and <code>words[i]</code> consist of English letters and digits.</li>
	<li>All the values of <code>words</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/bold-words-in-string/description/" target="_blank">758. Bold Words in String</a>.</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children = [None] * 128
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            idx = ord(c)
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)
        n = len(s)
        pairs = []
        for i in range(n):
            node = trie
            for j in range(i, n):
                idx = ord(s[j])
                if node.children[idx] is None:
                    break
                node = node.children[idx]
                if node.is_end:
                    pairs.append([i, j])
        if not pairs:
            return s
        st, ed = pairs[0]
        t = []
        for a, b in pairs[1:]:
            if ed + 1 < a:
                t.append([st, ed])
                st, ed = a, b
            else:
                ed = max(ed, b)
        t.append([st, ed])

        ans = []
        i = j = 0
        while i < n:
            if j == len(t):
                ans.append(s[i:])
                break
            st, ed = t[j]
            if i < st:
                ans.append(s[i:st])
            ans.append('<b>')
            ans.append(s[st : ed + 1])
            ans.append('</b>')
            j += 1
            i = ed + 1

        return ''.join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
