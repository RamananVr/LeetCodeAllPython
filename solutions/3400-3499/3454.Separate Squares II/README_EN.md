---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3454.Separate%20Squares%20II/README_EN.md
rating: 2671
source: Biweekly Contest 150 Q3
tags:
    - Segment Tree
    - Array
    - Binary Search
    - Sweep Line
---

<!-- problem:start -->

# [3454. Separate Squares II](https://leetcode.com/problems/separate-squares-ii)

## Description

<!-- description:start -->

<p>You are given a 2D integer array <code>squares</code>. Each <code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code> represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.</p>

<p>Find the <strong>minimum</strong> y-coordinate value of a horizontal line such that the total area covered by squares above the line <em>equals</em> the total area covered by squares below the line.</p>

<p>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p><strong>Note</strong>: Squares <strong>may</strong> overlap. Overlapping areas should be counted <strong>only once</strong> in this version.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">squares = [[0,0,1],[2,2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.00000</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3400-3499/3454.Separate%20Squares%20II/images/4065example1drawio.png" style="width: 269px; height: 203px;" /></p>

<p>Any horizontal line between <code>y = 1</code> and <code>y = 2</code> results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">squares = [[0,0,2],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.00000</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3400-3499/3454.Separate%20Squares%20II/images/4065example2drawio.png" style="width: 269px; height: 203px;" /></p>

<p>Since the blue square overlaps with the red square, it will not be counted again. Thus, the line <code>y = 1</code> splits the squares into two equal parts.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= squares.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code></li>
	<li><code>squares[i].length == 3</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li>The total area of all the squares will not exceed <code>10<sup>15</sup></code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sweep Line

This problem can be solved using the sweep line algorithm to calculate the total area of all squares.

We treat the top and bottom boundaries of each square as event points for the sweep line, sorted by $y$ coordinate in ascending order. For each event point, we use a segment tree to maintain the length of the covered $x$-axis interval below the current sweep line, allowing us to calculate the area increment between the current sweep line and the previous one.

The specific steps are as follows:

1. **Preprocess Event Points**: For each square, calculate the $y$ coordinates of its top and bottom boundaries and add them as event points to the event list. Each event point contains the $y$ coordinate, left boundary $x_1$, right boundary $x_2$, and a flag (indicating whether it's the top or bottom boundary).
2. **Sort Event Points**: Sort all event points by $y$ coordinate in ascending order.
3. **Build Segment Tree**: Build a segment tree using the discretized $x$ coordinates to maintain the length of the currently covered $x$-axis intervals.
4. **Scan Event Points**: Traverse the sorted event point list. For each event point:
    - Calculate the area increment between the current event point and the previous one, and add it to the total area.
    - Based on the type of the current event point (top or bottom boundary), update the segment tree by increasing or decreasing the coverage count of the corresponding $x$-axis interval.
5. **Calculate Target Area**: The target area is half of the total area.
6. **Scan Event Points Again**: Traverse the event point list again, calculating the cumulative area. When the cumulative area reaches the target area, calculate and return the corresponding $y$ coordinate.

The time complexity is $O(n \times \log n)$ and the space complexity is $O(n)$, where $n$ is the number of squares.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = ("l", "r", "cnt", "length")

    def __init__(self):
        self.l = self.r = 0
        self.cnt = self.length = 0

class SegmentTree:
    def __init__(self, nums):
        n = len(nums) - 1
        self.nums = nums
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 0, n - 1)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l != r:
            mid = (l + r) >> 1
            self.build(u << 1, l, mid)
            self.build(u << 1 | 1, mid + 1, r)

    def modify(self, u, l, r, k):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            self.tr[u].cnt += k
        else:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            if l <= mid:
                self.modify(u << 1, l, r, k)
            if r > mid:
                self.modify(u << 1 | 1, l, r, k)
        self.pushup(u)

    def pushup(self, u):
        if self.tr[u].cnt:
            self.tr[u].length = self.nums[self.tr[u].r + 1] - self.nums[self.tr[u].l]
        elif self.tr[u].l == self.tr[u].r:
            self.tr[u].length = 0
        else:
            self.tr[u].length = self.tr[u << 1].length + self.tr[u << 1 | 1].length

    @property
    def length(self):
        return self.tr[1].length

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = set()
        segs = []
        for x1, y1, l in squares:
            x2, y2 = x1 + l, y1 + l
            xs.update([x1, x2])
            segs.append((y1, x1, x2, 1))
            segs.append((y2, x1, x2, -1))
        segs.sort()
        st = sorted(xs)
        tree = SegmentTree(st)
        d = {x: i for i, x in enumerate(st)}
        area = 0
        y0 = 0
        for y, x1, x2, k in segs:
            area += (y - y0) * tree.length
            tree.modify(1, d[x1], d[x2] - 1, k)
            y0 = y

        target = area / 2
        area = 0
        y0 = 0
        for y, x1, x2, k in segs:
            t = (y - y0) * tree.length
            if area + t >= target:
                return y0 + (target - area) / tree.length
            area += t
            tree.modify(1, d[x1], d[x2] - 1, k)
            y0 = y
        return 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
