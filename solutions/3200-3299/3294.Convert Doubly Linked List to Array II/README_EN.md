---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3294.Convert%20Doubly%20Linked%20List%20to%20Array%20II/README_EN.md
tags:
    - Array
    - Linked List
    - Doubly-Linked List
---

<!-- problem:start -->

# [3294. Convert Doubly Linked List to Array II 🔒](https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii)

## Description

<!-- description:start -->

<p>You are given an <strong>arbitrary</strong> <code>node</code> from a <strong>doubly linked list</strong>, which contains nodes that have a next pointer and a previous pointer.</p>

<p>Return an integer array which contains the elements of the linked list <strong>in order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [1,2,3,4,5], node = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,3,4,5]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [4,5,6,7,8], node = 8</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,5,6,7,8]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given list is in the range <code>[1, 500]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
	<li>All nodes have unique <code>Node.val</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Traverse the Linked List

We can start from the given node and traverse the linked list backward until we reach the head node. Then, we traverse the linked list forward from the head node, adding the values of the nodes we encounter to the answer array.

After the traversal is complete, return the answer array.

The time complexity is $O(n)$, where $n$ is the number of nodes in the linked list. Ignoring the space consumption of the answer array, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""

class Solution:
    def toArray(self, node: "Optional[Node]") -> List[int]:
        while node.prev:
            node = node.prev
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
