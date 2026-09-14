---
comments: true
difficulty: Hard
rating: 1797
source: Weekly Contest 132 Q4
tags:
    - Tree
    - Depth-First Search
    - String
    - Binary Tree
---

<!-- problem:start -->

# [1028. Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal)

## Description

<!-- description:start -->

<p>We run a&nbsp;preorder&nbsp;depth-first search (DFS) on the <code>root</code> of a binary tree.</p>

<p>At each node in this traversal, we output <code>D</code> dashes (where <code>D</code> is the depth of this node), then we output the value of this node.&nbsp; If the depth of a node is <code>D</code>, the depth of its immediate child is <code>D + 1</code>.&nbsp; The depth of the <code>root</code> node is <code>0</code>.</p>

<p>If a node has only one child, that child is guaranteed to be <strong>the left child</strong>.</p>

<p>Given the output <code>traversal</code> of this traversal, recover the tree and return <em>its</em> <code>root</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1028.Recover%20a%20Tree%20From%20Preorder%20Traversal/images/recover_tree_ex1.png" style="width: 423px; height: 200px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-2--3--4-5--6--7&quot;
<strong>Output:</strong> [1,2,5,3,4,6,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1028.Recover%20a%20Tree%20From%20Preorder%20Traversal/images/recover_tree_ex2.png" style="width: 432px; height: 250px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-2--3---4-5--6---7&quot;
<strong>Output:</strong> [1,2,5,3,null,6,null,4,null,7]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1028.Recover%20a%20Tree%20From%20Preorder%20Traversal/images/recover_tree_ex3.png" style="width: 305px; height: 250px;" />
<pre>
<strong>Input:</strong> traversal = &quot;1-401--349---90--88&quot;
<strong>Output:</strong> [1,401,null,349,88,90]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the original tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Splitting the traversal by depth and recursively attaching children builds the tree for $n\le 1000$, but the string is carved many times. In a depth-annotated preorder the parent of a new node is the nearest node whose depth is one smaller — the stack top after popping deeper nodes.
>
> We parse runs of `-` as depth and digits as values. Before pushing, nodes whose depth is not smaller are popped; the new node becomes the left or right child of the new top.
>
> The bottom of the stack is the root. Stack size is used as the current depth, matching the dashes in the string.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
