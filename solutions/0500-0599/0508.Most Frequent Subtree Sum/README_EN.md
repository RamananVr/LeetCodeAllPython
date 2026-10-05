---
comments: true
difficulty: Medium
tags:
    - Tree
    - Depth-First Search
    - Hash Table
    - Binary Tree
    - Tree DP
---

<!-- problem:start -->

# [508. Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum)

## Description

<!-- description:start -->

<p>Given the <code>root</code> of a binary tree, return the most frequent <strong>subtree sum</strong>. If there is a tie, return all the values with the highest frequency in any order.</p>

<p>The <strong>subtree sum</strong> of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0508.Most%20Frequent%20Subtree%20Sum/images/freq1-tree.jpg" style="width: 207px; height: 183px;" />
<pre>
<strong>Input:</strong> root = [5,2,-3]
<strong>Output:</strong> [2,-3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0508.Most%20Frequent%20Subtree%20Sum/images/freq2-tree.jpg" style="width: 207px; height: 183px;" />
<pre>
<strong>Input:</strong> root = [5,2,-5]
<strong>Output:</strong> [2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + DFS

<!-- thinking:start -->

> **Thinking**
>
> A subtree sum is left + right + root, so both children must be known first. Rescanning each subtree repeats work.
>
> A post-order DFS returns the current sum and a hash map counts frequencies. After the walk, keep the sums whose frequency is maximal. One traversal both sums and counts.

<!-- thinking:end -->

We can use a hash table $\textit{cnt}$ to record the frequency of each subtree sum. Then, we use depth-first search (DFS) to traverse the entire tree, calculate the sum of elements for each subtree, and update $\textit{cnt}$.

Finally, we traverse $\textit{cnt}$ to find all subtree sums that appear most frequently.

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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            s = l + r + root.val
            cnt[s] += 1
            return s

        cnt = Counter()
        dfs(root)
        mx = max(cnt.values())
        return [k for k, v in cnt.items() if v == mx]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table + Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> A subtree sum is the left sum plus the right sum plus the node value, so both children must be known first. Rescanning each subtree repeats work. Returning the sum from a postorder recursion is correct on a short tree.
>
> The tree can contain $10^4$ nodes. A left chain makes this postorder walk recurse once per node and overflow the call stack.
>
> Each sum depends only on the two children, so children must be finished before their parent. Frequencies can be counted in a hash table during the walk.
>
> An explicit stack performs that postorder walk. On entry it pushes an exit marker and the two children; on exit it writes the subtree sum into the hash table. After the walk, the sums with the highest frequency are the answer.

<!-- thinking:end -->

A hash table $\textit{cnt}$ records how often each subtree sum appears. An explicit stack walks the binary tree in postorder. On entry we push an exit marker, then the right child and the left child. On exit the children's sums are already stored, the current sum is those two plus the node value, and $\textit{cnt}$ is updated.

Finally we keep every subtree sum whose frequency is maximal.

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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        sub = {}
        stk = [(root, 0)]
        while stk:
            node, state = stk.pop()
            if node is None:
                continue
            if state == 0:
                stk.append((node, 1))
                stk.append((node.right, 0))
                stk.append((node.left, 0))
                continue
            l = sub[id(node.left)] if node.left is not None else 0
            r = sub[id(node.right)] if node.right is not None else 0
            s = l + r + node.val
            cnt[s] += 1
            sub[id(node)] = s
        if not cnt:
            return []
        mx = max(cnt.values())
        return [k for k, v in cnt.items() if v == mx]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
