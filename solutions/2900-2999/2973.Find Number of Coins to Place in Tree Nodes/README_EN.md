---
comments: true
difficulty: Hard
rating: 2276
source: Biweekly Contest 120 Q4
tags:
    - Tree
    - Depth-First Search
    - Dynamic Programming
    - Sorting
    - Tree DP
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2973. Find Number of Coins to Place in Tree Nodes](https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes)

## Description

<!-- description:start -->

<p>You are given an <strong>undirected</strong> tree with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>, and rooted at node <code>0</code>. You are given a 2D integer array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.</p>

<p>You are also given a <strong>0-indexed</strong> integer array <code>cost</code> of length <code>n</code>, where <code>cost[i]</code> is the <strong>cost</strong> assigned to the <code>i<sup>th</sup></code> node.</p>

<p>You need to place some coins on every node of the tree. The number of coins to be placed at node <code>i</code> can be calculated as:</p>

<ul>
	<li>If size of the subtree of node <code>i</code> is less than <code>3</code>, place <code>1</code> coin.</li>
	<li>Otherwise, place an amount of coins equal to the <strong>maximum</strong> product of cost values assigned to <code>3</code> distinct nodes in the subtree of node <code>i</code>. If this product is <strong>negative</strong>, place <code>0</code> coins.</li>
</ul>

<p>Return <em>an array </em><code>coin</code><em> of size </em><code>n</code><em> such that </em><code>coin[i]</code><em> is the number of coins placed at node </em><code>i</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2900-2999/2973.Find%20Number%20of%20Coins%20to%20Place%20in%20Tree%20Nodes/images/screenshot-2023-11-10-012641.png" style="width: 600px; height: 233px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
<strong>Output:</strong> [120,1,1,1,1,1]
<strong>Explanation:</strong> For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2900-2999/2973.Find%20Number%20of%20Coins%20to%20Place%20in%20Tree%20Nodes/images/screenshot-2023-11-10-012614.png" style="width: 800px; height: 374px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
<strong>Output:</strong> [280,140,32,1,1,1,1,1,1]
<strong>Explanation:</strong> The coins placed on each node are:
- Place 8 * 7 * 5 = 280 coins on node 0.
- Place 7 * 5 * 4 = 140 coins on node 1.
- Place 8 * 2 * 2 = 32 coins on node 2.
- All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2900-2999/2973.Find%20Number%20of%20Coins%20to%20Place%20in%20Tree%20Nodes/images/screenshot-2023-11-10-012513.png" style="width: 300px; height: 277px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[0,2]], cost = [1,2,-2]
<strong>Output:</strong> [0,1,1]
<strong>Explanation:</strong> Node 1 and 2 are leaves with subtree of size 1, place 1 coin on each of them. For node 0 the only possible product of cost is 2 * 1 * -2 = -4. Hence place 0 coins on node 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>cost.length == n</code></li>
	<li><code>1 &lt;= |cost[i]| &lt;= 10<sup>4</sup></code></li>
	<li>The input is generated such that <code>edges</code> represents a valid tree.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + Sorting

<!-- thinking:start -->

> **Thinking**
>
> A subtree with fewer than three nodes places $1$; otherwise it places the maximum product of three costs, or $0$ if that product is negative. The maximum is either the three largest values or the two smallest (negative) times the largest. A subtree may have $n$ nodes, so the full list cannot be sent upward.
>
> DFS returns a sorted list keeping the two smallest and three largest values. After merging children, trim, then compute the node’s answer.

<!-- thinking:end -->

According to the problem description, there are two situations for the number of coins placed at each node $a$:

- If the number of nodes in the subtree corresponding to node $a$ is less than $3$, then place $1$ coin;
- If the number of nodes in the subtree corresponding to node $a$ is greater than or equal to $3$, then we need to take out $3$ different nodes from the subtree, calculate the maximum value of their cost product, and then place the corresponding number of coins at node $a$. If the maximum product is negative, place $0$ coins.

The first situation is relatively simple, we just need to count the number of nodes in the subtree of each node during the traversal.

For the second situation, if all costs are positive, we should take the $3$ nodes with the largest costs; if there are negative costs, we should take the $2$ nodes with the smallest costs and the $1$ node with the largest cost. Therefore, we need to maintain the smallest $2$ costs and the largest $3$ costs in each subtree.

