---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3000-3099/3063.Linked%20List%20Frequency/README_EN.md
tags:
    - Hash Table
    - Linked List
    - Counting
---

<!-- problem:start -->

# [3063. Linked List Frequency 🔒](https://leetcode.com/problems/linked-list-frequency)

## Description

<!-- description:start -->

<p>Given the <code>head</code> of a linked list containing <code>k</code> <strong>distinct</strong> elements, return <em>the head to a linked list of length </em><code>k</code><em> containing the <span data-keyword="frequency-linkedlist">frequency</span> of each <strong>distinct</strong> element in the given linked list in <strong>any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [1,1,2,1,2,3] </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [3,2,1] </span></p>

<p><strong>Explanation: </strong> There are <code>3</code> distinct elements in the list. The frequency of <code>1</code> is <code>3</code>, the frequency of <code>2</code> is <code>2</code> and the frequency of <code>3</code> is <code>1</code>. Hence, we return <code>3 -&gt; 2 -&gt; 1</code>.</p>

<p>Note that <code>1 -&gt; 2 -&gt; 3</code>, <code>1 -&gt; 3 -&gt; 2</code>, <code>2 -&gt; 1 -&gt; 3</code>, <code>2 -&gt; 3 -&gt; 1</code>, and <code>3 -&gt; 1 -&gt; 2</code> are also valid answers.</p>
</div>

<p><strong class="example">Example 2: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [1,1,2,2,2] </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [2,3] </span></p>

<p><strong>Explanation: </strong> There are <code>2</code> distinct elements in the list. The frequency of <code>1</code> is <code>2</code> and the frequency of <code>2</code> is <code>3</code>. Hence, we return <code>2 -&gt; 3</code>.</p>
</div>

<p><strong class="example">Example 3: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [6,5,4,3,2,1] </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [1,1,1,1,1,1] </span></p>

<p><strong>Explanation: </strong> There are <code>6</code> distinct elements in the list. The frequency of each of them is <code>1</code>. Hence, we return <code>1 -&gt; 1 -&gt; 1 -&gt; 1 -&gt; 1 -&gt; 1</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We use a hash table `cnt` to record the occurrence times of each element value in the linked list, then traverse the values of the hash table to construct a new linked list.

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
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = Counter()
        while head:
            cnt[head.val] += 1
            head = head.next
        dummy = ListNode()
        for val in cnt.values():
            dummy.next = ListNode(val, dummy.next)
        return dummy.next
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
