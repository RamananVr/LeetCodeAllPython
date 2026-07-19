---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3479.Fruits%20Into%20Baskets%20III/README_EN.md
rating: 2178
source: Weekly Contest 440 Q3
tags:
    - Segment Tree
    - Array
    - Binary Search
    - Ordered Set
---

<!-- problem:start -->

# [3479. Fruits Into Baskets III](https://leetcode.com/problems/fruits-into-baskets-iii)

## Description

<!-- description:start -->

<p>You are given two arrays of integers, <code>fruits</code> and <code>baskets</code>, each of length <code>n</code>, where <code>fruits[i]</code> represents the <strong>quantity</strong> of the <code>i<sup>th</sup></code> type of fruit, and <code>baskets[j]</code> represents the <strong>capacity</strong> of the <code>j<sup>th</sup></code> basket.</p>

<p>From left to right, place the fruits according to these rules:</p>

<ul>
	<li>Each fruit type must be placed in the <strong>leftmost available basket</strong> with a capacity <strong>greater than or equal</strong> to the quantity of that fruit type.</li>
	<li>Each basket can hold <b>only one</b> type of fruit.</li>
	<li>If a fruit type <b>cannot be placed</b> in any basket, it remains <b>unplaced</b>.</li>
</ul>

<p>Return the number of fruit types that remain unplaced after all possible allocations are made.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">fruits = [4,2,5], baskets = [3,5,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>fruits[0] = 4</code> is placed in <code>baskets[1] = 5</code>.</li>
	<li><code>fruits[1] = 2</code> is placed in <code>baskets[0] = 3</code>.</li>
	<li><code>fruits[2] = 5</code> cannot be placed in <code>baskets[2] = 4</code>.</li>
</ul>

<p>Since one fruit type remains unplaced, we return 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">fruits = [3,6,1], baskets = [6,4,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>fruits[0] = 3</code> is placed in <code>baskets[0] = 6</code>.</li>
	<li><code>fruits[1] = 6</code> cannot be placed in <code>baskets[1] = 4</code> (insufficient capacity) but can be placed in the next available basket, <code>baskets[2] = 7</code>.</li>
	<li><code>fruits[2] = 1</code> is placed in <code>baskets[1] = 4</code>.</li>
</ul>

<p>Since all fruits are successfully placed, we return 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == fruits.length == baskets.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= fruits[i], baskets[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree Binary Search

We can use a segment tree to maintain the maximum basket capacity in an interval, which allows us to quickly find the first basket with capacity greater than or equal to the fruit quantity through binary search. If no such basket is found, we increment the answer by one; if found, we set that basket's capacity to zero, indicating that the basket has been used.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of $\textit{baskets}$.

<!-- tabs:start -->

#### Python3

```python
class SegmentTree:
    __slots__ = ["nums", "tr"]

    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tr = [0] * (n << 2)
        self.build(1, 1, n)

    def build(self, u, l, r):
        if l == r:
            self.tr[u] = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def modify(self, u, l, r, i, v):
        if l == r:
            self.tr[u] = v
            return
        mid = (l + r) >> 1
        if i <= mid:
            self.modify(u << 1, l, mid, i, v)
        else:
            self.modify(u << 1 | 1, mid + 1, r, i, v)
        self.pushup(u)

    def query(self, u, l, r, v):
        if self.tr[u] < v:
            return -1
        if l == r:
            return l
        mid = (l + r) >> 1
        if self.tr[u << 1] >= v:
            return self.query(u << 1, l, mid, v)
        return self.query(u << 1 | 1, mid + 1, r, v)

    def pushup(self, u):
        self.tr[u] = max(self.tr[u << 1], self.tr[u << 1 | 1])

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegmentTree(baskets)
        n = len(baskets)
        ans = 0
        for x in fruits:
            i = tree.query(1, 1, n, x)
            if i < 0:
                ans += 1
            else:
                tree.modify(1, 1, n, i, 0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
