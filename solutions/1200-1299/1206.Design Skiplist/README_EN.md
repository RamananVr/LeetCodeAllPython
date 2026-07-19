---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1206.Design%20Skiplist/README_EN.md
tags:
    - Design
    - Linked List
---

<!-- problem:start -->

# [1206. Design Skiplist](https://leetcode.com/problems/design-skiplist)

## Description

<!-- description:start -->

<p>Design a <strong>Skiplist</strong> without using any built-in libraries.</p>

<p>A <strong>skiplist</strong> is a data structure that takes <code>O(log(n))</code> time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.</p>

<p>For example, we have a Skiplist containing <code>[30,40,50,60,70,90]</code> and we want to add <code>80</code> and <code>45</code> into it. The Skiplist works this way:</p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1206.Design%20Skiplist/images/1506_skiplist.gif" style="width: 500px; height: 173px;" /><br />
<small>Artyom Kalinin [CC BY-SA 3.0], via <a href="https://commons.wikimedia.org/wiki/File:Skip_list_add_element-en.gif" target="_blank" title="Artyom Kalinin [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons">Wikimedia Commons</a></small></p>

<p>You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than <code>O(n)</code>. It can be proven that the average time complexity for each operation is <code>O(log(n))</code> and space complexity is <code>O(n)</code>.</p>

<p>See more about Skiplist: <a href="https://en.wikipedia.org/wiki/Skip_list" target="_blank">https://en.wikipedia.org/wiki/Skip_list</a></p>

<p>Implement the <code>Skiplist</code> class:</p>

<ul>
	<li><code>Skiplist()</code> Initializes the object of the skiplist.</li>
	<li><code>bool search(int target)</code> Returns <code>true</code> if the integer <code>target</code> exists in the Skiplist or <code>false</code> otherwise.</li>
	<li><code>void add(int num)</code> Inserts the value <code>num</code> into the SkipList.</li>
	<li><code>bool erase(int num)</code> Removes the value <code>num</code> from the Skiplist and returns <code>true</code>. If <code>num</code> does not exist in the Skiplist, do nothing and return <code>false</code>. If there exist multiple <code>num</code> values, removing any one of them is fine.</li>
</ul>

<p>Note that duplicates may exist in the Skiplist, your code needs to handle this situation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Skiplist&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;, &quot;search&quot;, &quot;add&quot;, &quot;search&quot;, &quot;erase&quot;, &quot;erase&quot;, &quot;search&quot;]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
<strong>Output</strong>
[null, null, null, null, false, null, true, false, true, false]

<strong>Explanation</strong>
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0); // return False
skiplist.add(4);
skiplist.search(1); // return True
skiplist.erase(0);  // return False, 0 is not in skiplist.
skiplist.erase(1);  // return True
skiplist.search(1); // return False, 1 has already been erased.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num, target &lt;= 2 * 10<sup>4</sup></code></li>
	<li>At most <code>5 * 10<sup>4</sup></code> calls will be made to <code>search</code>, <code>add</code>, and <code>erase</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Data Structure

The core idea of a skip list is to use multiple "levels" to store data, with each level acting as an index. Data starts from the bottom level linked list and gradually rises to higher levels, eventually forming a multi-level linked list structure. Each level's nodes only contain part of the data, allowing for jumps to reduce search time.

In this problem, we use a $\textit{Node}$ class to represent the nodes of the skip list. Each node contains a $\textit{val}$ field and a $\textit{next}$ array. The length of the array is $\textit{level}$, indicating the next node at each level. We use a $\textit{Skiplist}$ class to implement the skip list operations.

The skip list contains a head node $\textit{head}$ and the current maximum level $\textit{level}$. The head node's value is set to $-1$ to mark the starting position of the list. We use a dynamic array $\textit{next}$ to store pointers to successor nodes.

For the $\textit{search}$ operation, we start from the highest level of the skip list and traverse downwards until we find the target node or determine that the target node does not exist. At each level, we use the $\textit{find\_closest}$ method to jump to the node closest to the target.

For the $\textit{add}$ operation, we first randomly decide the level of the new node. Then, starting from the highest level, we find the node closest to the new value at each level and insert the new node at the appropriate position. If the level of the inserted node is greater than the current maximum level of the skip list, we need to update the level of the skip list.

For the $\textit{erase}$ operation, similar to the search operation, we traverse each level of the skip list to find and delete the target node. When deleting a node, we need to update the $\textit{next}$ pointers at each level. If the highest level of the skip list has no nodes, we need to decrease the level of the skip list.

Additionally, we define a $\textit{random\_level}$ method to randomly decide the level of the new node. This method generates a random number between $[1, \textit{max\_level}]$ until the generated random number is greater than or equal to $\textit{p}$. We also have a $\textit{find\_closest}$ method to find the node closest to the target value at each level.

The time complexity of the above operations is $O(\log n)$, where $n$ is the number of nodes in the skip list. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = ['val', 'next']

    def __init__(self, val: int, level: int):
        self.val = val
        self.next = [None] * level

class Skiplist:
    max_level = 32
    p = 0.25

    def __init__(self):
        self.head = Node(-1, self.max_level)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            curr = self.find_closest(curr, i, target)
            if curr.next[i] and curr.next[i].val == target:
                return True
        return False

    def add(self, num: int) -> None:
        curr = self.head
        level = self.random_level()
        node = Node(num, level)
        self.level = max(self.level, level)
        for i in range(self.level - 1, -1, -1):
            curr = self.find_closest(curr, i, num)
            if i < level:
                node.next[i] = curr.next[i]
                curr.next[i] = node

    def erase(self, num: int) -> bool:
        curr = self.head
        ok = False
        for i in range(self.level - 1, -1, -1):
            curr = self.find_closest(curr, i, num)
            if curr.next[i] and curr.next[i].val == num:
                curr.next[i] = curr.next[i].next[i]
                ok = True
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
        return ok

    def find_closest(self, curr: Node, level: int, target: int) -> Node:
        while curr.next[level] and curr.next[level].val < target:
            curr = curr.next[level]
        return curr

    def random_level(self) -> int:
        level = 1
        while level < self.max_level and random.random() < self.p:
            level += 1
        return level

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
