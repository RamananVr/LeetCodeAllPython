---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1373.Maximum%20Sum%20BST%20in%20Binary%20Tree/README_EN.md
rating: 1913
source: Biweekly Contest 21 Q4
tags:
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Dynamic Programming
    - Binary Tree
---

<!-- problem:start -->

# [1373. Maximum Sum BST in Binary Tree](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree)

## Description

<!-- description:start -->

<p>Given a <strong>binary tree</strong> <code>root</code>, return <em>the maximum sum of all keys of <strong>any</strong> sub-tree which is also a Binary Search Tree (BST)</em>.</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1373.Maximum%20Sum%20BST%20in%20Binary%20Tree/images/sample_1_1709.png" style="width: 320px; height: 250px;" /></p>

<pre>
<strong>Input:</strong> root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
<strong>Output:</strong> 20
<strong>Explanation:</strong> Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1373.Maximum%20Sum%20BST%20in%20Binary%20Tree/images/sample_2_1709.png" style="width: 134px; height: 180px;" /></p>

<pre>
<strong>Input:</strong> root = [4,3,null,1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [-4,-2,-5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All values are negatives. Return an empty BST.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 4 * 10<sup>4</sup>]</code>.</li>
	<li><code>-4 * 10<sup>4</sup> &lt;= Node.val &lt;= 4 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

To determine whether a tree is a binary search tree, it needs to meet the following four conditions:

- The left subtree is a binary search tree;
- The right subtree is a binary search tree;
- The maximum value of the left subtree is less than the value of the root node;
- The minimum value of the right subtree is greater than the value of the root node.

Therefore, we design a function $dfs(root)$, the return value of the function is a quadruple $(bst, mi, mx, s)$, where:

- The number $bst$ indicates whether the tree with $root$ as the root is a binary search tree. If it is a binary search tree, then $bst = 1$; otherwise $bst = 0$;
- The number $mi$ represents the minimum value of the tree with $root$ as the root;
- The number $mx$ represents the maximum value of the tree with $root$ as the root;
- The number $s$ represents the sum of all nodes of the tree with $root$ as the root.

The execution logic of the function $dfs(root)$ is as follows:

If $root$ is an empty node, return $(1, +\infty, -\infty, 0)$, indicating that the empty tree is a binary search tree, the minimum value and maximum value are positive infinity and negative infinity respectively, and the sum of nodes is $0$.

Otherwise, recursively calculate the left subtree and right subtree of $root$, and get $(lbst, lmi, lmx, ls)$ and $(rbst, rmi, rmx, rs)$ respectively, then judge whether the $root$ node meets the conditions of the binary search tree.

If $lbst = 1$ and $rbst = 1$ and $lmx < root.val < rmi$, then the tree with $root$ as the root is a binary search tree, and the sum of nodes $s= ls + rs + root.val$. We update the answer $ans = \max(ans, s)$, and return $(1, \min(lmi, root.val), \max(rmx, root.val), s)$.

Otherwise, the tree with $root$ as the root is not a binary search tree, we return $(0, 0, 0, 0)$.

We call $dfs(root)$ in the main function. After execution, the answer is $ans$.

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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> tuple:
            if root is None:
                return 1, inf, -inf, 0
            lbst, lmi, lmx, ls = dfs(root.left)
            rbst, rmi, rmx, rs = dfs(root.right)
            if lbst and rbst and lmx < root.val < rmi:
                nonlocal ans
                s = ls + rs + root.val
                ans = max(ans, s)
                return 1, min(lmi, root.val), max(rmx, root.val), s
            return 0, 0, 0, 0

        ans = 0
        dfs(root)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
