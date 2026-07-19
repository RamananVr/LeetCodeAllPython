---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0145.Binary%20Tree%20Postorder%20Traversal/README_EN.md
tags:
    - Stack
    - Tree
    - Depth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a&nbsp;binary tree, return <em>the postorder traversal of its nodes&#39; values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,null,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2,1]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0145.Binary%20Tree%20Postorder%20Traversal/images/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,6,7,5,2,9,8,3,1]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0145.Binary%20Tree%20Postorder%20Traversal/images/tree_2.png" style="width: 350px; height: 286px;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = []</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

We first recursively traverse the left and right subtrees, then visit the root node.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree. The space complexity mainly depends on the stack space used for recursive calls.

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        ans = []
        dfs(root)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Stack Implementation for Postorder Traversal

The order of preorder traversal is: root, left, right. If we change the order of the left and right children, the order becomes: root, right, left. Finally, reversing the result gives us the postorder traversal result.

Therefore, the idea of using a stack to implement non-recursive traversal is as follows:

1. Define a stack $stk$, and first push the root node into the stack.
2. If the stack is not empty, pop a node from the stack each time.
3. Process the node.
4. First push the left child of the node into the stack, then push the right child of the node into the stack (if there are child nodes).
5. Repeat steps 2-4.
6. Reverse the result to get the postorder traversal result.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree. The space complexity mainly depends on the stack space.

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return ans[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Morris Implementation for Postorder Traversal

Morris traversal does not require a stack, and its space complexity is $O(1)$. The core idea is:

Traverse the binary tree nodes,

1. If the right subtree of the current node `root` is empty, add the current node value to the result list $ans$, and update the current node to `root.left`.
1. If the right subtree of the current node `root` is not empty, find the leftmost node `next` of the right subtree (which is the successor of the `root` node in inorder traversal):
    - If the left subtree of the successor node `next` is empty, add the current node value to the result list $ans$, then point the left subtree of the successor node to the current node `root`, and update the current node to `root.right`.
    - If the left subtree of the successor node `next` is not empty, point the left subtree of the successor node to null (i.e., disconnect `next` and `root`), and update the current node to `root.left`.
1. Repeat the above steps until the binary tree node is null, and the traversal ends.
1. Finally, return the reverse of the result list.

> The idea of Morris postorder traversal is consistent with Morris preorder traversal, just change the "root-left-right" of preorder to "root-right-left", and finally reverse the result to become "left-right-root".

The time complexity is $O(n)$, where $n$ is the number of nodes in the binary tree. The space complexity is $O(1)$.

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.right is None:
                ans.append(root.val)
                root = root.left
            else:
                next = root.right
                while next.left and next.left != root:
                    next = next.left
                if next.left != root:
                    ans.append(root.val)
                    next.left = root
                    root = root.right
                else:
                    next.left = None
                    root = root.left
        return ans[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