We first construct the adjacency list $g$ based on the given two-dimensional array $edges$, where $g[a]$ represents all neighbor nodes of node $a$.

Next, we design a function $dfs(a, fa)$, which returns an array $res$, which stores the smallest $2$ costs and the largest $3$ costs in the subtree of node $a$ (may not be $5$).

In the function $dfs(a, fa)$, we add the cost $cost[a]$ of node $a$ to the array $res$, and then traverse all neighbor nodes $b$ of node $a$. If $b$ is not the parent node $fa$ of node $a$, then we add the result of $dfs(b, a)$ to the array $res$.

Then, we sort the array $res$, and then calculate the number of coins placed at node $a$ based on the length $m$ of the array $res$, and update $ans[a]$:

- If $m \ge 3$, then the number of coins placed at node $a$ is $\max(0, res[m - 1] \times res[m - 2] \times res[m - 3], res[0] \times res[1] \times res[m - 1])$, otherwise the number of coins placed at node $a$ is $1$;
- If $m > 5$, then we only need to keep the first $2$ elements and the last $3$ elements of the array $res$.

Finally, we call the function $dfs(0, -1)$, and return the answer array $ans$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        def dfs(a: int, fa: int) -> List[int]:
            res = [cost[a]]
            for b in g[a]:
                if b != fa:
                    res.extend(dfs(b, a))
            res.sort()
            if len(res) >= 3:
                ans[a] = max(res[-3] * res[-2] * res[-1], res[0] * res[1] * res[-1], 0)
            if len(res) > 5:
                res = res[:2] + res[-3:]
            return res

        n = len(cost)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = [1] * n
        dfs(0, -1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Explicit Stack + Sorting

<!-- thinking:start -->

> **Thinking**
>
> A subtree with fewer than three nodes places $1$ coin; otherwise it places the maximum product of three costs, or $0$ when that product is negative. The maximum is either the three largest costs or the two smallest costs times the largest. A subtree may contain $n$ nodes, so the full list cannot be sent upward, and each subtree keeps only the two smallest and three largest costs. Merging those lists by recursion along a chain uses a call depth equal to the node count and overflows Python once $n$ reaches $1000$, while $n$ can be $2 \times 10^4$. The stack stores $(node, parent, state)$: state $0$ pushes the exit marker and then the children, and state $1$ merges, sorts, and trims the child lists before writing the current answer.

<!-- thinking:end -->

There are two cases for the number of coins placed at node $a$:

- If the subtree of $a$ has fewer than $3$ nodes, place $1$ coin.
- If the subtree has at least $3$ nodes, take $3$ different nodes, place their maximum cost product at $a$, and place $0$ when that product is negative.

When every cost is positive, the product uses the $3$ largest costs. When negatives appear, the two smallest costs times the largest cost must also be considered. Each subtree therefore keeps only its $2$ smallest costs and its $3$ largest costs.

Build the graph from $edges$ and set every answer to $1$. An explicit stack processes nodes in postorder. Each frame is $(a, fa, state)$. When $state = 0$, push $(a, fa, 1)$ and then push every neighbor other than the parent with state $0$. When $state = 1$, merge $cost[a]$ with the already trimmed lists of the children and sort the result into $res$ of length $m$:

- If $m \ge 3$, the number of coins at $a$ is $\max(0, res[m - 1] \times res[m - 2] \times res[m - 3], res[0] \times res[1] \times res[m - 1])$; otherwise it stays $1$.
- If $m > 5$, keep only the first $2$ elements and the last $3$ elements of $res$ for the parent to merge.

The merged list is sorted again, so the order in which children are pushed does not change the answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = [1] * n
        sub = [None] * n
        stk = [(0, -1, 0)]
        while stk:
            a, fa, state = stk.pop()
            if state == 0:
                stk.append((a, fa, 1))
                for b in g[a]:
                    if b != fa:
                        stk.append((b, a, 0))
            else:
                res = [cost[a]]
                for b in g[a]:
                    if b != fa:
                        res.extend(sub[b])
                res.sort()
                if len(res) >= 3:
                    ans[a] = max(
                        res[-3] * res[-2] * res[-1], res[0] * res[1] * res[-1], 0
                    )
                if len(res) > 5:
                    res = res[:2] + res[-3:]
                sub[a] = res
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
