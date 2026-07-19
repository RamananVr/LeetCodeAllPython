---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2876.Count%20Visited%20Nodes%20in%20a%20Directed%20Graph/README_EN.md
rating: 2209
source: Weekly Contest 365 Q4
tags:
    - Depth-First Search
    - Graph
    - Topological Sort
    - Memoization
    - Dynamic Programming
---

<!-- problem:start -->

# [2876. Count Visited Nodes in a Directed Graph](https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph)

## Description

<!-- description:start -->

<p>There is a <strong>directed</strong> graph consisting of <code>n</code> nodes numbered from <code>0</code> to <code>n - 1</code> and <code>n</code> directed edges.</p>

<p>You are given a <strong>0-indexed</strong> array <code>edges</code> where <code>edges[i]</code> indicates that there is an edge from node <code>i</code> to node <code>edges[i]</code>.</p>

<p>Consider the following process on the graph:</p>

<ul>
	<li>You start from a node <code>x</code> and keep visiting other nodes through edges until you reach a node that you have already visited before on this <strong>same</strong> process.</li>
</ul>

<p>Return <em>an array </em><code>answer</code><em> where </em><code>answer[i]</code><em> is the number of <strong>different</strong> nodes that you will visit if you perform the process starting from node </em><code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2876.Count%20Visited%20Nodes%20in%20a%20Directed%20Graph/images/graaphdrawio-1.png" />
<pre>
<strong>Input:</strong> edges = [1,2,0,0]
<strong>Output:</strong> [3,3,3,4]
<strong>Explanation:</strong> We perform the process starting from each node in the following way:
- Starting from node 0, we visit the nodes 0 -&gt; 1 -&gt; 2 -&gt; 0. The number of different nodes we visit is 3.
- Starting from node 1, we visit the nodes 1 -&gt; 2 -&gt; 0 -&gt; 1. The number of different nodes we visit is 3.
- Starting from node 2, we visit the nodes 2 -&gt; 0 -&gt; 1 -&gt; 2. The number of different nodes we visit is 3.
- Starting from node 3, we visit the nodes 3 -&gt; 0 -&gt; 1 -&gt; 2 -&gt; 0. The number of different nodes we visit is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2876.Count%20Visited%20Nodes%20in%20a%20Directed%20Graph/images/graaph2drawio.png" style="width: 191px; height: 251px;" />
<pre>
<strong>Input:</strong> edges = [1,2,3,4,0]
<strong>Output:</strong> [5,5,5,5,5]
<strong>Explanation:</strong> Starting from any node we can visit every node in the graph in the process.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges[i] &lt;= n - 1</code></li>
	<li><code>edges[i] != i</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Basic Tree + Traversal

We can use an array $ans$ to record the answer for each node, and an array $vis$ to record the visit order for each node.

For each node $i$, if it has not been visited yet, we start traversing from node $i$. There are two cases:

- If we encounter a node that has been visited before during the traversal, then we must have first entered the cycle and then walked around the cycle. For nodes outside the cycle, their answer is the length of the cycle plus the distance from the node to the cycle; for nodes inside the cycle, their answer is the length of the cycle.
- If we encounter a node that has been visited before during the traversal, then for each visited node, its answer is the distance from the current node to this node plus the answer of this node.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array edges.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        vis = [0] * n
        for i in range(n):
            if not ans[i]:
                cnt, j = 0, i
                while not vis[j]:
                    cnt += 1
                    vis[j] = cnt
                    j = edges[j]
                cycle, total = 0, cnt + ans[j]
                if not ans[j]:
                    cycle = cnt - vis[j] + 1
                    total = cnt
                j = i
                while not ans[j]:
                    ans[j] = max(total, cycle)
                    total -= 1
                    j = edges[j]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
