---
comments: true
difficulty: Medium
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Search Tree
    - Binary Tree
---

<!-- problem:start -->

# [3831. Median of a Binary Search Tree Level 🔒](https://leetcode.com/problems/median-of-a-binary-search-tree-level)

## Description

<!-- description:start -->

<p>You are given the <code>root</code> of a <strong>Binary Search Tree (BST)</strong> and an integer <code>level</code>.</p>

<p>The root node is at level 0. Each level represents the distance from the root.</p>

<p>Return the <strong>median value</strong> of all node values present at the given <code>level</code>. If the level does not exist or contains no nodes, return -1.</p>

<p>The <strong>median</strong> is defined as the middle element after sorting the values at that level in <strong>non-decreasing</strong> order. If the number of values at that level is even, return the <strong>upper</strong> median (the larger of the two middle elements after sorting).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3800-3899/3831.Median%20of%20a%20Binary%20Search%20Tree%20Level/images/screenshot-2026-01-27-at-20801pm.png" style="width: 180px; height: 182px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [4,null,5,null,7], level = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The nodes at <code>level = 2</code> are <code>[7]</code>. The median value is 7.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3800-3899/3831.Median%20of%20a%20Binary%20Search%20Tree%20Level/images/screenshot-2026-01-27-at-20926pm.png" style="width: 200px; height: 169px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [6,3,8], level = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The nodes at <code>level = 1</code> are <code>[3, 8]</code>. There are two possible median values, so the larger one 8 is the answer.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<p><strong class="example">​​​​​​​​​​​​​​</strong><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3800-3899/3831.Median%20of%20a%20Binary%20Search%20Tree%20Level/images/screenshot-2026-01-27-at-21001pm.png" style="width: 150px; height: 193px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [2,1], level = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no node present at <code>level = 2</code>​​​​​​​, so the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2 * 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= level &lt;= 2 * 10<sup>​​​​​​​5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

<!-- thinking:start -->

> **Thinking**
>
> We need the median of a given BST level, taking the upper middle on even counts. A level may hold $O(n)$ nodes with $n \le 2 \times 10^5$.
>
> Collecting then sorting is unnecessary: inorder of a BST is sorted, so the inorder subsequence of that level is already ordered.
>
> An inorder DFS appends a value only when the depth equals $\textit{level}$.
>
> The median is $\textit{nums}[\lfloor |\textit{nums}|/2 \rfloor]$; an empty level yields $-1$.

<!-- thinking:end -->

We notice that the problem requires us to find the median of node values at a certain level in a binary search tree. Since the definition of median is to sort the node values and take the middle value, and the in-order traversal of a binary search tree is inherently sorted, we can collect the node values at the specified level through in-order traversal.

We define a helper function $\text{dfs}(root, i)$, where $root$ is the current node and $i$ is the level of the current node. In the function, if the current node is empty, we return directly. Otherwise, we recursively traverse the left subtree, check if the level of the current node equals the target level, and if so, add the value of the current node to the result list, and finally recursively traverse the right subtree.

We initialize an empty list $\text{nums}$ to store the node values at the specified level, and call $\text{dfs}(root, 0)$ to start the traversal. Finally, we check if $\text{nums}$ is empty, and if so, return -1, otherwise return the value at the middle position of $\text{nums}$.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the number of nodes in the tree.

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
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        def dfs(root: Optional[TreeNode], i: int):
            if root is None:
                return
            dfs(root.left, i + 1)
            if i == level:
                nums.append(root.val)
            dfs(root.right, i + 1)

        nums = []
        dfs(root, 0)
        return nums[len(nums) // 2] if nums else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Explicit-Stack Inorder

<!-- thinking:start -->

> **Thinking**
>
> The median of one BST level takes the upper middle value when the count is even. Collecting that level and sorting it is correct, and $n$ can be $2 \times 10^5$.
>
> Inorder visits the left child first. A chain of that length recurses once per node and overflows the call stack.
>
> Inorder of a BST is already nondecreasing, so the values of the chosen level appear in sorted order and do not need another sort. A node only needs its own depth.
>
> An explicit stack performs the inorder walk. On entry it pushes an exit marker and the left child; on exit, a node whose depth equals $\textit{level}$ is appended, and then the right child is pushed. The median is $\textit{nums}[\lfloor |\textit{nums}|/2 \rfloor]$, or $-1$ when the level is empty.

<!-- thinking:end -->

The median is a sorted middle value, and an inorder walk of a binary search tree is already sorted, so the values on the requested level can be collected in that order. When the count is even, index $\lfloor |\textit{nums}|/2 \rfloor$ is the larger of the two middle values.

An explicit stack carries the current node, its depth, and whether its left subtree has been expanded. On entry we push an exit marker and the left child. On exit, if the depth equals $\textit{level}$, the node value is appended to $\textit{nums}$, and then the right child is pushed.

An empty $\textit{nums}$ returns $-1$; otherwise the middle entry is the answer.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the number of nodes in the tree.

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
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        nums = []
        stk = [(root, 0, 0)]
        while stk:
            node, i, state = stk.pop()
            if node is None:
                continue
            if state == 0:
                stk.append((node, i, 1))
                stk.append((node.left, i + 1, 0))
                continue
            if i == level:
                nums.append(node.val)
            stk.append((node.right, i + 1, 0))
        return nums[len(nums) // 2] if nums else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
