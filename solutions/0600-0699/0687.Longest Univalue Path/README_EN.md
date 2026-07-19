---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0687.Longest%20Univalue%20Path/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return <em>the length of the longest path, where each node in the path has the same value</em>. This path may or may not pass through the root.</p>

<p><strong>The length of the path</strong> between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0687.Longest%20Univalue%20Path/images/ex1.jpg" style="width: 450px; height: 238px;" />
<pre>
<strong>Input:</strong> root = [5,4,5,1,1,null,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The shown image shows that the longest path of the same value (i.e. 5).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0687.Longest%20Univalue%20Path/images/ex2.jpg" style="width: 450px; height: 238px;" />
<pre>
<strong>Input:</strong> root = [1,4,5,4,4,null,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The shown image shows that the longest path of the same value (i.e. 4).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>The depth of the tree will not exceed <code>1000</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We design a function $\textit{dfs}(root)$, which represents the longest univalue path length extending downward with the $\textit{root}$ node as one endpoint of the path.

In $\textit{dfs}(root)$, we first recursively call $\textit{dfs}(root.\textit{left})$ and $\textit{dfs}(root.\textit{right})$ to get two return values $\textit{l}$ and $\textit{r}$. These two return values represent the longest univalue path lengths extending downward with the left and right children of the $\textit{root}$ node as one endpoint of the path, respectively.

If the $\textit{root}$ has a left child and $\textit{root}.\textit{val} = \textit{root}.\textit{left}.\textit{val}$, then the longest univalue path length extending downward with the left child of the $\textit{root}$ as one endpoint of the path should be $\textit{l} + 1$; otherwise, this length is $0$. If the $\textit{root}$ has a right child and $\textit{root}.\textit{val} = \textit{root}.\textit{right}.\textit{val}$, then the longest univalue path length extending downward with the right child of the $\textit{root}$ as one endpoint of the path should be $\textit{r} + 1$; otherwise, this length is $0$.

After recursively calling the left and right children, we update the answer to $\max(\textit{ans}, \textit{l} + \textit{r})$, which is the longest univalue path length passing through the $\textit{root}$ with the $\textit{root}$ as one endpoint of the path.

Finally, the $\textit{dfs}(root)$ function returns the longest univalue path length extending downward with the $\textit{root}$ as one endpoint of the path, which is $\max(\textit{l}, \textit{r})$.

In the main function, we call $\textit{dfs}(root)$ to get the answer.

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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            l = l + 1 if root.left and root.left.val == root.val else 0
            r = r + 1 if root.right and root.right.val == root.val else 0
            nonlocal ans
            ans = max(ans, l + r)
            return max(l, r)

        ans = 0
        dfs(root)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
