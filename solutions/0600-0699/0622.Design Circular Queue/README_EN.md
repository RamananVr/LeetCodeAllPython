---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0622.Design%20Circular%20Queue/README_EN.md
tags:
    - Design
    - Queue
    - Array
    - Linked List
---

<!-- problem:start -->

# [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue)

## Description

<!-- description:start -->

<p>Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called &quot;Ring Buffer&quot;.</p>

<p>One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.</p>

<p>Implement the <code>MyCircularQueue</code> class:</p>

<ul>
	<li><code>MyCircularQueue(k)</code> Initializes the object with the size of the queue to be <code>k</code>.</li>
	<li><code>int Front()</code> Gets the front item from the queue. If the queue is empty, return <code>-1</code>.</li>
	<li><code>int Rear()</code> Gets the last item from the queue. If the queue is empty, return <code>-1</code>.</li>
	<li><code>boolean enQueue(int value)</code> Inserts an element into the circular queue. Return <code>true</code> if the operation is successful.</li>
	<li><code>boolean deQueue()</code> Deletes an element from the circular queue. Return <code>true</code> if the operation is successful.</li>
	<li><code>boolean isEmpty()</code> Checks whether the circular queue is empty or not.</li>
	<li><code>boolean isFull()</code> Checks whether the circular queue is full or not.</li>
</ul>

<p>You must solve the problem without using the built-in queue data structure in your programming language.&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyCircularQueue&quot;, &quot;enQueue&quot;, &quot;enQueue&quot;, &quot;enQueue&quot;, &quot;enQueue&quot;, &quot;Rear&quot;, &quot;isFull&quot;, &quot;deQueue&quot;, &quot;enQueue&quot;, &quot;Rear&quot;]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
<strong>Output</strong>
[null, true, true, true, false, 3, true, true, true, 4]

<strong>Explanation</strong>
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>0 &lt;= value &lt;= 1000</code></li>
	<li>At most <code>3000</code> calls will be made to&nbsp;<code>enQueue</code>, <code>deQueue</code>,&nbsp;<code>Front</code>,&nbsp;<code>Rear</code>,&nbsp;<code>isEmpty</code>, and&nbsp;<code>isFull</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Array Simulation

We can use an array $q$ of length $k$ to simulate a circular queue, with a pointer $\textit{front}$ to record the position of the front element. Initially, the queue is empty, and $\textit{front}$ is $0$. Additionally, we use a variable $\textit{size}$ to record the number of elements in the queue, initially $\textit{size}$ is $0$.

When calling the `enQueue` method, we first check if the queue is full, i.e., $\textit{size} = k$. If it is full, we return $\textit{false}$. Otherwise, we insert the element at position $(\textit{front} + \textit{size}) \bmod k$, then $\textit{size} = \textit{size} + 1$, indicating that the number of elements in the queue has increased by $1$. Finally, we return $\textit{true}$.

When calling the `deQueue` method, we first check if the queue is empty, i.e., $\textit{size} = 0$. If it is empty, we return $\textit{false}$. Otherwise, we set $\textit{front} = (\textit{front} + 1) \bmod k$, indicating that the front element has been dequeued, then $\textit{size} = \textit{size} - 1$.

When calling the `Front` method, we first check if the queue is empty, i.e., $\textit{size} = 0$. If it is empty, we return $-1$. Otherwise, we return $q[\textit{front}]$.

When calling the `Rear` method, we first check if the queue is empty, i.e., $\textit{size} = 0$. If it is empty, we return $-1$. Otherwise, we return $q[(\textit{front} + \textit{size} - 1) \bmod k]$.

When calling the `isEmpty` method, we simply check if $\textit{size} = 0$.

When calling the `isFull` method, we simply check if $\textit{size} = k$.

In terms of time complexity, the above operations all have a time complexity of $O(1)$. The space complexity is $O(k)$.

<!-- tabs:start -->

#### Python3

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.size = 0
        self.capacity = k
        self.front = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[(self.front + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
