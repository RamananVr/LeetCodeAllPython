---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3263.Convert%20Doubly%20Linked%20List%20to%20Array%20I/README_EN.md
tags:
    - Array
    - Linked List
    - Doubly-Linked List
---

<!-- problem:start -->

# [3263. Convert Doubly Linked List to Array I 🔒](https://leetcode.com/problems/convert-doubly-linked-list-to-array-i)

## Description

<!-- description:start -->

<p>You are given the <code>head</code> of a <strong>doubly linked list</strong>, which contains nodes that have a next pointer and a previous pointer.</p>

<p>Return an integer array which contains the elements of the linked list <strong>in order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [1,2,3,4,3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,3,4,3,2,1]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [2,2,2,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2,2,2,2]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [3,2,3,2,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2,3,2,3,2]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given list is in the range <code>[1, 50]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 50</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Direct Traversal

We can directly traverse the linked list, adding the values of the nodes to the answer array $\textit{ans}$ one by one.

After the traversal is complete, return the answer array $\textit{ans}$.

The time complexity is $O(n)$, where $n$ is the length of the linked list. Ignoring the space consumption of the answer array, the space complexity is $O(1)$.

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
    def toArray(self, root: "Optional[Node]") -> List[int]:
        ans = []
        while root:
            ans.append(root.val)
            root = root.next
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
