---
comments: true
difficulty: Easy
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Search Tree
    - Hash Table
    - Two Pointers
    - Binary Tree
---

<!-- problem:start -->

# [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary search tree and an integer <code>k</code>, return <code>true</code> <em>if there exist two elements in the BST such that their sum is equal to</em> <code>k</code>, <em>or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0653.Two%20Sum%20IV%20-%20Input%20is%20a%20BST/images/sum_tree_1.jpg" style="width: 400px; height: 229px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 9
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0653.Two%20Sum%20IV%20-%20Input%20is%20a%20BST/images/sum_tree_2.jpg" style="width: 400px; height: 229px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 28
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>root</code> is guaranteed to be a <strong>valid</strong> binary search tree.</li>
	<li><code>-10<sup>5</sup> &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Find two nodes summing to $k$. Inorder plus two pointers works after collecting values.
>
> A set of seen values during a walk is enough: if $k-val$ is present, return true. The BST order is not required.

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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root):
            if root is None:
                return False
            if k - root.val in vis:
                return True
            vis.add(root.val)
            return dfs(root.left) or dfs(root.right)

        vis = set()
        return dfs(root)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> DFS can be replaced by BFS with the same seen-set test; only the traversal order changes.

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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        vis = set()
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if k - node.val in vis:
                    return True
                vis.add(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Hash Set and Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> Find two nodes whose values sum to $k$. Inorder plus two pointers works after collecting every value. A set of values already seen is enough: if $k$ minus the current value is present, return true. On a short tree one depth-first walk does this, and the BST order is not required.
>
> The tree can contain $10^4$ nodes. A left chain makes this walk recurse once per node and overflow the call stack.
>
> Each node depends only on values already visited. The children do not need to return before the node is checked.
>
> An explicit stack keeps that depth-first order. Pop a node, test $k$ minus its value, then store the value and push the right child and the left child. The set belongs to this call only.

<!-- thinking:end -->

A hash set stores values already visited, and an explicit stack walks the tree depth-first. When a node is popped, return true if $k$ minus its value is already in the set. Otherwise store the value and push the non-null right child and left child.

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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vis = set()
        stk = []
        if root is not None:
            stk.append(root)
        while stk:
            node = stk.pop()
            if k - node.val in vis:
                return True
            vis.add(node.val)
            if node.right is not None:
                stk.append(node.right)
            if node.left is not None:
                stk.append(node.left)
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
