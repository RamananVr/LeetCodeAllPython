---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0865.Smallest%20Subtree%20with%20all%20the%20Deepest%20Nodes/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Hash Table
    - Binary Tree
---

<!-- problem:start -->

# [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, the depth of each node is <strong>the shortest distance to the root</strong>.</p>

<p>Return <em>the smallest subtree</em> such that it contains <strong>all the deepest nodes</strong> in the original tree.</p>

<p>A node is called <strong>the deepest</strong> if it has the largest depth possible among any node in the entire tree.</p>

<p>The <strong>subtree</strong> of a node is a tree consisting of that node, plus the set of all descendants of that node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0865.Smallest%20Subtree%20with%20all%20the%20Deepest%20Nodes/images/sketch1.png" style="width: 600px; height: 510px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4]
<strong>Output:</strong> [2,7,4]
<strong>Explanation:</strong> We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The root is the deepest node in the tree.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [0,1,3,null,2]
<strong>Output:</strong> [2]
<strong>Explanation:</strong> The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>The values of the nodes in the tree are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1123: <a href="https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/" target="_blank">https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/</a></p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

We design a function $\textit{dfs}(\textit{root})$ that returns the smallest subtree containing all the deepest nodes in the subtree rooted at $\textit{root}$, as well as the depth of the subtree rooted at $\textit{root}$.

The execution process of the function $\textit{dfs}(\textit{root})$ is as follows:

- If $\textit{root}$ is null, return $\text{null}$ and $0$.
- Otherwise, recursively calculate the smallest subtree and depth of the left and right subtrees of $\textit{root}$, denoted as $l$ and $l_d$, and $r$ and $r_d$, respectively. If $l_d > r_d$, then the smallest subtree containing all the deepest nodes in the subtree rooted at the left child of $\textit{root}$ is $l$, with a depth of $l_d + 1$. If $l_d < r_d$, then the smallest subtree containing all the deepest nodes in the subtree rooted at the right child of $\textit{root}$ is $r$, with a depth of $r_d + 1$. If $l_d = r_d$, then $\textit{root}$ is the smallest subtree containing all the deepest nodes, with a depth of $l_d + 1$.

Finally, return the first element of the result of $\textit{dfs}(\textit{root})$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if root is None:
                return None, 0
            l, ld = dfs(root.left)
            r, rd = dfs(root.right)
            if ld > rd:
                return l, ld + 1
            if ld < rd:
                return r, rd + 1
            return root, ld + 1

        return dfs(root)[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
