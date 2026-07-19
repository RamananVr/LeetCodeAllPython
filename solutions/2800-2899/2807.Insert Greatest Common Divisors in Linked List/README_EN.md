---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2807.Insert%20Greatest%20Common%20Divisors%20in%20Linked%20List/README_EN.md
rating: 1279
source: Biweekly Contest 110 Q2
tags:
    - Linked List
    - Math
    - Number Theory
---

<!-- problem:start -->

# [2807. Insert Greatest Common Divisors in Linked List](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list)

## Description

<!-- description:start -->

<p>Given the head of a linked list <code>head</code>, in which each node contains an integer value.</p>

<p>Between every pair of adjacent nodes, insert a new node with a value equal to the <strong>greatest common divisor</strong> of them.</p>

<p>Return <em>the linked list after insertion</em>.</p>

<p>The <strong>greatest common divisor</strong> of two numbers is the largest positive integer that evenly divides both numbers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2807.Insert%20Greatest%20Common%20Divisors%20in%20Linked%20List/images/ex1_copy.png" style="width: 641px; height: 181px;" />
<pre>
<strong>Input:</strong> head = [18,6,10,3]
<strong>Output:</strong> [18,6,6,2,10,1,3]
<strong>Explanation:</strong> The 1<sup>st</sup> diagram denotes the initial linked list and the 2<sup>nd</sup> diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1<sup>st</sup> and the 2<sup>nd</sup> nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2<sup>nd</sup> and the 3<sup>rd</sup> nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3<sup>rd</sup> and the 4<sup>th</sup> nodes.
There are no more adjacent nodes, so we return the linked list.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2807.Insert%20Greatest%20Common%20Divisors%20in%20Linked%20List/images/ex2_copy1.png" style="width: 51px; height: 191px;" />
<pre>
<strong>Input:</strong> head = [7]
<strong>Output:</strong> [7]
<strong>Explanation:</strong> The 1<sup>st</sup> diagram denotes the initial linked list and the 2<sup>nd</sup> diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We use two pointers $pre$ and $cur$ to point to the current node and the next node respectively. We only need to insert a new node between $pre$ and $cur$. Therefore, each time we calculate the greatest common divisor $x$ of $pre$ and $cur$, we insert a new node with value $x$ between $pre$ and $cur$. Then we update $pre = cur$ and $cur = cur.next$, and continue to traverse the linked list until $cur$ is null.

The time complexity is $O(n \times \log M)$, where $n$ is the length of the linked list, and $M$ is the maximum value of the nodes in the linked list. Ignoring the space consumption of the result linked list, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        pre, cur = head, head.next
        while cur:
            x = gcd(pre.val, cur.val)
            pre.next = ListNode(x, cur)
            pre, cur = cur, cur.next
        return head
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
