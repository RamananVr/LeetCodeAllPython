---
comments: true
difficulty: Medium
tags:
    - Linked List
    - Two Pointers
    - Divide and Conquer
    - Sorting
    - Merge Sort
---

<!-- problem:start -->

# [148. Sort List](https://leetcode.com/problems/sort-list)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a linked list, return <em>the list after sorting it in <strong>ascending order</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0148.Sort%20List/images/sort_list_1.jpg" style="width: 450px; height: 194px;" />
<pre>
<strong>Input:</strong> head = [4,2,1,3]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0148.Sort%20List/images/sort_list_2.jpg" style="width: 550px; height: 184px;" />
<pre>
<strong>Input:</strong> head = [-1,5,3,4,0]
<strong>Output:</strong> [-1,0,3,4,5]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you sort the linked list in <code>O(n logn)</code> time and <code>O(1)</code> memory (i.e. constant space)?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Merge Sort

<!-- thinking:start -->

> **Thinking**
>
> Sort a list; the follow-up wants $O(n\log n)$ time and constant extra space. There is no random access, so quicksort swaps are awkward. $n\le 5\times 10^4$. Merge sort only needs sequential scans: split at the midpoint, sort both halves, merge. The recursion stack is $O(\log n)$.

<!-- thinking:end -->

We can use the merge sort approach to solve this problem.

First, we use the fast and slow pointers to find the middle of the linked list and break the list from the middle to form two separate sublists $\textit{l1}$ and $\textit{l2}$.

Then, we recursively sort $\textit{l1}$ and $\textit{l2}$, and finally merge $\textit{l1}$ and $\textit{l2}$ into a sorted linked list.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$. Here, $n$ is the length of the linked list.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1, l2 = head, slow.next
        slow.next = None
        l1, l2 = self.sortList(l1), self.sortList(l2)
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
