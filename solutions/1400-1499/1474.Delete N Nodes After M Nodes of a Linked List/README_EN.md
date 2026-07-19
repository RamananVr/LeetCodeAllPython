---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1474.Delete%20N%20Nodes%20After%20M%20Nodes%20of%20a%20Linked%20List/README_EN.md
tags:
    - Linked List
---

<!-- problem:start -->

# [1474. Delete N Nodes After M Nodes of a Linked List 🔒](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list)

## Description

<!-- description:start -->

<p>You are given the <code>head</code> of a linked list and two integers <code>m</code> and <code>n</code>.</p>

<p>Traverse the linked list and remove some nodes in the following way:</p>

<ul>
	<li>Start with the head as the current node.</li>
	<li>Keep the first <code>m</code> nodes starting with the current node.</li>
	<li>Remove the next <code>n</code> nodes</li>
	<li>Keep repeating steps 2 and 3 until you reach the end of the list.</li>
</ul>

<p>Return <em>the head of the modified list after removing the mentioned nodes</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1474.Delete%20N%20Nodes%20After%20M%20Nodes%20of%20a%20Linked%20List/images/sample_1_1848.png" style="width: 600px; height: 95px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
<strong>Output:</strong> [1,2,6,7,11,12]
<strong>Explanation:</strong> Keep the first (m = 2) nodes starting from the head of the linked List  (1 -&gt;2) show in black nodes.
Delete the next (n = 3) nodes (3 -&gt; 4 -&gt; 5) show in read nodes.
Continue with the same procedure until reaching the tail of the Linked List.
Head of the linked list after removing nodes is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1474.Delete%20N%20Nodes%20After%20M%20Nodes%20of%20a%20Linked%20List/images/sample_2_1848.png" style="width: 600px; height: 123px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
<strong>Output:</strong> [1,5,9]
<strong>Explanation:</strong> Head of linked list after removing nodes is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve this problem by modifying the list in-place?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We can simulate the entire deletion process. First, use a pointer $\textit{pre}$ to point to the head of the linked list, then traverse the linked list, moving $m - 1$ steps. If $\textit{pre}$ is null, it means the number of nodes from the current node is less than $m$, so we directly return the head. Otherwise, use a pointer $\textit{cur}$ to point to $\textit{pre}$, then move $n$ steps. If $\textit{cur}$ is null, it means the number of nodes from $\textit{pre}$ is less than $m + n$, so we directly set the $\textit{next}$ of $\textit{pre}$ to null. Otherwise, set the $\textit{next}$ of $\textit{pre}$ to the $\textit{next}$ of $\textit{cur}$, then move $\textit{pre}$ to its $\textit{next}$. Continue traversing the linked list until $\textit{pre}$ is null, then return the head.

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
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = head
        while pre:
            for _ in range(m - 1):
                if pre:
                    pre = pre.next
            if pre is None:
                return head
            cur = pre
            for _ in range(n):
                if cur:
                    cur = cur.next
            pre.next = None if cur is None else cur.next
            pre = pre.next
        return head
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
