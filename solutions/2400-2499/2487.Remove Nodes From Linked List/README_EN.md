---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2487.Remove%20Nodes%20From%20Linked%20List/README_EN.md
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

### Solution 1: Monotonic Stack Simulation

We can first store the node values of the linked list into an array $nums$. Then, we traverse the array $nums$, maintaining a stack $stk$ that is monotonically decreasing from the bottom to the top. If the current element is larger than the top element of the stack, we pop the top element of the stack until the current element is less than or equal to the top element, and then we push the current element into the stack.

Finally, we construct the resulting linked list from the bottom to the top of the stack, which is the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the linked list.

We can also directly traverse the linked list without using the array $nums$, maintaining a stack $stk$ that is monotonically decreasing from the bottom to the top. If the current element is larger than the top element of the stack, we pop the top element of the stack until the current element is less than or equal to the top element. Then, if the stack is not empty, we set the $next$ pointer of the top element of the stack to the current element. Otherwise, we set the $next$ pointer of the dummy head node of the answer linked list to the current element. Finally, we push the current element into the stack and continue to traverse the linked list.

After the traversal, we return the $next$ pointer of the dummy head node as the answer.

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

### Solution 2

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
