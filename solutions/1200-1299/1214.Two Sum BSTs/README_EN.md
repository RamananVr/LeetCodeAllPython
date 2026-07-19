---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1214.Two%20Sum%20BSTs/README_EN.md
rating: 1389
source: Biweekly Contest 10 Q2
tags:
    - Stack
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Two Pointers
    - Binary Search
    - Binary Tree
---

<!-- problem:start -->

# [1214. Two Sum BSTs 🔒](https://leetcode.com/problems/two-sum-bsts)

## Description

<!-- description:start -->

<p>Given the roots of two binary search trees, <code>root1</code> and <code>root2</code>, return <code>true</code> if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1214.Two%20Sum%20BSTs/images/ex1.png" style="width: 369px; height: 169px;" />
<pre>
<strong>Input:</strong> root1 = [2,1,4], root2 = [1,0,3], target = 5
<strong>Output:</strong> true
<strong>Explanation: </strong>2 and 3 sum up to 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1214.Two%20Sum%20BSTs/images/ex2.png" style="width: 453px; height: 290px;" />
<pre>
<strong>Input:</strong> root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each tree is in the range <code>[1, 5000]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val, target &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: In-order Traversal + Two Pointers

We perform in-order traversals on the two trees separately, obtaining two sorted arrays $nums[0]$ and $nums[1]$. Then we use a two-pointer method to determine whether there exist two numbers whose sum equals the target value. The two-pointer method is as follows:

Initialize two pointers $i$ and $j$, pointing to the left boundary of array $nums[0]$ and the right boundary of array $nums[1]$ respectively;

Each time, compare the sum $x = nums[0][i] + nums[1][j]$ with the target value. If $x = target$, return `true`; otherwise, if $x \lt target$, move $i$ one step to the right; otherwise, if $x \gt target$, move $j$ one step to the left.

The time complexity is $O(m + n)$, and the space complexity is $O(m + n)$. Here, $m$ and $n$ are the number of nodes in the two trees respectively.

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
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        def dfs(root: Optional[TreeNode], i: int):
            if root is None:
                return
            dfs(root.left, i)
            nums[i].append(root.val)
            dfs(root.right, i)

        nums = [[], []]
        dfs(root1, 0)
        dfs(root2, 1)
        i, j = 0, len(nums[1]) - 1
        while i < len(nums[0]) and ~j:
            x = nums[0][i] + nums[1][j]
            if x == target:
                return True
            if x < target:
                i += 1
            else:
                j -= 1
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
