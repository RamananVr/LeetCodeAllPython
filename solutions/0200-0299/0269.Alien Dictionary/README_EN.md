---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0269.Alien%20Dictionary/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
    - Topological Sort
    - Array
    - String
---

<!-- problem:start -->

# [269. Alien Dictionary 🔒](https://leetcode.com/problems/alien-dictionary)

## Description

<!-- description:start -->

<p>There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.</p>

<p>You are given a list of strings <code>words</code> from the alien language&#39;s dictionary. Now it is claimed that the strings in <code>words</code> are <span data-keyword="lexicographically-smaller-string-alien"><strong>sorted lexicographically</strong></span> by the rules of this new language.</p>

<p>If this claim is incorrect, and the given arrangement of string in&nbsp;<code>words</code>&nbsp;cannot correspond to any order of letters,&nbsp;return&nbsp;<code>&quot;&quot;.</code></p>

<p>Otherwise, return <em>a string of the unique letters in the new alien language sorted in <strong>lexicographically increasing order</strong> by the new language&#39;s rules</em><em>. </em>If there are multiple solutions, return<em> <strong>any of them</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;wrt&quot;,&quot;wrf&quot;,&quot;er&quot;,&quot;ett&quot;,&quot;rftt&quot;]
<strong>Output:</strong> &quot;wertf&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;z&quot;,&quot;x&quot;]
<strong>Output:</strong> &quot;zx&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;z&quot;,&quot;x&quot;,&quot;z&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> The order is invalid, so return <code>&quot;&quot;</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = [[False] * 26 for _ in range(26)]
        s = [False] * 26
        cnt = 0
        n = len(words)
        for i in range(n - 1):
            for c in words[i]:
                if cnt == 26:
                    break
                o = ord(c) - ord('a')
                if not s[o]:
                    cnt += 1
                    s[o] = True
            m = len(words[i])
            for j in range(m):
                if j >= len(words[i + 1]):
                    return ''
                c1, c2 = words[i][j], words[i + 1][j]
                if c1 == c2:
                    continue
                o1, o2 = ord(c1) - ord('a'), ord(c2) - ord('a')
                if g[o2][o1]:
                    return ''
                g[o1][o2] = True
                break
        for c in words[n - 1]:
            if cnt == 26:
                break
            o = ord(c) - ord('a')
            if not s[o]:
                cnt += 1
                s[o] = True

        indegree = [0] * 26
        for i in range(26):
            for j in range(26):
                if i != j and s[i] and s[j] and g[i][j]:
                    indegree[j] += 1
        q = deque()
        ans = []
        for i in range(26):
            if s[i] and indegree[i] == 0:
                q.append(i)
        while q:
            t = q.popleft()
            ans.append(chr(t + ord('a')))
            for i in range(26):
                if s[i] and i != t and g[t][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        return '' if len(ans) < cnt else ''.join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
