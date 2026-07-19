---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2100-2199/2179.Count%20Good%20Triplets%20in%20an%20Array/README_EN.md
rating: 2272
source: Biweekly Contest 72 Q4
tags:
    - Binary Indexed Tree
    - Segment Tree
    - Array
    - Binary Search
    - Divide and Conquer
    - Ordered Set
    - Merge Sort
---

<!-- problem:start -->

# [2179. Count Good Triplets in an Array](https://leetcode.com/problems/count-good-triplets-in-an-array)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> arrays <code>nums1</code> and <code>nums2</code> of length <code>n</code>, both of which are <strong>permutations</strong> of <code>[0, 1, ..., n - 1]</code>.</p>

<p>A <strong>good triplet</strong> is a set of <code>3</code> <strong>distinct</strong> values which are present in <strong>increasing order</strong> by position both in <code>nums1</code> and <code>nums2</code>. In other words, if we consider <code>pos1<sub>v</sub></code> as the index of the value <code>v</code> in <code>nums1</code> and <code>pos2<sub>v</sub></code> as the index of the value <code>v</code> in <code>nums2</code>, then a good triplet will be a set <code>(x, y, z)</code> where <code>0 &lt;= x, y, z &lt;= n - 1</code>, such that <code>pos1<sub>x</sub> &lt; pos1<sub>y</sub> &lt; pos1<sub>z</sub></code> and <code>pos2<sub>x</sub> &lt; pos2<sub>y</sub> &lt; pos2<sub>z</sub></code>.</p>

<p>Return <em>the <strong>total number</strong> of good triplets</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,0,1,3], nums2 = [0,1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
There are 4 triplets (x,y,z) such that pos1<sub>x</sub> &lt; pos1<sub>y</sub> &lt; pos1<sub>z</sub>. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2<sub>x</sub> &lt; pos2<sub>y</sub> &lt; pos2<sub>z</sub>. Hence, there is only 1 good triplet.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= n - 1</code></li>
	<li><code>nums1</code> and <code>nums2</code> are permutations of <code>[0, 1, ..., n - 1]</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Indexed Tree (Fenwick Tree)

For this problem, we first use `pos` to record the position of each number in `nums2`, and then process each element in `nums1` sequentially.

Consider the number of good triplets **with the current number as the middle number**. The first number must have already been traversed and must appear earlier than the current number in `nums2`. The third number must not yet have been traversed and must appear later than the current number in `nums2`.

Take `nums1 = [4,0,1,3,2]` and `nums2 = [4,1,0,2,3]` as an example. Consider the traversal process:

1. First, process `4`. At this point, the state of `nums2` is `[4,X,X,X,X]`. The number of values before `4` is `0`, and the number of values after `4` is `4`. Therefore, `4` as the middle number forms `0` good triplets.
2. Next, process `0`. The state of `nums2` becomes `[4,X,0,X,X]`. The number of values before `0` is `1`, and the number of values after `0` is `2`. Therefore, `0` as the middle number forms `2` good triplets.
3. Next, process `1`. The state of `nums2` becomes `[4,1,0,X,X]`. The number of values before `1` is `1`, and the number of values after `1` is `2`. Therefore, `1` as the middle number forms `2` good triplets.
4. ...
5. Finally, process `2`. The state of `nums2` becomes `[4,1,0,2,3]`. The number of values before `2` is `4`, and the number of values after `2` is `0`. Therefore, `2` as the middle number forms `0` good triplets.

We can use a **Binary Indexed Tree (Fenwick Tree)** to update the occurrence of numbers at each position in `nums2`, and quickly calculate the number of `1`s to the left of each number and the number of `0`s to the right of each number.

A Binary Indexed Tree, also known as a Fenwick Tree, efficiently supports the following operations:

1. **Point Update** `update(x, delta)`: Add a value `delta` to the number at position `x` in the sequence.
2. **Prefix Sum Query** `query(x)`: Query the sum of the sequence in the range `[1, ..., x]`, i.e., the prefix sum at position `x`.

Both operations have a time complexity of $O(\log n)$. Therefore, the overall time complexity is $O(n \log n)$, where $n$ is the length of the array $\textit{nums1}$. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += BinaryIndexedTree.lowbit(x)

    def query(self, x):
        s = 0
        while x > 0:
            s += self.c[x]
            x -= BinaryIndexedTree.lowbit(x)
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = {v: i for i, v in enumerate(nums2, 1)}
        ans = 0
        n = len(nums1)
        tree = BinaryIndexedTree(n)
        for num in nums1:
            p = pos[num]
            left = tree.query(p)
            right = n - p - (tree.query(n) - tree.query(p))
            ans += left * right
            tree.update(p, 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Segment Tree

We can also use a segment tree to solve this problem. A segment tree is a data structure that efficiently supports range queries and updates. The basic idea is to divide an interval into multiple subintervals, with each subinterval represented by a node.

The segment tree divides the entire interval into multiple non-overlapping subintervals, with the number of subintervals not exceeding `log(width)`. To update the value of an element, we only need to update `log(width)` intervals, all of which are contained within a larger interval that includes the element.

- Each node of the segment tree represents an interval.
- The segment tree has a unique root node, representing the entire range, such as `[1, N]`.
- Each leaf node of the segment tree represents a unit interval `[x, x]`.
- For each internal node `[l, r]`, its left child represents `[l, mid]`, and its right child represents `[mid + 1, r]`, where `mid = ⌊(l + r) / 2⌋` (floor division).

The time complexity is $O(n \log n)$, where $n$ is the length of the array $\textit{nums1}$. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = ("l", "r", "v")

    def __init__(self):
        self.l = 0
        self.r = 0
        self.v = 0

class SegmentTree:
    def __init__(self, n):
        self.tr = [Node() for _ in range(4 * n)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l = l
        self.tr[u].r = r
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def modify(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].v += v
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def pushup(self, u):
        self.tr[u].v = self.tr[u << 1].v + self.tr[u << 1 | 1].v

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].v
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        v = 0
        if l <= mid:
            v += self.query(u << 1, l, r)
        if r > mid:
            v += self.query(u << 1 | 1, l, r)
        return v

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = {v: i for i, v in enumerate(nums2, 1)}
        ans = 0
        n = len(nums1)
        tree = SegmentTree(n)
        for num in nums1:
            p = pos[num]
            left = tree.query(1, 1, p)
            right = n - p - (tree.query(1, 1, n) - tree.query(1, 1, p))
            ans += left * right
            tree.modify(1, p, 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
