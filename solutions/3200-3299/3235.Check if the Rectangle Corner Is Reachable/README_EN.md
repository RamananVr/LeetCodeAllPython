---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3235.Check%20if%20the%20Rectangle%20Corner%20Is%20Reachable/README_EN.md
rating: 3773
source: Weekly Contest 408 Q4
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Geometry
    - Array
    - Math
---

<!-- problem:start -->

# [3235. Check if the Rectangle Corner Is Reachable](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable)

## Description

<!-- description:start -->

<p>You are given two positive integers <code>xCorner</code> and <code>yCorner</code>, and a 2D array <code>circles</code>, where <code>circles[i] = [x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub>]</code> denotes a circle with center at <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and radius <code>r<sub>i</sub></code>.</p>

<p>There is a rectangle in the coordinate plane with its bottom left corner at the origin and top right corner at the coordinate <code>(xCorner, yCorner)</code>. You need to check whether there is a path from the bottom left corner to the top right corner such that the <strong>entire path</strong> lies inside the rectangle, <strong>does not</strong> touch or lie inside <strong>any</strong> circle, and touches the rectangle <strong>only</strong> at the two corners.</p>

<p>Return <code>true</code> if such a path exists, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">xCorner = 3, yCorner = 4, circles = [[2,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3235.Check%20if%20the%20Rectangle%20Corner%20Is%20Reachable/images/example2circle1.png" style="width: 346px; height: 264px;" /></p>

<p>The black curve shows a possible path between <code>(0, 0)</code> and <code>(3, 4)</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">xCorner = 3, yCorner = 3, circles = [[1,1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3235.Check%20if%20the%20Rectangle%20Corner%20Is%20Reachable/images/example1circle.png" style="width: 346px; height: 264px;" /></p>

<p>No path exists from <code>(0, 0)</code> to <code>(3, 3)</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">xCorner = 3, yCorner = 3, circles = [[2,1,1],[1,2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3235.Check%20if%20the%20Rectangle%20Corner%20Is%20Reachable/images/example0circle.png" style="width: 346px; height: 264px;" /></p>

<p>No path exists from <code>(0, 0)</code> to <code>(3, 3)</code>.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">xCorner = 4, yCorner = 4, circles = [[5,5,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3235.Check%20if%20the%20Rectangle%20Corner%20Is%20Reachable/images/rectangles.png" style="width: 346px; height: 264px;" /></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= xCorner, yCorner &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= circles.length &lt;= 1000</code></li>
	<li><code>circles[i].length == 3</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + Mathematics

According to the problem description, we discuss the following cases:

When there is only one circle in `circles`:

1. If the starting point $(0, 0)$ is inside the circle (including the boundary), or the ending point $(\textit{xCorner}, \textit{yCorner})$ is inside the circle, then it is impossible to satisfy the condition of "not touching the circle".
2. If the circle intersects with the left or top side of the rectangle and also intersects with the right or bottom side of the rectangle, then the circle will block the path from the bottom-left corner to the top-right corner of the rectangle, making it impossible to satisfy the condition of "not touching the circle".

When there are multiple circles in `circles`:

1. Similar to the above case, if the starting point or ending point is inside a circle, it is impossible to satisfy the condition of "not touching the circle".
2. If there are multiple circles, they may intersect within the rectangle, forming a larger obstacle area. As long as this obstacle area intersects with the left or top side of the rectangle and also intersects with the right or bottom side of the rectangle, it is impossible to satisfy the condition of "not touching the circle". If the intersecting area is not inside the rectangle, it cannot be merged because the intersecting area cannot block the path inside the rectangle. Additionally, if part of the intersecting area is inside the rectangle and part is outside, these circles can be used as starting or ending points and can be merged or not. We only need to choose one of the intersecting points. If this point is inside the rectangle, we can merge these circles.

Based on the above analysis, we traverse all circles. For the current circle, if the starting point or ending point is inside the circle, we directly return `false`. Otherwise, if this point has not been visited and the circle intersects with the left or top side of the rectangle, we start a depth-first search (DFS) from this circle. During the search, if we find a circle that intersects with the right or bottom side of the rectangle, it means the obstacle area formed by the circles blocks the path from the bottom-left corner to the top-right corner of the rectangle, and we return `false`.

We define $\textit{dfs}(i)$ to represent starting a DFS from the $i$-th circle. If we find a circle that intersects with the right or bottom side of the rectangle, we return `true`; otherwise, we return `false`.

The execution process of the function $\textit{dfs}(i)$ is as follows:

1. If the current circle intersects with the right or bottom side of the rectangle, return `true`;
2. Otherwise, mark the current circle as visited;
3. Next, traverse all other circles. If circle $j$ has not been visited, and circle $i$ intersects with circle $j$, and one of the intersection points of these two circles is inside the rectangle, continue the DFS from circle $j$. If we find a circle that intersects with the right or bottom side of the rectangle, return `true`;
4. If no such circle is found, return `false`.

In the above process, we need to determine whether two circles $O_1 = (x_1, y_1, r_1)$ and $O_2 = (x_2, y_2, r_2)$ intersect. If the distance between the centers of the two circles does not exceed the sum of their radii, i.e., $(x_1 - x_2)^2 + (y_1 - y_2)^2 \le (r_1 + r_2)^2$, then they intersect.

We also need to find an intersection point of the two circles. We take a point $A = (x, y)$ such that $\frac{O_1 A}{O_1 O_2} = \frac{r_1}{r_1 + r_2}$. If the two circles intersect, point $A$ must be in the intersection. In this case, $\frac{x - x_1}{x_2 - x_1} = \frac{r_1}{r_1 + r_2}$, solving for $x = \frac{x_1 r_2 + x_2 r_1}{r_1 + r_2}$. Similarly, $y = \frac{y_1 r_2 + y_2 r_1}{r_1 + r_2}$. As long as this point is inside the rectangle, we can continue the DFS, satisfying:

$$
\begin{cases}
x_1 r_2 + x_2 r_1 < (r_1 + r_2) \times \textit{xCorner} \\
y_1 r_2 + y_2 r_1 < (r_1 + r_2) \times \textit{yCorner}
\end{cases}
$$

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Here, $n$ is the number of circles.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canReachCorner(
        self, xCorner: int, yCorner: int, circles: List[List[int]]
    ) -> bool:
        def in_circle(x: int, y: int, cx: int, cy: int, r: int) -> int:
            return (x - cx) ** 2 + (y - cy) ** 2 <= r**2

        def cross_left_top(cx: int, cy: int, r: int) -> bool:
            a = abs(cx) <= r and 0 <= cy <= yCorner
            b = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return a or b

        def cross_right_bottom(cx: int, cy: int, r: int) -> bool:
            a = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            b = abs(cy) <= r and 0 <= cx <= xCorner
            return a or b

        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            if cross_right_bottom(x1, y1, r1):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                if vis[j] or not ((x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2):
                    continue
                if (
                    (x1 * r2 + x2 * r1 < (r1 + r2) * xCorner)
                    and (y1 * r2 + y2 * r1 < (r1 + r2) * yCorner)
                    and dfs(j)
                ):
                    return True
            return False

        vis = [False] * len(circles)
        for i, (x, y, r) in enumerate(circles):
            if in_circle(0, 0, x, y, r) or in_circle(xCorner, yCorner, x, y, r):
                return False
            if (not vis[i]) and cross_left_top(x, y, r) and dfs(i):
                return False
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
