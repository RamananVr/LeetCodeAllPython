---
comments: true
difficulty: Easy
tags:
    - Design
    - Array
    - Hash Table
    - Linked List
    - Hash Function
---

<!-- problem:start -->

# [705. Design HashSet](https://leetcode.com/problems/design-hashset)

## Description

<!-- description:start -->

<p>Design a HashSet without using any built-in hash table libraries.</p>

<p>Implement <code>MyHashSet</code> class:</p>

<ul>
	<li><code>void add(key)</code> Inserts the value <code>key</code> into the HashSet.</li>
	<li><code>bool contains(key)</code> Returns whether the value <code>key</code> exists in the HashSet or not.</li>
	<li><code>void remove(key)</code> Removes the value <code>key</code> in the HashSet. If <code>key</code> does not exist in the HashSet, do nothing.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyHashSet&quot;, &quot;add&quot;, &quot;add&quot;, &quot;contains&quot;, &quot;contains&quot;, &quot;add&quot;, &quot;contains&quot;, &quot;remove&quot;, &quot;contains&quot;]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, true, false, null, true, null, false]

<strong>Explanation</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>, <code>remove</code>, and <code>contains</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Static Array Implementation

<!-- thinking:start -->

> **Thinking**
>
> Implement a set of keys in $[0, 10^6]$ with at most $10^4$ operations. A library map would work, but the point is to design the store.
>
> Keys are already non-negative integers with a fixed bound, so they can be indices. A boolean array of length $10^6+1$ turns add, remove, and contains into a single write or read.
>
> Space follows the value range rather than the number of keys; that is acceptable under these limits.

<!-- thinking:end -->

Directly create an array of size $1000001$, initially with each element set to `false`, indicating that the element does not exist in the hash set.

When adding an element to the hash set, set the corresponding position in the array to `true`; when deleting an element, set the corresponding position in the array to `false`; when checking if an element exists, directly return the value at the corresponding position in the array.

The time complexity of the above operations is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class MyHashSet:
    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Array of Linked Lists

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 buys $O(1)$ with an array as large as the key universe; most of that space stays unused when few keys appear.
>
> Hash by a smaller modulus into a fixed number of buckets, and store collisions in a list. Each operation hashes, then scans one short bucket.
>
> With $\textit{SIZE}=1000$ the memory follows the bucket count, and the expected cost stays near constant.

<!-- thinking:end -->

We can also create an array of size $SIZE=1000$, where each position in the array is a linked list.

<!-- tabs:start -->

#### Python3

```python
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        idx = self.hash(key)
        self.data[idx].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        idx = self.hash(key)
        self.data[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        return any(v == key for v in self.data[idx])

    def hash(self, key) -> int:
        return key % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
