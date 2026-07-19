---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2569.Handling%20Sum%20Queries%20After%20Update/README_EN.md
rating: 2397
source: Biweekly Contest 98 Q4
tags:
    - Segment Tree
    - Array
---

<!-- problem:start -->

# [2569. Handling Sum Queries After Update](https://leetcode.com/problems/handling-sum-queries-after-update)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> arrays <code>nums1</code> and <code>nums2</code> and a 2D array <code>queries</code> of queries. There are three types of queries:</p>

<ol>
	<li>For a query of type 1, <code>queries[i]&nbsp;= [1, l, r]</code>. Flip the values from <code>0</code> to <code>1</code> and from <code>1</code> to <code>0</code> in <code>nums1</code>&nbsp;from index <code>l</code> to index <code>r</code>. Both <code>l</code> and <code>r</code> are <strong>0-indexed</strong>.</li>
	<li>For a query of type 2, <code>queries[i]&nbsp;= [2, p, 0]</code>. For every index <code>0 &lt;= i &lt; n</code>, set&nbsp;<code>nums2[i] =&nbsp;nums2[i]&nbsp;+ nums1[i]&nbsp;* p</code>.</li>
	<li>For a query of type 3, <code>queries[i]&nbsp;= [3, 0, 0]</code>. Find the sum of the elements in <code>nums2</code>.</li>
</ol>

<p>Return <em>an array containing all the answers to the third type&nbsp;queries.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
<strong>Output:</strong> [3]
<strong>Explanation:</strong> After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
<strong>Output:</strong> [5]
<strong>Explanation:</strong> After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length,nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums1.length = nums2.length</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code><font face="monospace">queries[i].length = 3</font></code></li>
	<li><code><font face="monospace">0 &lt;= l &lt;= r &lt;= nums1.length - 1</font></code></li>
	<li><code><font face="monospace">0 &lt;= p &lt;= 10<sup>6</sup></font></code></li>
	<li><code>0 &lt;= nums1[i] &lt;= 1</code></li>
	<li><code>0 &lt;= nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree

According to the problem description:

- Operation $1$ is to reverse all numbers in the index range $[l,..r]$ of array `nums1`, that is, change $0$ to $1$ and $1$ to $0$.
- Operation $3$ is to sum all numbers in array `nums2`.
- Operation $2$ is to add the sum of all numbers in array `nums2` with $p$ times the sum of all numbers in array `nums1`, that is, $sum(nums2) = sum(nums2) + p * sum(nums1)$.

Therefore, we actually only need to maintain the segment sum of array `nums1`, which can be implemented through a segment tree.

We define each node of the segment tree as `Node`, each node contains the following attributes:

- `l`: The left endpoint of the node, the index starts from $1$.
- `r`: The right endpoint of the node, the index starts from $1$.
- `s`: The segment sum of the node.
- `lazy`: The lazy tag of the node.

The segment tree mainly has the following operations:

- `build(u, l, r)`: Build the segment tree.
- `pushdown(u)`: Propagate the lazy tag.
- `pushup(u)`: Update the information of the parent node with the information of the child nodes.
- `modify(u, l, r)`: Modify the segment sum. In this problem, it is to reverse each number in the segment, so the segment sum $s = r - l + 1 - s$.
- `query(u, l, r)`: Query the segment sum.

First, calculate the sum of all numbers in array `nums2`, denoted as $s$.

When executing operation $1$, we only need to call `modify(1, l + 1, r + 1)`.

When executing operation $2$, we update $s = s + p \times query(1, 1, n)$.

When executing operation $3$, we just need to add $s$ to the answer array.

The time complexity is $O(n + m \times \log n)$, and the space complexity is $O(n)$. Where $n$ and $m$ are the lengths of arrays `nums1` and `queries` respectively.

<!-- tabs:start -->

#### Python3

```python
class Node:
    def __init__(self):
        self.l = self.r = 0
        self.s = self.lazy = 0

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l == r:
            self.tr[u].s = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def modify(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            self.tr[u].lazy ^= 1
            self.tr[u].s = self.tr[u].r - self.tr[u].l + 1 - self.tr[u].s
            return
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if l <= mid:
            self.modify(u << 1, l, r)
        if r > mid:
            self.modify(u << 1 | 1, l, r)
        self.pushup(u)

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].s
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        res = 0
        if l <= mid:
            res += self.query(u << 1, l, r)
        if r > mid:
            res += self.query(u << 1 | 1, l, r)
        return res

    def pushup(self, u):
        self.tr[u].s = self.tr[u << 1].s + self.tr[u << 1 | 1].s

    def pushdown(self, u):
        if self.tr[u].lazy:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            self.tr[u << 1].s = mid - self.tr[u].l + 1 - self.tr[u << 1].s
            self.tr[u << 1].lazy ^= 1
            self.tr[u << 1 | 1].s = self.tr[u].r - mid - self.tr[u << 1 | 1].s
            self.tr[u << 1 | 1].lazy ^= 1
            self.tr[u].lazy ^= 1

class Solution:
    def handleQuery(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        tree = SegmentTree(nums1)
        s = sum(nums2)
        ans = []
        for op, a, b in queries:
            if op == 1:
                tree.modify(1, a + 1, b + 1)
            elif op == 2:
                s += a * tree.query(1, 1, len(nums1))
            else:
                ans.append(s)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
