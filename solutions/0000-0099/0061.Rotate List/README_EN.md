---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0061.Rotate%20List/README_EN.md
tags:
    - Linked List
    - Two Pointers
---

<!-- problem:start -->

# [61. Rotate List](https://leetcode.com/problems/rotate-list)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a linked&nbsp;list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0061.Rotate%20List/images/rotate1.jpg" style="width: 450px; height: 191px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0061.Rotate%20List/images/roate2.jpg" style="width: 305px; height: 350px;" />
<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Fast and Slow Pointers + Link List Concatenation

First, we check whether the number of nodes in the linked list is less than $2$. If so, we directly return $head$.

Otherwise, we first count the number of nodes $n$ in the linked list, and then take the modulus of $k$ by $n$ to get the effective value of $k$.

If the effective value of $k$ is $0$, it means that the linked list does not need to be rotated, and we can directly return $head$.

Otherwise, we use fast and slow pointers, let the fast pointer move $k$ steps first, and then let the fast and slow pointers move together until the fast pointer moves to the end of the linked list. At this time, the next node of the slow pointer is the new head node of the linked list.

Finally, we concatenate the linked list.

The time complexity is $O(n)$, where $n$ is the number of nodes in the linked list. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        k %= n
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next

        ans = slow.next
        slow.next = None
        fast.next = head
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
