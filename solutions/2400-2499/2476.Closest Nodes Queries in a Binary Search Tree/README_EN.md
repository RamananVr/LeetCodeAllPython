---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2476.Closest%20Nodes%20Queries%20in%20a%20Binary%20Search%20Tree/README_EN.md
rating: 1596
source: Weekly Contest 320 Q2
tags:
    - Tree
    - Depth-First Search
    - Binary Search Tree
    - Array
    - Binary Search
    - Binary Tree
---

<!-- problem:start -->

# [2476. Closest Nodes Queries in a Binary Search Tree](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree)

## Description

<!-- description:start -->

<p>You are given the <code>root</code> of a <strong>binary search tree </strong>and an array <code>queries</code> of size <code>n</code> consisting of positive integers.</p>

<p>Find a <strong>2D</strong> array <code>answer</code> of size <code>n</code> where <code>answer[i] = [min<sub>i</sub>, max<sub>i</sub>]</code>:</p>

<ul>
	<li><code>min<sub>i</sub></code> is the <strong>largest</strong> value in the tree that is smaller than or equal to <code>queries[i]</code>. If a such value does not exist, add <code>-1</code> instead.</li>
	<li><code>max<sub>i</sub></code> is the <strong>smallest</strong> value in the tree that is greater than or equal to <code>queries[i]</code>. If a such value does not exist, add <code>-1</code> instead.</li>
</ul>

<p>Return <em>the array</em> <code>answer</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2476.Closest%20Nodes%20Queries%20in%20a%20Binary%20Search%20Tree/images/bstreeedrawioo.png" style="width: 261px; height: 281px;" />
<pre>
<strong>Input:</strong> root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
<strong>Output:</strong> [[2,2],[4,6],[15,-1]]
<strong>Explanation:</strong> We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2476.Closest%20Nodes%20Queries%20in%20a%20Binary%20Search%20Tree/images/bstttreee.png" style="width: 101px; height: 121px;" />
<pre>
<strong>Input:</strong> root = [4,null,9], queries = [3]
<strong>Output:</strong> [[-1,4]]
<strong>Explanation:</strong> The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
	<li><code>n == queries.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: In-order Traversal + Binary Search

Since the problem provides a binary search tree, we can obtain a sorted array through in-order traversal. Then for each query, we can find the maximum value less than or equal to the query value and the minimum value greater than or equal to the query value through binary search.

The time complexity is $O(n + m \times \log n)$, and the space complexity is $O(n)$. Here, $n$ and $m$ are the number of nodes in the binary search tree and the number of queries, respectively.

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
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)

        nums = []
        dfs(root)
        ans = []
        for x in queries:
            i = bisect_left(nums, x + 1) - 1
            j = bisect_left(nums, x)
            mi = nums[i] if 0 <= i < len(nums) else -1
            mx = nums[j] if 0 <= j < len(nums) else -1
            ans.append([mi, mx])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
