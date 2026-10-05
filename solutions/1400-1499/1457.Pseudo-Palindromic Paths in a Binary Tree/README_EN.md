---
comments: true
difficulty: Medium
rating: 1405
source: Weekly Contest 190 Q3
tags:
    - Bit Manipulation
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [1457. Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree)

## Description

<!-- description:start -->

<p>Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be <strong>pseudo-palindromic</strong> if at least one permutation of the node values in the path is a palindrome.</p>

<p><em>Return the number of <strong>pseudo-palindromic</strong> paths going from the root node to leaf nodes.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1457.Pseudo-Palindromic%20Paths%20in%20a%20Binary%20Tree/images/palindromic_paths_1.png" style="width: 300px; height: 201px;" /></p>

<pre>
<strong>Input:</strong> root = [2,3,1,3,1,null,1]
<strong>Output:</strong> 2 
<strong>Explanation:</strong> The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1457.Pseudo-Palindromic%20Paths%20in%20a%20Binary%20Tree/images/palindromic_paths_2.png" style="width: 300px; height: 314px;" /></strong></p>

<pre>
<strong>Input:</strong> root = [2,1,1,1,3,null,null,null,null,null,1]
<strong>Output:</strong> 1 
<strong>Explanation:</strong> The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [9]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 9</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + Bit Manipulation

<!-- thinking:start -->

> **Thinking**
>
> A path is pseudo-palindromic iff at most one value occurs an odd number of times. Values are $1$– $9$ and $n\le 10^5$, so XOR a 10-bit mask along the path.
>
> At a leaf, count the path when $mask$ has at most one bit set. Recurse with the updated mask and sum both children.

<!-- thinking:end -->

A path is a pseudo-palindromic path if and only if the number of nodes with odd occurrences in the path is $0$ or $1$.

Since the range of the binary tree node values is from $1$ to $9$, for each path from root to leaf, we can use a $10$-bit binary number $mask$ to represent the occurrence status of the node values in the current path. The $i$th bit of $mask$ is $1$ if the node value $i$ appears an odd number of times in the current path, and $0$ if it appears an even number of times. Therefore, a path is a pseudo-palindromic path if and only if $mask \&(mask - 1) = 0$, where $\&$ represents the bitwise AND operation.

Based on the above analysis, we can use the depth-first search method to calculate the number of paths. We define a function $dfs(root, mask)$, which represents the number of pseudo-palindromic paths starting from the current $root$ node and with the current state $mask$. The answer is $dfs(root, 0)$.

The execution logic of the function $dfs(root, mask)$ is as follows:

If $root$ is null, return $0$;

Otherwise, let $mask = mask \oplus 2^{root.val}$, where $\oplus$ represents the bitwise XOR operation.

If $root$ is a leaf node, return $1$ if $mask \&(mask - 1) = 0$, otherwise return $0$;

If $root$ is not a leaf node, return $dfs(root.left, mask) + dfs(root.right, mask)$.

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
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], mask: int):
            if root is None:
                return 0
            mask ^= 1 << root.val
            if root.left is None and root.right is None:
                return int((mask & (mask - 1)) == 0)
            return dfs(root.left, mask) + dfs(root.right, mask)

        return dfs(root, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Explicit Stack + Bit Manipulation

<!-- thinking:start -->

> **Thinking**
>
> A root-to-leaf path can be rearranged into a palindrome exactly when at most one value occurs an odd number of times. Values lie in $1$ through $9$ and $n$ reaches $10^5$, so a 10-bit mask updated by XOR records the parity of each value.
>
> Counting at the leaf and adding the two subtrees would finish the walk, but the search enters the left child first. A left chain can be $n$ nodes long, so recursion overflows before the leaf test. The mask depends only on the path from the root, so the two children do not depend on each other.
>
> An explicit stack stores each node with the mask from above. After a pop, the current value is XORed in. A leaf whose $mask \& (mask-1) = 0$ adds one path; otherwise the right child is pushed, then the left child, both with the updated mask.
>
> Each node is pushed once, and the leaf counts are the number of pseudo-palindromic paths.

<!-- thinking:end -->

A path is a pseudo-palindromic path if and only if the number of nodes with odd occurrences in the path is $0$ or $1$.

Since the range of the binary tree node values is from $1$ to $9$, for each path from root to leaf, we can use a $10$-bit binary number $mask$ to represent the occurrence status of the node values in the current path. The $i$th bit of $mask$ is $1$ if the node value $i$ appears an odd number of times in the current path, and $0$ if it appears an even number of times. Therefore, a path is a pseudo-palindromic path if and only if $mask \& (mask - 1) = 0$, where $\&$ represents the bitwise AND operation.

An explicit stack walks from the root. Each entry is a node and the mask above it. After a pop, set $mask = mask \oplus 2^{\textit{val}}$. If the node is a leaf and $mask \& (mask - 1) = 0$, add one to the answer. Otherwise push the right child and then the left child, both with the updated mask, and skip a missing child. The left child is pushed last, so it is handled first.

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
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stk = [(root, 0)]
        while stk:
            node, mask = stk.pop()
            if node is None:
                continue
            mask ^= 1 << node.val
            if node.left is None and node.right is None:
                ans += (mask & (mask - 1)) == 0
            else:
                stk.append((node.right, mask))
                stk.append((node.left, mask))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
