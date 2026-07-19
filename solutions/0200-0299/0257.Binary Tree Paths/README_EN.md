---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0257.Binary%20Tree%20Paths/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - String
    - Backtracking
    - Binary Tree
---

<!-- problem:start -->

# [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>all root-to-leaf paths in <strong>any order</strong></em>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0257.Binary%20Tree%20Paths/images/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,5]
<strong>Output:</strong> [&quot;1-&gt;2-&gt;5&quot;,&quot;1-&gt;3&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [&quot;1&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

## Solution 1: DFS

We can use depth-first search to traverse the entire binary tree. Each time, we add the current node to the path. If the current node is a leaf node, we add the entire path to the answer. Otherwise, we continue to recursively traverse the child nodes of the node. Finally, when the recursion ends and returns to the current node, we need to remove the current node from the path.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes in the binary tree.

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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            t.append(str(root.val))
            if root.left is None and root.right is None:
                ans.append("->".join(t))
            else:
                dfs(root.left)
                dfs(root.right)
            t.pop()

        ans = []
        t = []
        dfs(root)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
