---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0919.Complete%20Binary%20Tree%20Inserter/README_EN.md
tags:
    - Tree
    - Breadth-First Search
    - Design
    - Binary Tree
---

<!-- problem:start -->

# [919. Complete Binary Tree Inserter](https://leetcode.com/problems/complete-binary-tree-inserter)

## Description

<!-- description:start -->

<p>A <strong>complete binary tree</strong> is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.</p>

<p>Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.</p>

<p>Implement the <code>CBTInserter</code> class:</p>

<ul>
	<li><code>CBTInserter(TreeNode root)</code> Initializes the data structure with the <code>root</code> of the complete binary tree.</li>
	<li><code>int insert(int v)</code> Inserts a <code>TreeNode</code> into the tree with value <code>Node.val == val</code> so that the tree remains complete, and returns the value of the parent of the inserted <code>TreeNode</code>.</li>
	<li><code>TreeNode get_root()</code> Returns the root node of the tree.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0919.Complete%20Binary%20Tree%20Inserter/images/lc-treeinsert.jpg" style="width: 500px; height: 143px;" />
<pre>
<strong>Input</strong>
[&quot;CBTInserter&quot;, &quot;insert&quot;, &quot;insert&quot;, &quot;get_root&quot;]
[[[1, 2]], [3], [4], []]
<strong>Output</strong>
[null, 1, 2, [1, 2, 3, 4]]

<strong>Explanation</strong>
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3); // return 1
cBTInserter.insert(4); // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 5000</code></li>
	<li><code>root</code> is a complete binary tree.</li>
	<li><code>0 &lt;= val &lt;= 5000</code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>insert</code> and <code>get_root</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

We can use an array $tree$ to store all nodes of the complete binary tree. During initialization, we use a queue $q$ to perform level-order traversal of the given tree and store all nodes into the array $tree$.

When inserting a node, we can find the parent node $p$ of the new node through the array $tree$. Then we create a new node $node$, insert it into the array $tree$, and make $node$ as the left child or right child of $p$. Finally, we return the value of $p$.

When getting the root node, we directly return the first element of the array $tree$.

In terms of time complexity, it takes $O(n)$ time for initialization, and the time complexity for inserting a node and getting the root node are both $O(1)$. The space complexity is $O(n)$, where $n$ is the number of nodes in the tree.

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                self.tree.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    def insert(self, val: int) -> int:
        p = self.tree[(len(self.tree) - 1) // 2]
        node = TreeNode(val)
        self.tree.append(node)
        if p.left is None:
            p.left = node
        else:
            p.right = node
        return p.val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
