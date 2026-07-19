---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0437.Path%20Sum%20III/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Binary Tree
---

<!-- problem:start -->

# [437. Path Sum III](https://leetcode.com/problems/path-sum-iii)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>the number of paths where the sum of the values&nbsp;along the path equals</em>&nbsp;<code>targetSum</code>.</p>

<p>The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0437.Path%20Sum%20III/images/pathsum3-1-tree.jpg" style="width: 450px; height: 386px;" />
<pre>
<strong>Input:</strong> root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
<strong>Output:</strong> 3
<strong>Explanation:</strong> The paths that sum to 8 are shown.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 1000]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Prefix Sum + Recursion

We can use the idea of prefix sums to recursively traverse the binary tree while using a hash table $\textit{cnt}$ to count the occurrences of each prefix sum along the path from the root to the current node.

We design a recursive function $\textit{dfs(node, s)}$, where $\textit{node}$ represents the current node being traversed, and $s$ represents the prefix sum along the path from the root to the current node. The return value of the function is the number of paths ending at $\textit{node}$ or its subtree nodes with a sum equal to $\textit{targetSum}$. The final answer is $\textit{dfs(root, 0)}$.

The recursive process of $\textit{dfs(node, s)}$ is as follows:

- If the current node $\textit{node}$ is null, return $0$.
- Calculate the prefix sum $s$ along the path from the root to the current node.
- Use $\textit{cnt}[s - \textit{targetSum}]$ to represent the number of paths ending at the current node with a sum equal to $\textit{targetSum}$. Here, $\textit{cnt}[s - \textit{targetSum}]$ is the count of prefix sums equal to $s - \textit{targetSum}$ in $\textit{cnt}$.
- Increment the count of the prefix sum $s$ by $1$, i.e., $\textit{cnt}[s] = \textit{cnt}[s] + 1$.
- Recursively traverse the left and right child nodes of the current node by calling $\textit{dfs(node.left, s)}$ and $\textit{dfs(node.right, s)}$, and add their return values.
- After the return value is calculated, decrement the count of the prefix sum $s$ by $1$, i.e., $\textit{cnt}[s] = \textit{cnt}[s] - 1$.
- Finally, return the result.

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s):
            if node is None:
                return 0
            s += node.val
            ans = cnt[s - targetSum]
            cnt[s] += 1
            ans += dfs(node.left, s)
            ans += dfs(node.right, s)
            cnt[s] -= 1
            return ans

        cnt = Counter({0: 1})
        return dfs(root, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
