---
comments: true
difficulty: Medium
rating: 1454
source: Weekly Contest 321 Q3
tags:
    - Stack
    - Recursion
    - Linked List
    - Monotonic Stack
---

<!-- problem:start -->

# [2487. Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list)

## Description

<!-- description:start -->

<p>You are given the <code>head</code> of a linked list.</p>

<p>Remove every node which has a node with a greater value anywhere to the right side of it.</p>

<p>Return <em>the </em><code>head</code><em> of the modified linked list.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2400-2499/2487.Remove%20Nodes%20From%20Linked%20List/images/drawio.png" style="width: 631px; height: 51px;" />
<pre>
<strong>Input:</strong> head = [5,2,13,3,8]
<strong>Output:</strong> [13,8]
<strong>Explanation:</strong> The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1,1,1,1]
<strong>Output:</strong> [1,1,1,1]
<strong>Explanation:</strong> Every node has value 1, so no nodes are removed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the given list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack (Array)

<!-- thinking:start -->

> **Thinking**
>
> Delete a node if a strictly larger value exists to its right: keep the decreasing right-to-left suffix. At $n\le 10^5$, copy values, maintain a decreasing stack, then rebuild the list.

<!-- thinking:end -->

Store the node values in an array $nums$, then scan $nums$ with a monotonically decreasing stack. Pop while the current value is larger than the top, then push. Rebuild the list from the bottom of the stack.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the linked list.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stk = []
        for v in nums:
            while stk and stk[-1] < v:
                stk.pop()
            stk.append(v)
        dummy = ListNode()
        head = dummy
        for v in stk:
            head.next = ListNode(v)
            head = head.next
        return dummy.next
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Monotonic Stack (In-place List)

<!-- thinking:start -->

> **Thinking**
>
> Method 1 allocates a value array and new nodes. The same stack can hold list nodes: pop while the top is smaller, then link the new top to the current node. A dummy of $+\infty$ avoids an empty stack.

<!-- thinking:end -->

Traverse the list directly with a monotonically decreasing stack of nodes. When the current value is larger, pop; then link the new top's $next$ (or the dummy head) to the current node and push it. Return the dummy head's $next$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the linked list.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(inf, head)
        cur = head
        stk = [dummy]
        while cur:
            while stk[-1].val < cur.val:
                stk.pop()
            stk[-1].next = cur
            stk.append(cur)
            cur = cur.next
        return dummy.next
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
