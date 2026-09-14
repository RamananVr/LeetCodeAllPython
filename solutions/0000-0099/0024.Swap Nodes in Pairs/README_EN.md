---
comments: true
difficulty: Medium
tags:
    - Recursion
    - Linked List
---

<!-- problem:start -->

# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)

## Description

<!-- description:start -->

<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head. You must solve the problem without&nbsp;modifying the values in the list&#39;s nodes (i.e., only nodes themselves may be changed.)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,1,4,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0024.Swap%20Nodes%20in%20Pairs/images/swap_ex1.jpg" style="width: 422px; height: 222px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = []</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">head = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,1,3]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the&nbsp;list&nbsp;is in the range <code>[0, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

<!-- thinking:start -->

> **Thinking**
>
> The first idea is to swap values of adjacent nodes. The problem forbids changing values, so we must rewire pointers. At most $100$ nodes, so any correct linking will pass.
>
> The bottleneck is the link order: flip the first pair and then the rest, and it is easy to lose a successor.
>
> After one pair is swapped, the suffix starting at the third node is the same problem. The new head is always the original second node.
>
> So recurse on $head.next.next$ first, then reverse the current pair onto that result. An empty list or a single node cannot form a pair and is returned as-is.

<!-- thinking:end -->

We can implement swapping two nodes in the linked list through recursion.

The termination condition of recursion is that there are no nodes in the linked list, or there is only one node in the linked list. At this time, swapping cannot be performed, so we directly return this node.

Otherwise, we recursively swap the linked list $head.next.next$, and let the swapped head node be $t$. Then we let $p$ be the next node of $head$, and let $p$ point to $head$, and $head$ point to $t$, finally return $p$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the linked list.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        t = self.swapPairs(head.next.next)
        p = head.next
        p.next = head
        head.next = t
        return p
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Iteration

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 is correct, but recursion depth tracks the number of pairs, so extra space is $O(n)$. The same three pointer writes inside a pair can run in a loop.
>
> A dummy pins the list head. Pointers $pre$ and $cur$ rewrite the two nodes after $pre$, then advance by one pair.
>
> Time stays $O(n)$; extra space drops to $O(1)$.

<!-- thinking:end -->

We set a dummy head node $dummy$, initially pointing to $head$, and then set two pointers $pre$ and $cur$, initially $pre$ points to $dummy$, and $cur$ points to $head$.

Next, we traverse the linked list. Each time we need to swap the two nodes after $pre$, so we first judge whether $cur$ and $cur.next$ are empty. If they are not empty, we perform the swap, otherwise we terminate the loop.

The time complexity is $O(n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the linked list.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        while cur and cur.next:
            t = cur.next
            cur.next = t.next
            t.next = cur
            pre.next = t
            pre, cur = cur, cur.next
        return dummy.next
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
