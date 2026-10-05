---
comments: true
difficulty: Medium
rating: 1911
source: Weekly Contest 264 Q3
tags:
    - Tree
    - Depth-First Search
    - Array
    - Binary Tree
    - Tree DP
---

<!-- problem:start -->

# [2049. Count Nodes With the Highest Score](https://leetcode.com/problems/count-nodes-with-the-highest-score)

## Description

<!-- description:start -->

<p>There is a <strong>binary</strong> tree rooted at <code>0</code> consisting of <code>n</code> nodes. The nodes are labeled from <code>0</code> to <code>n - 1</code>. You are given a <strong>0-indexed</strong> integer array <code>parents</code> representing the tree, where <code>parents[i]</code> is the parent of node <code>i</code>. Since node <code>0</code> is the root, <code>parents[0] == -1</code>.</p>

<p>Each node has a <strong>score</strong>. To find the score of a node, consider if the node and the edges connected to it were <strong>removed</strong>. The tree would become one or more <strong>non-empty</strong> subtrees. The <strong>size</strong> of a subtree is the number of the nodes in it. The <strong>score</strong> of the node is the <strong>product of the sizes</strong> of all those subtrees.</p>

<p>Return <em>the <strong>number</strong> of nodes that have the <strong>highest score</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="example-1" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2049.Count%20Nodes%20With%20the%20Highest%20Score/images/example-1.png" style="width: 604px; height: 266px;" />
<pre>
<strong>Input:</strong> parents = [-1,2,0,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="example-2" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2049.Count%20Nodes%20With%20the%20Highest%20Score/images/example-2.png" style="width: 95px; height: 143px;" />
<pre>
<strong>Input:</strong> parents = [-1,2,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == parents.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>parents[0] == -1</code></li>
	<li><code>0 &lt;= parents[i] &lt;= n - 1</code> for <code>i != 0</code></li>
	<li><code>parents</code> represents a valid binary tree.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

<!-- thinking:start -->

> **Thinking**
>
> Removing a node scores the product of component sizes. With $n \le 10^5$ we need all scores in one walk. Subtree sizes appear on the DFS unwind; the complement is $n-cnt$.
>
> Build child lists and DFS from the root: multiply child sizes, then $n-cnt$ if nonzero. Track the maximum score and its multiplicity.

<!-- thinking:end -->

First, we construct a graph $g$ based on the given parent array `parents`, where $g[i]$ represents all child nodes of node $i$. We define a variable $ans$ to represent the number of nodes with the highest score, and a variable $mx$ to represent the highest score.

Then, we design a function `dfs(i, fa)` to calculate the score of node $i$ and return the number of nodes in the subtree rooted at node $i$.

The calculation process of the function `dfs(i, fa)` is as follows:

We first initialize a variable $cnt = 1$, representing the number of nodes in the subtree rooted at node $i$; a variable $score = 1$, representing the initial score of node $i$.

Next, we traverse all child nodes $j$ of node $i$. If $j$ is not the parent node $fa$ of node $i$, then we recursively call `dfs(j, i)`, and multiply the return value into $score$, and add the return value to $cnt$.

After traversing the child nodes, if $n - cnt > 0$, then we multiply $n - cnt$ into $score$.

Then, we check whether $mx$ is less than $score$. If it is less, then we update $mx$ to $score$, and update $ans$ to $1$; if it is equal, then we update $ans$ to $ans + 1$.

Finally, we return $cnt$.

In the end, we call `dfs(0, -1)` and return $ans$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def dfs(i: int, fa: int):
            cnt = score = 1
            for j in g[i]:
                if j != fa:
                    t = dfs(j, i)
                    score *= t
                    cnt += t
            if n - cnt:
                score *= n - cnt
            nonlocal ans, mx
            if mx < score:
                mx = score
                ans = 1
            elif mx == score:
                ans += 1
            return cnt

        n = len(parents)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)
        ans = mx = 0
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
> Removing a node scores the product of the remaining component sizes. $n$ can reach $10^5$. On a chain the first recursive call always follows the only child, so the depth is $n$ and exceeds the default recursion limit.
>
> The product needs every child's subtree size, and the component above the node has size $n$ minus that subtree.
>
> An explicit stack walks the tree in postorder. On entry, push the exit marker and then the children. On exit, multiply the child subtree sizes, then multiply by $n-cnt$ when a component remains above, and track the maximum score and how many nodes reach it.

<!-- thinking:end -->

First, we construct a graph $g$ based on the given parent array `parents`, where $g[i]$ represents all child nodes of node $i$. We define a variable $ans$ to represent the number of nodes with the highest score, and a variable $mx$ to represent the highest score.

An explicit stack walks the tree from root $0$ in postorder. Entering a node pushes that node's exit marker and then its children, so the children finish first. On exit, each child's subtree size is already stored. Initialize $cnt = 1$ and $score = 1$. Multiply each child's subtree size into $score$ and add it to $cnt$. If $n - cnt > 0$, also multiply $n - cnt$ into $score$. If $score$ is greater than $mx$, set $mx$ to $score$ and $ans$ to $1$; if they are equal, add $1$ to $ans$. Store $cnt$ as the current node's subtree size.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)
        ans = mx = 0
        sz = [0] * n
        stk = [(0, -1, 0)]
        while stk:
            i, fa, state = stk.pop()
            if state == 0:
                stk.append((i, fa, 1))
                for j in g[i]:
                    if j != fa:
                        stk.append((j, i, 0))
            else:
                cnt = score = 1
                for j in g[i]:
                    if j != fa:
                        t = sz[j]
                        score *= t
                        cnt += t
                if n - cnt:
                    score *= n - cnt
                if mx < score:
                    mx = score
                    ans = 1
                elif mx == score:
                    ans += 1
                sz[i] = cnt
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
