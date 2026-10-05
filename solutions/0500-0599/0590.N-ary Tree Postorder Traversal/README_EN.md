---
comments: true
difficulty: Easy
tags:
    - Stack
    - Tree
    - Depth-First Search
---

<!-- problem:start -->

# [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of an n-ary tree, return <em>the postorder traversal of its nodes&#39; values</em>.</p>

<p>Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0590.N-ary%20Tree%20Postorder%20Traversal/images/narytreeexample.png" style="width: 100%; max-width: 300px;" />
<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [5,6,3,2,4,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0590.N-ary%20Tree%20Postorder%20Traversal/images/sample_4_964.png" style="width: 296px; height: 241px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
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
> N-ary postorder is children left to right, then the root. Recursion visits children first.
>
> Recurse on each child, then append the root. An empty tree yields an empty list.

<!-- thinking:end -->

We can recursively traverse the entire tree. For each node, we first recursively call the function for each of the node's children, then add the node's value to the answer.

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
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if root is None:
                return
            for child in root.children:
                dfs(child)
            ans.append(root.val)

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
> Solution 1 already records the root and pushes children from left to right, then reverses the list into postorder.
>
> This section is the same walk. Pop a node, record it, push children left to right, and reverse the answer.

<!-- thinking:end -->

This section uses the same explicit stack.

We use a stack to help us get the post-order traversal. We first push the root node into the stack. Since the post-order traversal is left subtree, right subtree, root, and the characteristic of the stack is first in last out, we first add the node's value to the answer, then push each of the node's children into the stack in the order from left to right. This way, we can get the traversal result of root, right subtree, left subtree. Finally, we reverse the answer to get the post-order traversal result.

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
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            for child in node.children:
                stk.append(child)
        return ans[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> N-ary postorder records children from left to right, then the root. Recursion on a chain of height $1000$ exhausts the call stack, and $1000$ is the height limit.
>
> The bottleneck is that chain: the child is visited before the root returns, so the depth tracks the height.
>
> Recording the root and pushing children from left to right produces root-right-left. Reversing that list is left-right-root.
>
> An explicit stack does that walk. Pop a node, append its value, push its children from left to right, then reverse the answer. An empty tree returns an empty list.

<!-- thinking:end -->

Simulate postorder with a stack. Push the root, and after popping a node append its value, then push its children from left to right. Reverse the answer to obtain left, right, root order.

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
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            for child in node.children:
                stk.append(child)
        return ans[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
