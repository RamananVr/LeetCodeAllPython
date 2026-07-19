---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0105.Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/README_EN.md
tags:
    - Tree
    - Array
    - Hash Table
    - Divide and Conquer
    - Binary Tree
---

<!-- problem:start -->

# [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

## Description

<!-- description:start -->

<p>Given two integer arrays <code>preorder</code> and <code>inorder</code> where <code>preorder</code> is the preorder traversal of a binary tree and <code>inorder</code> is the inorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0105.Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/images/tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code> and <code>inorder</code> consist of <strong>unique</strong> values.</li>
	<li>Each value of <code>inorder</code> also appears in <code>preorder</code>.</li>
	<li><code>preorder</code> is <strong>guaranteed</strong> to be the preorder traversal of the tree.</li>
	<li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Recursion

The first node $preorder[0]$ in the pre-order sequence is the root node. We find the position $k$ of the root node in the in-order sequence, which can divide the in-order sequence into the left subtree $inorder[0..k]$ and the right subtree $inorder[k+1..]$.

Through the intervals of the left and right subtrees, we can calculate the number of nodes in the left and right subtrees, assumed to be $a$ and $b$. Then in the pre-order nodes, the $a$ nodes after the root node are the left subtree, and the $b$ nodes after that are the right subtree.

Therefore, we design a function $dfs(i, j, n)$, where $i$ and $j$ represent the starting positions of the pre-order sequence and the in-order sequence, respectively, and $n$ represents the number of nodes. The return value of the function is the binary tree constructed with $preorder[i..i+n-1]$ as the pre-order sequence and $inorder[j..j+n-1]$ as the in-order sequence.

The execution process of the function $dfs(i, j, n)$ is as follows:

- If $n \leq 0$, it means there are no nodes, return a null node.
- Take out the first node $v = preorder[i]$ of the pre-order sequence as the root node, and then use the hash table $d$ to find the position $k$ of the root node in the in-order sequence. Then the number of nodes in the left subtree is $k - j$, and the number of nodes in the right subtree is $n - k + j - 1$.
- Recursively construct the left subtree $l = dfs(i + 1, j, k - j)$ and the right subtree $r = dfs(i + 1 + k - j, k + 1, n - k + j - 1)$.
- Finally, return the binary tree with $v$ as the root node and $l$ and $r$ as the left and right subtrees, respectively.

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0:
                return None
            v = preorder[i]
            k = d[v]
            l = dfs(i + 1, j, k - j)
            r = dfs(i + 1 + k - j, k + 1, n - k + j - 1)
            return TreeNode(v, l, r)

        d = {v: i for i, v in enumerate(inorder)}
        return dfs(0, 0, len(preorder))
```

<!-- tabs:end -->

If the node values given in the problem have duplicates, then we only need to record all the positions where each node value appears, and then recursively construct the tree.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getBinaryTrees(self, preOrder: List[int], inOrder: List[int]) -> List[TreeNode]:
        def dfs(i: int, j: int, n: int) -> List[TreeNode]:
            if n <= 0:
                return [None]
            v = preOrder[i]
            ans = []
            for k in d[v]:
                if j <= k < j + n:
                    for l in dfs(i + 1, j, k - j):
                        for r in dfs(i + 1 + k - j, k + 1, n - 1 - (k - j)):
                            ans.append(TreeNode(v, l, r))
            return ans

        d = defaultdict(list)
        for i, x in enumerate(inOrder):
            d[x].append(i)
        return dfs(0, 0, len(preOrder))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
