---
comments: true
difficulty: Medium
tags:
    - Tree
    - Breadth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0102.Binary%20Tree%20Level%20Order%20Traversal/images/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

<!-- thinking:start -->

> **Thinking**
>
> We must emit values level by level. DFS can record depth and group later, but then left-to-right order needs extra work. $n \le 2000$, and a level holds at most $O(n)$ nodes.
>
> BFS expands by level: the nodes currently in the queue are exactly one level. Dequeue them, collect values, and enqueue children to form the next level from left to right.

<!-- thinking:end -->

We can use the BFS method to solve this problem. First, enqueue the root node, then continuously perform the following operations until the queue is empty:

- Traverse all nodes in the current queue, store their values in a temporary array $t$, and then enqueue their child nodes.
- Store the temporary array $t$ in the answer array.

Finally, return the answer array.

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        while q:
            t = []
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
