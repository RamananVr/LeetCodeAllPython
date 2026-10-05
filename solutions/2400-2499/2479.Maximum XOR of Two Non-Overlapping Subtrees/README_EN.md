---
comments: true
difficulty: Hard
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

<!-- thinking:start -->

> **Thinking**
>
> Maximum XOR of two non-overlapping subtree sums; $n\le 5\times 10^4$. First DFS computes $s[i]$. A second walk queries the trie before inserting: the query sees only finished subtrees that do not overlap the current one; the current sum is inserted after the children return.
>
> Sums reach about $10^{14}$, so a $48$-bit binary trie greedy-picks the opposite bit.

<!-- thinking:end -->

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

<!-- solution:start -->

### Solution 2: Explicit Stack + Binary Trie

<!-- thinking:start -->

> **Thinking**
>
> The score is the maximum XOR of two disjoint subtree sums, and $n$ reaches $5\times 10^4$. Recursing down a chain for the sums and again for the trie walk exhausts the call stack.
>
> The bottleneck is those two chains: each call steps to the next child, so the depth tracks $n$.
>
> A subtree sum depends only on its children. A query is valid only against a finished subtree that does not overlap the current one, which means the current sum must be inserted after its children.
>
> Both walks use an explicit stack. The first accumulates $s[i]$ after the children. The second searches a $48$-bit binary trie on pop, then inserts $s[i]$ once the children are done. Sums reach about $10^{14}$, so each bit still prefers the opposite branch.

<!-- thinking:end -->

An explicit stack computes each subtree sum. A second stack queries a binary trie before inserting that sum, so the two subtrees do not overlap.

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
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        s = [0] * n
        stk = [(0, -1, 0)]
        while stk:
            i, fa, state = stk.pop()
            if state == 0:
                stk.append((i, fa, 1))
                for j in reversed(g[i]):
                    if j != fa:
                        stk.append((j, i, 0))
            else:
                t = values[i]
                for j in g[i]:
                    if j != fa:
                        t += s[j]
                s[i] = t
        ans = 0
        tree = Trie()
        stk = [(0, -1, 0)]
        while stk:
            i, fa, state = stk.pop()
            if state == 0:
                ans = max(ans, tree.search(s[i]))
                stk.append((i, fa, 1))
                for j in reversed(g[i]):
                    if j != fa:
                        stk.append((j, i, 0))
            else:
                tree.insert(s[i])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
