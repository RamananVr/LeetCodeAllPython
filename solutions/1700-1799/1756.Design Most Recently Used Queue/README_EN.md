---
comments: true
difficulty: Medium
tags:
    - Design
    - Array
    - Linked List
    - Divide and Conquer
    - Doubly-Linked List
    - Splay Tree
    - Treap
    - Simulation
    - Sqrt Decomposition
---

<!-- problem:start -->

# [1756. Design Most Recently Used Queue 🔒](https://leetcode.com/problems/design-most-recently-used-queue)

## Description

<!-- description:start -->

<p>Design a queue-like data structure that moves the most recently used element to the end of the queue.</p>

<p>Implement the <code>MRUQueue</code> class:</p>

<ul>
	<li><code>MRUQueue(int n)</code> constructs the <code>MRUQueue</code> with <code>n</code> elements: <code>[1,2,3,...,n]</code>.</li>
	<li><code>int fetch(int k)</code> moves the <code>k<sup>th</sup></code> element <strong>(1-indexed)</strong> to the end of the queue and returns it.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[&quot;MRUQueue&quot;, &quot;fetch&quot;, &quot;fetch&quot;, &quot;fetch&quot;, &quot;fetch&quot;]
[[8], [3], [5], [2], [8]]
<strong>Output:</strong>
[null, 3, 6, 2, 2]

<strong>Explanation:</strong>
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3<sup>rd</sup> element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5<sup>th</sup> element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2<sup>nd</sup> element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8<sup>th</sup> element (2) is already at the end of the queue so just return it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li>At most <code>2000</code> calls will be made to <code>fetch</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Finding an <code>O(n)</code> algorithm per <code>fetch</code> is a bit easy. Can you find an algorithm with a better complexity for each <code>fetch</code> call?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> Each fetch moves the $k$-th element to the back. When $n$ and the query count are modest, a list deletion plus append is enough.
>
> $\textit{fetch}(k)$ takes index $k-1$, removes it, and appends it.

<!-- thinking:end -->

Use an array to maintain the current queue. For each $\textit{fetch}(k)$, take the $k$-th element, delete it from its current position, append it to the tail, and return it.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the queue.

<!-- tabs:start -->

#### Python3

```python
class MRUQueue:
    def __init__(self, n: int):
        self.q = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        ans = self.q[k - 1]
        self.q[k - 1 : k] = []
        self.q.append(ans)
        return ans

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Indexed Tree + Binary Search

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 deletes in linear time. If we only append and never compact, we must find the $k$-th still-present index quickly.
>
> A Fenwick tree counts how often each index was moved. Binary search the first $i$ with $i-\textit{query}(i)\ge k$, append $q[i]$, and mark $i$ deleted. Each fetch is $O(\log^2 n)$.

<!-- thinking:end -->

We use an array $q$ to maintain the current elements in the queue. When moving the $k$-th element, we do not delete it, but append it to the end of the array. How do we know the position of the $k$-th element in $q$ if we do not delete it?

We can use a Binary Indexed Tree to maintain whether each position in $q$ has been deleted. If the element at position $i$ is deleted, we update the $i$-th position in the tree, indicating that the number of times this position has been moved increases by $1$. Then, each time we want to delete the $k$-th element, we can use binary search to find the first position $i$ that satisfies $i - tree.query(i) \geq k$, which is the position of the $k$-th element in $q$. Let $x = q[i]$, then we append $x$ to the end of $q$ and update the $i$-th position in the tree. Finally, we return $x$.

The time complexity is $O(\log^2 n)$, and the space complexity is $O(n)$, where $n$ is the length of the queue.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] += v
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

class MRUQueue:
    def __init__(self, n: int):
        self.q = list(range(n + 1))
        self.tree = BinaryIndexedTree(n + 2010)

    def fetch(self, k: int) -> int:
        l, r = 1, len(self.q)
        while l < r:
            mid = (l + r) >> 1
            if mid - self.tree.query(mid) >= k:
                r = mid
            else:
                l = mid + 1
        x = self.q[l]
        self.q.append(x)
        self.tree.update(l, 1)
        return x

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
