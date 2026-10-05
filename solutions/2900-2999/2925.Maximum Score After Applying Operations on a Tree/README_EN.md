---
comments: true
difficulty: Medium
rating: 1939
source: Weekly Contest 370 Q3
tags:
    - Tree
    - Depth-First Search
    - Dynamic Programming
    - Tree DP
---

<!-- problem:start -->

# [2925. Maximum Score After Applying Operations on a Tree](https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree)

## Description

<!-- description:start -->

<p>There is an undirected tree with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>, and rooted at node <code>0</code>. You are given&nbsp;a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.</p>

<p>You are also given a <strong>0-indexed</strong> integer array <code>values</code> of length <code>n</code>, where <code>values[i]</code> is the <strong>value</strong> associated with the <code>i<sup>th</sup></code> node.</p>

<p>You start with a score of <code>0</code>. In one operation, you can:</p>

<ul>
	<li>Pick any node <code>i</code>.</li>
	<li>Add <code>values[i]</code> to your score.</li>
	<li>Set <code>values[i]</code> to <code>0</code>.</li>
</ul>

<p>A tree is <strong>healthy</strong> if the sum of values on the path from the root to any leaf node is different than zero.</p>

<p>Return <em>the <strong>maximum score</strong> you can obtain after performing these operations on the tree any number of times so that it remains <strong>healthy</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2900-2999/2925.Maximum%20Score%20After%20Applying%20Operations%20on%20a%20Tree/images/graph-13-1.png" style="width: 515px; height: 443px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[0,3],[2,4],[4,5]], values = [5,2,5,2,1,1]
<strong>Output:</strong> 11
<strong>Explanation:</strong> We can choose nodes 1, 2, 3, 4, and 5. The value of the root is non-zero. Hence, the sum of values on the path from the root to any leaf is different than zero. Therefore, the tree is healthy and the score is values[1] + values[2] + values[3] + values[4] + values[5] = 11.
It can be shown that 11 is the maximum score obtainable after any number of operations on the tree.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2900-2999/2925.Maximum%20Score%20After%20Applying%20Operations%20on%20a%20Tree/images/graph-14-2.png" style="width: 522px; height: 245px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [20,10,9,7,4,3,5]
<strong>Output:</strong> 40
<strong>Explanation:</strong> We can choose nodes 0, 2, 3, and 4.
- The sum of values on the path from 0 to 4 is equal to 10.
- The sum of values on the path from 0 to 3 is equal to 10.
- The sum of values on the path from 0 to 5 is equal to 3.
- The sum of values on the path from 0 to 6 is equal to 5.
Therefore, the tree is healthy and the score is values[0] + values[2] + values[3] + values[4] = 40.
It can be shown that 40 is the maximum score obtainable after any number of operations on the tree.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>values.length == n</code></li>
	<li><code>1 &lt;= values[i] &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that <code>edges</code> represents a valid tree.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Tree DP

<!-- thinking:start -->

> **Thinking**
>
> Every root-to-leaf path must keep at least one unselected node; the rest may add to the score. Enumerating select/skip at each vertex while enforcing every path explodes. Tree DP localizes the constraint: skip the root and take whole subtrees, or take the root and leave each subtree still valid.
>
> $dfs$ returns the subtree sum and the best valid selection. A leaf can only leave itself unselected, so the second value is $0$. An internal node takes $\max(values[i]+b, a)$. The answer is the second value at the root.

<!-- thinking:end -->

The problem is actually asking us to select some nodes from all nodes of the tree so that the sum of these nodes' values is maximized, and there is one node on each path from the root node to the leaf node that is not selected.

We can use the method of tree DP to solve this problem.

We design a function $dfs(i, fa)$, where $i$ represents the current node with node $i$ as the root of the subtree, and $fa$ represents the parent node of $i$. The function returns an array of length $2$, where $[0]$ represents the sum of the values of all nodes in the subtree, and $[1]$ represents the maximum value of the subtree satisfying that there is one node not selected on each path.

The value of $[0]$ can be obtained directly by DFS accumulating the values of each node, while the value of $[1]$ needs to consider two situations, namely whether node $i$ is selected. If it is selected, then each subtree of node $i$ must satisfy that there is one node not selected on each path; if it is not selected, then all nodes of each subtree of node $i$ can be selected. We take the maximum of these two situations.

It should be noted that the value of $[1]$ of the leaf node is $0$, because the leaf node has no subtree, so there is no need to consider the situation where there is one node not selected on each path.

The answer is $dfs(0, -1)[1]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        def dfs(i: int, fa: int = -1) -> (int, int):
            a = b = 0
            leaf = True
            for j in g[i]:
                if j != fa:
                    leaf = False
                    aa, bb = dfs(j, i)
                    a += aa
                    b += bb
            if leaf:
                return values[i], 0
            return values[i] + a, max(values[i] + b, a)

        g = [[] for _ in range(len(values))]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        return dfs(0)[1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Tree DP + Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> Every root-to-leaf path must keep at least one unselected node; the remaining values may add to the score. Enumerating select or skip at each vertex while enforcing every path grows with the number of paths and does not fit $n \le 2 \times 10^4$. Once the choice is localized to a subtree, skipping the current node takes each child subtree whole, and taking it requires every child subtree to stay valid; both choices depend only on the subtree sum and the valid score, so child order does not matter. Filling that pair by recursion along a chain uses a call depth equal to the node count and overflows Python's recursion limit. The stack therefore stores $(node, parent, state)$: state $0$ pushes the exit marker and then the children, and state $1$ writes the pair after the children are ready. A leaf stores second value $0$, an internal node takes $\max(values[i]+b, a)$, and the answer is the second value at the root.

<!-- thinking:end -->

The problem asks us to select some nodes so that the sum of their values is maximized, and every path from the root to a leaf keeps at least one node unselected.

We record two quantities for each subtree with tree DP and fill them in postorder on an explicit stack. For node $i$, the first value is the sum of every node in the subtree, and the second value is the maximum score the subtree can obtain while satisfying the path constraint. A leaf has no child, so it can leave an unselected node only by skipping itself: the first value is $values[i]$ and the second value is $0$. An internal node has two choices. Skipping $i$ takes every node in each child subtree, scoring the sum of those subtree sums $a$. Taking $i$ requires each child subtree to stay valid on its own, scoring $values[i]$ plus the sum of the child scores $b$. We keep the larger of the two.

Each stack frame is $(i, fa, state)$. When $state = 0$, we push $(i, fa, 1)$ and then push every neighbor other than the parent with state $0$, so the children finish first. When $state = 1$, we read the finished child results and write node $i$ by the rule above. The order in which children are pushed does not change the answer.

The answer is the second value at the root.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        sub = [(0, 0)] * n
        stk = [(0, -1, 0)]
        while stk:
            i, fa, state = stk.pop()
            if state == 0:
                stk.append((i, fa, 1))
                for j in g[i]:
                    if j != fa:
                        stk.append((j, i, 0))
            else:
                a = b = 0
                leaf = True
                for j in g[i]:
                    if j != fa:
                        leaf = False
                        aa, bb = sub[j]
                        a += aa
                        b += bb
                if leaf:
                    sub[i] = (values[i], 0)
                else:
                    sub[i] = (values[i] + a, max(values[i] + b, a))
        return sub[0][1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
