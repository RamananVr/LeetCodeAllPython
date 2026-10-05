---
comments: true
difficulty: Easy
tags:
    - Stack
    - Tree
    - Depth-First Search
---

<!-- problem:start -->

# [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of an n-ary tree, return <em>the preorder traversal of its nodes&#39; values</em>.</p>

<p>Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0589.N-ary%20Tree%20Preorder%20Traversal/images/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [1,3,5,6,2,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0589.N-ary%20Tree%20Preorder%20Traversal/images/sample_4_964.png" style="width: 296px; height: 241px;" /></p>

<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The height of the n-ary tree is less than or equal to <code>1000</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

<!-- thinking:start -->

> **Thinking**
>
> N-ary preorder is the root, then children from left to right. Recursion matches the definition.
>
> Append the root, then recurse on each child. An empty tree yields an empty list. Each node is visited once.

<!-- thinking:end -->

We can recursively traverse the entire tree. For each node, we first add the node's value to the answer, then recursively call the function for each of the node's children.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: "Node") -> List[int]:
        def dfs(root):
            if root is None:
                return
            ans.append(root.val)
            for child in root.children:
                dfs(child)

        ans = []
        dfs(root)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Iteration (Stack Implementation)

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 already walks preorder with an explicit stack, pushing children from right to left so the leftmost child pops first.
>
> This section is the same walk. Pop a node, record it, then push its children in reverse. The order matches the preorder definition.

<!-- thinking:end -->

This section uses the same explicit stack.

We use a stack to help us get the pre-order traversal. We first push the root node into the stack. Since the pre-order traversal is root, left subtree, right subtree, and the characteristic of the stack is first in last out, we first add the node's value to the answer, then push each of the node's children into the stack in the order from right to left. We continue this process until the stack is empty.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            for child in node.children[::-1]:
                stk.append(child)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> N-ary preorder records the root, then the children from left to right. Recursion on a chain of height $1000$ exhausts the call stack, and $1000$ is the height limit.
>
> The bottleneck is that chain: each call steps into the single next child, so the depth tracks the height.
>
> Preorder records the current node before visiting children, so the walk does not wait for a child to return.
>
> An explicit stack holds the nodes still to visit. Pop a node, append its value, then push its children from right to left so the leftmost child pops first. An empty tree returns an empty list.

<!-- thinking:end -->

Simulate preorder with a stack. Push the root, and after popping a node append its value, then push its children from right to left until the stack is empty.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

<!-- tabs:start -->

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            for child in node.children[::-1]:
                stk.append(child)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
