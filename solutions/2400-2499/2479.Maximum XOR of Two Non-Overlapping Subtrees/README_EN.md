---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2479.Maximum%20XOR%20of%20Two%20Non-Overlapping%20Subtrees/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Graph
    - Trie
---

<!-- problem:start -->

# [2479. Maximum XOR of Two Non-Overlapping Subtrees 🔒](https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees)

## Description

<!-- description:start -->

<p>There is an undirected tree with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given the integer <code>n</code> and a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree. The root of the tree is the node labeled <code>0</code>.</p>

<p>Each node has an associated <strong>value</strong>. You are given an array <code>values</code> of length <code>n</code>, where <code>values[i]</code> is the <strong>value</strong> of the <code>i<sup>th</sup></code> node.</p>

<p>Select any two <strong>non-overlapping</strong> subtrees. Your <strong>score</strong> is the bitwise XOR of the sum of the values within those subtrees.</p>

<p>Return <em>the</em> <em><strong>maximum</strong></em> <i>possible <strong>score</strong> you can achieve</i>. <em>If it is impossible to find two nonoverlapping subtrees</em>, return <code>0</code>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The <strong>subtree</strong> of a node is the tree consisting of that node and all of its descendants.</li>
	<li>Two subtrees are <strong>non-overlapping </strong>if they do not share <strong>any common</strong> node.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2479.Maximum%20XOR%20of%20Two%20Non-Overlapping%20Subtrees/images/treemaxxor.png" style="width: 346px; height: 249px;" />
<pre>
<strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[1,3],[1,4],[2,5]], values = [2,8,3,6,2,5]
<strong>Output:</strong> 24
<strong>Explanation:</strong> Node 1&#39;s subtree has sum of values 16, while node 2&#39;s subtree has sum of values 8, so choosing these nodes will yield a score of 16 XOR 8 = 24. It can be proved that is the maximum possible score we can obtain.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2479.Maximum%20XOR%20of%20Two%20Non-Overlapping%20Subtrees/images/tree3drawio.png" style="width: 240px; height: 261px;" />
<pre>
<strong>Input:</strong> n = 3, edges = [[0,1],[1,2]], values = [4,6,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no possible way to select two non-overlapping subtrees, so we just return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>values.length == n</code></li>
	<li><code>1 &lt;= values[i] &lt;= 10<sup>9</sup></code></li>
	<li>It is guaranteed that <code>edges</code> represents a valid tree.</li>
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
        self.children = [None] * 2

    def insert(self, x):
        node = self
        for i in range(47, -1, -1):
            v = (x >> i) & 1
            if node.children[v] is None:
                node.children[v] = Trie()
            node = node.children[v]

    def search(self, x):
        node = self
        res = 0
        for i in range(47, -1, -1):
            v = (x >> i) & 1
            if node is None:
                return res
            if node.children[v ^ 1]:
                res = res << 1 | 1
                node = node.children[v ^ 1]
            else:
                res <<= 1
                node = node.children[v]
        return res

class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        def dfs1(i, fa):
            t = values[i]
            for j in g[i]:
                if j != fa:
                    t += dfs1(j, i)
            s[i] = t
            return t

        def dfs2(i, fa):
            nonlocal ans
            ans = max(ans, tree.search(s[i]))
            for j in g[i]:
                if j != fa:
                    dfs2(j, i)
            tree.insert(s[i])

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        s = [0] * n
        dfs1(0, -1)
        ans = 0
        tree = Trie()
        dfs2(0, -1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
