---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0404.Sum%20of%20Left%20Leaves/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>the sum of all left leaves.</em></p>

<p>A <strong>leaf</strong> is a node with no children. A <strong>left leaf</strong> is a leaf that is the left child of another node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0404.Sum%20of%20Left%20Leaves/images/leftsum-tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 24
<strong>Explanation:</strong> There are two left leaves in the binary tree, with values 9 and 15 respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

First, we check if `root` is null. If it is, we return $0$.

Otherwise, we recursively call the `sumOfLeftLeaves` function to calculate the sum of all left leaves in `root`'s right subtree, and assign the result to the answer variable $ans$. Then we check if `root`'s left child exists. If it does, we check if it is a leaf node. If it is a leaf node, we add its value to the answer variable $ans$. Otherwise, we recursively call the `sumOfLeftLeaves` function to calculate the sum of all left leaves in `root`'s left subtree, and add the result to the answer variable $ans$.

Finally, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = self.sumOfLeftLeaves(root.right)
        if root.left:
            if root.left.left == root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Stack

We can also convert the recursion in Solution 1 to iteration, using a stack to simulate the recursion process.

Similar to Solution 1, we first check if `root` is null. If it is, we return $0$.

Otherwise, we initialize the answer variable $ans$ to $0$, and then initialize a stack $stk$ and add `root` to the stack.

While the stack is not empty, we pop the top element `root` from the stack. If `root`'s left child exists, we check if it is a leaf node. If it is a leaf node, we add its value to the answer variable $ans$. Otherwise, we add its left child to the stack. Then we check if `root`'s right child exists. If it does, we add it to the stack.

Finally, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = 0
        stk = [root]
        while stk:
            root = stk.pop()
            if root.left:
                if root.left.left == root.left.right:
                    ans += root.left.val
                else:
                    stk.append(root.left)
            if root.right:
                stk.append(root.right)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
