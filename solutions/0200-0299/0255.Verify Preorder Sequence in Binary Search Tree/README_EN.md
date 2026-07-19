---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0255.Verify%20Preorder%20Sequence%20in%20Binary%20Search%20Tree/README_EN.md
tags:
    - Stack
    - Tree
    - Binary Search Tree
    - Recursion
    - Array
    - Binary Tree
    - Monotonic Stack
---

<!-- problem:start -->

# [255. Verify Preorder Sequence in Binary Search Tree 🔒](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree)

## Description

<!-- description:start -->

<p>Given an array of <strong>unique</strong> integers <code>preorder</code>, return <code>true</code> <em>if it is the correct preorder traversal sequence of a binary search tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0255.Verify%20Preorder%20Sequence%20in%20Binary%20Search%20Tree/images/preorder-tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> preorder = [5,2,1,3,6]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> preorder = [5,2,6,1,3]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= preorder[i] &lt;= 10<sup>4</sup></code></li>
	<li>All the elements of <code>preorder</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it using only constant space complexity?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stk = []
        last = -inf
        for x in preorder:
            if x < last:
                return False
            while stk and stk[-1] < x:
                last = stk.pop()
            stk.append(x)
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
