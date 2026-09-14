---
comments: true
difficulty: Medium
rating: 1804
source: Weekly Contest 140 Q3
tags:
    - Tree
    - Depth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [1080. Insufficient Nodes in Root to Leaf Paths](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree and an integer <code>limit</code>, delete all <strong>insufficient nodes</strong> in the tree simultaneously, and return <em>the root of the resulting binary tree</em>.</p>

<p>A node is <strong>insufficient</strong> if every root to <strong>leaf</strong> path intersecting this node has a sum strictly less than <code>limit</code>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1080.Insufficient%20Nodes%20in%20Root%20to%20Leaf%20Paths/images/insufficient-11.png" style="width: 500px; height: 207px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
<strong>Output:</strong> [1,2,3,4,null,null,7,8,9,null,14]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1080.Insufficient%20Nodes%20in%20Root%20to%20Leaf%20Paths/images/insufficient-3.png" style="width: 400px; height: 274px;" />
<pre>
<strong>Input:</strong> root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
<strong>Output:</strong> [5,4,8,11,null,17,4,7,null,null,null,5]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1080.Insufficient%20Nodes%20in%20Root%20to%20Leaf%20Paths/images/screen-shot-2019-06-11-at-83301-pm.png" style="width: 250px; height: 199px;" />
<pre>
<strong>Input:</strong> root = [1,2,-3,-5,null,4,null], limit = -1
<strong>Output:</strong> [1,null,-3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 5000]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= limit &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Nodes that lie only on root-to-leaf paths summing to less than $\textit{limit}$ must go. A path is decided at the leaf; a parent stays only if a child survives. $n\le 5000$ allows one postorder.
>
> Descending subtracts the current value from $\textit{limit}$. A leaf is removed when the remainder is still positive. An internal node is removed only after both children become null.
>
> The call returns the new subtree root, which may be empty.

<!-- thinking:end -->

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
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None
        limit -= root.val
        if root.left is None and root.right is None:
            return None if limit > 0 else root
        root.left = self.sufficientSubset(root.left, limit)
        root.right = self.sufficientSubset(root.right, limit)
        return None if root.left is None and root.right is None else root
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
