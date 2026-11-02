---
comments: true
difficulty: Easy
tags:
    - Linked List
---

<!-- problem:start -->

# [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a sorted linked list, <em>delete all duplicates such that each element appears only once</em>. Return <em>the linked list <strong>sorted</strong> as well</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0083.Remove%20Duplicates%20from%20Sorted%20List/images/list1.jpg" style="width: 302px; height: 242px;" />
<pre>
<strong>Input:</strong> head = [1,1,2]
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0083.Remove%20Duplicates%20from%20Sorted%20List/images/list2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,1,2,3,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 300]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>The list is guaranteed to be <strong>sorted</strong> in ascending order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

<!-- thinking:start -->

> **Thinking**
>
> The first idea is dump values into a set and rebuild. Correct, and $n \le 300$ is tiny, but that ignores sorted adjacency and uses extra space.
>
> The bottleneck is not rewriting links in place. Duplicates sit next to each other, so skipping $\textit{cur}.\textit{next}$ when values match is enough.
>
> Unlike the previous problem, we keep the first occurrence. A single pointer walk: drop the next node when equal, advance only when different. The head is always kept, so no dummy is needed.

<!-- thinking:end -->

We use a pointer $\textit{cur}$ to traverse the linked list. If the element corresponding to the current $\textit{cur}$ is the same as the element corresponding to $\textit{cur}.\textit{next}$, we set the $\textit{next}$ pointer of $\textit{cur}$ to point to the next node of $\textit{cur}.\textit{next}$. Otherwise, it means that the element corresponding to $\textit{cur}$ in the linked list is not duplicated, so we can move the $\textit{cur}$ pointer to the next node.

After the traversal ends, return the head node of the linked list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
