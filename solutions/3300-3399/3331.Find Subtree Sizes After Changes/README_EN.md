---
comments: true
difficulty: Medium
rating: 2045
source: Biweekly Contest 142 Q2
tags:
    - Tree
    - Depth-First Search
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [3331. Find Subtree Sizes After Changes](https://leetcode.com/problems/find-subtree-sizes-after-changes)

## Description

<!-- description:start -->

<p>You are given a tree rooted at node 0 that consists of <code>n</code> nodes numbered from <code>0</code> to <code>n - 1</code>. The tree is represented by an array <code>parent</code> of size <code>n</code>, where <code>parent[i]</code> is the parent of node <code>i</code>. Since node 0 is the root, <code>parent[0] == -1</code>.</p>

<p>You are also given a string <code>s</code> of length <code>n</code>, where <code>s[i]</code> is the character assigned to node <code>i</code>.</p>

<p>We make the following changes on the tree <strong>one</strong> time <strong>simultaneously</strong> for all nodes <code>x</code> from <code>1</code> to <code>n - 1</code>:</p>

<ul>
	<li>Find the <strong>closest</strong> node <code>y</code> to node <code>x</code> such that <code>y</code> is an ancestor of <code>x</code>, and <code>s[x] == s[y]</code>.</li>
	<li>If node <code>y</code> does not exist, do nothing.</li>
	<li>Otherwise, <strong>remove</strong> the edge between <code>x</code> and its current parent and make node <code>y</code> the new parent of <code>x</code> by adding an edge between them.</li>
</ul>

<p>Return an array <code>answer</code> of size <code>n</code> where <code>answer[i]</code> is the <strong>size</strong> of the <span data-keyword="subtree">subtree</span> rooted at node <code>i</code> in the <strong>final</strong> tree.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">parent = [-1,0,0,1,1,1], s = &quot;abaabc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[6,3,1,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3300-3399/3331.Find%20Subtree%20Sizes%20After%20Changes/images/graphex1drawio.png" style="width: 230px; height: 277px;" />
<p>The parent of node 3 will change from node 1 to node 0.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">parent = [-1,0,4,0,1], s = &quot;abbba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[5,2,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3300-3399/3331.Find%20Subtree%20Sizes%20After%20Changes/images/exgraph2drawio.png" style="width: 160px; height: 308px;" />
<p>The following changes will happen at the same time:</p>

<ul>
	<li>The parent of node 4 will change from node 1 to node 0.</li>
	<li>The parent of node 2 will change from node 4 to node 1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == parent.length == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= parent[i] &lt;= n - 1</code> for all <code>i &gt;= 1</code>.</li>
	<li><code>parent[0] == -1</code></li>
	<li><code>parent</code> represents a valid tree.</li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A node may be reattached under its nearest ancestor with the same letter. With $n \le 10^5$ we should not rebuild the edge list and then recount subtrees.
>
> One DFS is enough: stacks $\textit{d}[c]$ store ancestors of letter $c$. Before returning, we add the current subtree size to the previous same-letter ancestor if it exists, otherwise to the parent.
>
> Post-order ensures $\textit{ans}[i]$ already includes every descendant; popping the stack restores the ancestor chain.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs(i: int, fa: int):
            ans[i] = 1
            d[s[i]].append(i)
            for j in g[i]:
                dfs(j, i)
            k = fa
            if len(d[s[i]]) > 1:
                k = d[s[i]][-2]
            if k != -1:
                ans[k] += ans[i]
            d[s[i]].pop()

        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        d = defaultdict(list)
        ans = [0] * n
        dfs(0, -1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> A node may be reattached under its nearest ancestor with the same letter. $n$ can reach $10^5$, so rebuilding the edge list and then recounting subtrees is unnecessary. On a chain the first recursive call always follows the only child, so the depth is $n$ and exceeds the default recursion limit.
>
> A subtree size can be added to its new parent only after every descendant has been counted, and a same-letter ancestor lies on the current path.
>
> An explicit stack walks the tree in postorder, while $\textit{d}[c]$ stores the nodes of letter $c$ still on the path. On entry, set the node's size to $1$, push it onto its letter stack, then push the exit marker and the children. On exit, add the subtree size to the earlier same-letter node when one exists, otherwise to the parent, and pop the letter stack.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        d = [[] for _ in range(26)]
        ans = [0] * n
        stk = [(0, -1, 0)]
        while stk:
            i, fa, state = stk.pop()
            if state == 0:
                ans[i] = 1
                idx = ord(s[i]) - 97
                d[idx].append(i)
                stk.append((i, fa, 1))
                for j in g[i]:
                    stk.append((j, i, 0))
            else:
                idx = ord(s[i]) - 97
                k = d[idx][-2] if len(d[idx]) > 1 else fa
                if k != -1:
                    ans[k] += ans[i]
                d[idx].pop()
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
