---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0897.Increasing%20Order%20Search%20Tree/README_EN.md
tags:
    - Stack
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Binary Tree
---

<!-- problem:start -->

# [897. Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary search tree, rearrange the tree in <strong>in-order</strong> so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0897.Increasing%20Order%20Search%20Tree/images/ex1.jpg" style="width: 600px; height: 350px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0897.Increasing%20Order%20Search%20Tree/images/ex2.jpg" style="width: 300px; height: 114px;" />
<pre>
<strong>Input:</strong> root = [5,1,7]
<strong>Output:</strong> [1,null,5,null,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree will be in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS In-order Traversal

We define a virtual node $dummy$, initially the right child of $dummy$ points to the root node $root$, and a pointer $prev$ points to $dummy$.

We perform an in-order traversal on the binary search tree. During the traversal, each time we visit a node, we point the right child of $prev$ to it, then set the left child of the current node to null, and assign the current node to $prev$ for the next traversal.

After the traversal ends, the original binary search tree is modified into a singly linked list with only right child nodes. We then return the right child of the virtual node $dummy$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary search tree.

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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root is None:
                return
            nonlocal prev
            dfs(root.left)
            prev.right = root
            root.left = None
            prev = root
            dfs(root.right)

        dummy = prev = TreeNode(right=root)
        dfs(root)
        return dummy.right
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
