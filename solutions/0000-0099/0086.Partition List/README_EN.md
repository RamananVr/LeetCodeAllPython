---
comments: true
difficulty: Medium
tags:
    - Linked List
    - Two Pointers
---

<!-- problem:start -->

# [86. Partition List](https://leetcode.com/problems/partition-list)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a linked list and a value <code>x</code>, partition it such that all nodes <strong>less than</strong> <code>x</code> come before nodes <strong>greater than or equal</strong> to <code>x</code>.</p>

<p>You should <strong>preserve</strong> the original relative order of the nodes in each of the two partitions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0086.Partition%20List/images/partition.jpg" style="width: 662px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,4,3,2,5,2], x = 3
<strong>Output:</strong> [1,2,2,4,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [2,1], x = 2
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 200]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>-200 &lt;= x &lt;= 200</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> The first idea is two scans: collect nodes $< x$, then the rest, and rebuild. Correct, and $n \le 200$ is tiny, but that copies nodes or walks twice, and it is easy to scramble relative order.
>
> The bottleneck is splitting and reassembling instead of one pass. The problem only asks for a stable partition: order among the small nodes and among the large nodes both stay the same.
>
> So grow two lists in one walk and stitch the small tail to the large head. Tail pointers link original nodes — no copies; clear the large tail to avoid a cycle.

<!-- thinking:end -->

We create two linked lists $l$ and $r$, one to store nodes less than $x$ and the other to store nodes greater than or equal to $x$. Then we concatenate them.

The time complexity is $O(n)$, where $n$ is the length of the original linked list. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = ListNode()
        r = ListNode()
        tl, tr = l, r
        while head:
            if head.val < x:
                tl.next = head
                tl = tl.next
            else:
                tr.next = head
                tr = tr.next
            head = head.next
        tr.next = None
        tl.next = r.next
        return l.next
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
