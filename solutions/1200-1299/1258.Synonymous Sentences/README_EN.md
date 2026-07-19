---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1258.Synonymous%20Sentences/README_EN.md
rating: 1847
source: Biweekly Contest 13 Q3
tags:
    - Sort
    - Union Find
    - Array
    - Hash Table
    - String
    - Backtracking
---

<!-- problem:start -->

# [1258. Synonymous Sentences 🔒](https://leetcode.com/problems/synonymous-sentences)

## Description

<!-- description:start -->

<p>You are given a list of equivalent string pairs <code>synonyms</code> where <code>synonyms[i] = [s<sub>i</sub>, t<sub>i</sub>]</code> indicates that <code>s<sub>i</sub></code> and <code>t<sub>i</sub></code> are equivalent strings. You are also given a sentence <code>text</code>.</p>

<p>Return <em>all possible synonymous sentences <strong>sorted lexicographically</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> synonyms = [[&quot;happy&quot;,&quot;joy&quot;],[&quot;sad&quot;,&quot;sorrow&quot;],[&quot;joy&quot;,&quot;cheerful&quot;]], text = &quot;I am happy today but was sad yesterday&quot;
<strong>Output:</strong> [&quot;I am cheerful today but was sad yesterday&quot;,&quot;I am cheerful today but was sorrow yesterday&quot;,&quot;I am happy today but was sad yesterday&quot;,&quot;I am happy today but was sorrow yesterday&quot;,&quot;I am joy today but was sad yesterday&quot;,&quot;I am joy today but was sorrow yesterday&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> synonyms = [[&quot;happy&quot;,&quot;joy&quot;],[&quot;cheerful&quot;,&quot;glad&quot;]], text = &quot;I am happy today but was sad yesterday&quot;
<strong>Output:</strong> [&quot;I am happy today but was sad yesterday&quot;,&quot;I am joy today but was sad yesterday&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= synonyms.length &lt;= 10</code></li>
	<li><code>synonyms[i].length == 2</code></li>
	<li><code>1 &lt;= s<sub>i</sub>.length,<sub> </sub>t<sub>i</sub>.length &lt;= 10</code></li>
	<li><code>s<sub>i</sub> != t<sub>i</sub></code></li>
	<li><code>text</code> consists of at most <code>10</code> words.</li>
	<li>All the pairs of&nbsp;<code>synonyms</code> are <strong>unique</strong>.</li>
	<li>The words of <code>text</code> are separated by single spaces.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Union-Find + DFS

We can notice that the synonyms in the problem are transitive, i.e., if `a` and `b` are synonyms, and `b` and `c` are synonyms, then `a` and `c` are also synonyms. Therefore, we can use a union-find set to find the connected components of synonyms, where all the words in each connected component are synonyms and are sorted in lexicographical order.

Next, we split the string `text` into a word array `sentence` by spaces. For each word `sentence[i]`, if it is a synonym, we replace it with all the words in the connected component, otherwise, we do not replace it. In this way, we can get all the sentences. This can be implemented by DFS search.

We design a function $dfs(i)$, which represents starting from the $i$th word of `sentence`, replacing it with all the words in the connected component, and then recursively processing the following words.

If $i$ is greater than or equal to the length of `sentence`, it means that we have processed all the words, and at this time, we add the current sentence to the answer array. Otherwise, if `sentence[i]` is not a synonym, we do not replace it, directly add it to the current sentence, and then recursively process the following words. Otherwise, we replace `sentence[i]` with all the words in the connected component, and also recursively process the following words.

Finally, return the answer array.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Where $n$ is the number of words.

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.size[pa] > self.size[pb]:
                self.p[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.p[pa] = pb
                self.size[pb] += self.size[pa]

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def dfs(i):
            if i >= len(sentence):
                ans.append(' '.join(t))
                return
            if sentence[i] not in d:
                t.append(sentence[i])
                dfs(i + 1)
                t.pop()
            else:
                root = uf.find(d[sentence[i]])
                for j in g[root]:
                    t.append(words[j])
                    dfs(i + 1)
                    t.pop()

        words = list(set(chain.from_iterable(synonyms)))
        d = {w: i for i, w in enumerate(words)}
        uf = UnionFind(len(d))
        for a, b in synonyms:
            uf.union(d[a], d[b])
        g = defaultdict(list)
        for i in range(len(words)):
            g[uf.find(i)].append(i)
        for k in g.keys():
            g[k].sort(key=lambda i: words[i])
        sentence = text.split()
        ans = []
        t = []
        dfs(0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
