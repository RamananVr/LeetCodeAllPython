---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [742. Closest Leaf in a Binary Tree 🔒](https://leetcode.com/problems/closest-leaf-in-a-binary-tree)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree where every node has <strong>a unique value</strong> and a target integer <code>k</code>, return <em>the value of the <strong>nearest leaf node</strong> to the target </em><code>k</code><em> in the tree</em>.</p>

<p><strong>Nearest to a leaf</strong> means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/images/closest1-tree.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>Input:</strong> root = [1,3,2], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> Either 2 or 3 is the nearest leaf node to the target of 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/images/closest2-tree.jpg" style="width: 64px; height: 65px;" />
<pre>
<strong>Input:</strong> root = [1], k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The nearest leaf node is the root node itself.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree/images/closest3-tree.jpg" style="width: 464px; height: 384px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,null,null,null,5,null,6], k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
	<li>All the values of the tree are <strong>unique</strong>.</li>
	<li>There exist some node in the tree where <code>Node.val == k</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + BFS

First, we use depth-first search to construct an undirected graph $g$, where $g[node]$ represents the set of nodes adjacent to the node $node$. Then we start a breadth-first search from node $k$ until we find a leaf node, which is the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: Optional[TreeNode], fa: Optional[TreeNode]):
            if root:
                g[root].append(fa)
                g[fa].append(root)
                dfs(root.left, root)
                dfs(root.right, root)

        g = defaultdict(list)
        dfs(root, None)
        q = deque(node for node in g if node and node.val == k)
        vis = set(q)
        while 1:
            node = q.popleft()
            if node:
                if node.left == node.right:
                    return node.val
                for nxt in g[node]:
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
