---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0572.Subtree%20of%20Another%20Tree/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Binary Tree
    - String Matching
    - Hash Function
---

<!-- problem:start -->

# [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree)

## Description

<!-- description:start -->

<p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values of<code> subRoot</code> and <code>false</code> otherwise.</p>

<p>A subtree of a binary tree <code>tree</code> is a tree that consists of a node in <code>tree</code> and all of this node&#39;s descendants. The tree <code>tree</code> could also be considered as a subtree of itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0572.Subtree%20of%20Another%20Tree/images/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0572.Subtree%20of%20Another%20Tree/images/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>root</code> tree is in the range <code>[1, 2000]</code>.</li>
	<li>The number of nodes in the <code>subRoot</code> tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We define a helper function $\textit{same}(p, q)$ to determine whether the tree rooted at $p$ and the tree rooted at $q$ are identical. If the root values of the two trees are equal, and their left and right subtrees are also respectively equal, then the two trees are identical.

In the $\textit{isSubtree}(\textit{root}, \textit{subRoot})$ function, we first check if $\textit{root}$ is null. If it is, we return $\text{false}$. Otherwise, we check if $\textit{root}$ and $\textit{subRoot}$ are identical. If they are, we return $\text{true}$. Otherwise, we recursively check if the left or right subtree of $\textit{root}$ contains $\textit{subRoot}$.

The time complexity is $O(n \times m)$, and the space complexity is $O(n)$. Here, $n$ and $m$ are the number of nodes in the trees $root$ and $subRoot$, respectively.

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None or q is None:
                return p is q
            return p.val == q.val and same(p.left, q.left) and same(p.right, q.right)

        if root is None:
            return False
        return (
            same(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
