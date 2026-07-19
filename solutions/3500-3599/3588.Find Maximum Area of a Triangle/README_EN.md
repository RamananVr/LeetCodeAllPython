---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3588.Find%20Maximum%20Area%20of%20a%20Triangle/README_EN.md
rating: 1818
source: Biweekly Contest 159 Q2
tags:
    - Greedy
    - Geometry
    - Array
    - Hash Table
    - Math
    - Enumeration
---

<!-- problem:start -->

# [3588. Find Maximum Area of a Triangle](https://leetcode.com/problems/find-maximum-area-of-a-triangle)

## Description

<!-- description:start -->

<p>You are given a 2D array <code>coords</code> of size <code>n x 2</code>, representing the coordinates of <code>n</code> points in an infinite Cartesian plane.</p>

<p>Find <strong>twice</strong> the <strong>maximum</strong> area of a triangle with its corners at <em>any</em> three elements from <code>coords</code>, such that at least one side of this triangle is <strong>parallel</strong> to the x-axis or y-axis. Formally, if the maximum area of such a triangle is <code>A</code>, return <code>2 * A</code>.</p>

<p>If no such triangle exists, return -1.</p>

<p><strong>Note</strong> that a triangle <em>cannot</em> have zero area.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coords = [[1,1],[1,2],[3,2],[3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3500-3599/3588.Find%20Maximum%20Area%20of%20a%20Triangle/images/image-20250420010047-1.png" style="width: 300px; height: 289px;" /></p>

<p>The triangle shown in the image has a base 1 and height 2. Hence its area is <code>1/2 * base * height = 1</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coords = [[1,1],[2,2],[3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible triangle has corners <code>(1, 1)</code>, <code>(2, 2)</code>, and <code>(3, 3)</code>. None of its sides are parallel to the x-axis or the y-axis.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == coords.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coords[i][0], coords[i][1] &lt;= 10<sup>6</sup></code></li>
	<li>All <code>coords[i]</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Hash Map

The problem asks for twice the area of the triangle, so we can directly calculate the product of the base and height of the triangle.

Since the triangle must have at least one side parallel to the $x$-axis or $y$-axis, we can enumerate sides parallel to the $x$-axis and calculate the double area for all possible triangles, then swap the coordinates in $\textit{coords}$ and repeat the process to calculate the double area for triangles with sides parallel to the $y$-axis.

Therefore, we design a function $\textit{calc}$ to calculate the double area for all possible triangles with sides parallel to the $y$-axis.

We use two hash maps $\textit{f}$ and $\textit{g}$ to record the minimum and maximum $y$-coordinates for each $x$-coordinate. Then we iterate through $\textit{coords}$, updating $\textit{f}$ and $\textit{g}$, and also record the minimum and maximum $x$-coordinates. Finally, we iterate through $\textit{f}$, calculate the double area for each $x$-coordinate, and update the answer.

In the main function, we first call the $\textit{calc}$ function to calculate the double area for triangles with sides parallel to the $y$-axis, then swap the coordinates in $\textit{coords}$ and repeat the process to calculate the double area for triangles with sides parallel to the $x$-axis. Finally, we return the answer; if the answer is 0, we return -1.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of $\textit{coords}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        def calc() -> int:
            mn, mx = inf, 0
            f = {}
            g = {}
            for x, y in coords:
                mn = min(mn, x)
                mx = max(mx, x)
                if x in f:
                    f[x] = min(f[x], y)
                    g[x] = max(g[x], y)
                else:
                    f[x] = g[x] = y
            ans = 0
            for x, y in f.items():
                d = g[x] - y
                ans = max(ans, d * max(mx - x, x - mn))
            return ans

        ans = calc()
        for c in coords:
            c[0], c[1] = c[1], c[0]
        ans = max(ans, calc())
        return ans if ans else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
