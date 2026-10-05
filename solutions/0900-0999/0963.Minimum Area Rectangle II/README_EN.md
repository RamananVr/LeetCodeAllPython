---
comments: true
difficulty: Medium
tags:
    - Geometry
    - Array
    - Hash Table
    - Math
---

<!-- problem:start -->

# [963. Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii)

## Description

<!-- description:start -->

<p>You are given an array of points in the <strong>X-Y</strong> plane <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.</p>

<p>Return <em>the minimum area of any rectangle formed from these points, with sides <strong>not necessarily parallel</strong> to the X and Y axes</em>. If there is not any such rectangle, return <code>0</code>.</p>

<p>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0963.Minimum%20Area%20Rectangle%20II/images/1a.png" style="width: 398px; height: 400px;" />
<pre>
<strong>Input:</strong> points = [[1,2],[2,1],[1,0],[0,1]]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0963.Minimum%20Area%20Rectangle%20II/images/2.png" style="width: 400px; height: 251px;" />
<pre>
<strong>Input:</strong> points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
<strong>Output:</strong> 1.00000
<strong>Explanation:</strong> The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0963.Minimum%20Area%20Rectangle%20II/images/3.png" style="width: 383px; height: 400px;" />
<pre>
<strong>Input:</strong> points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no possible rectangle to form from these points.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 50</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 4 * 10<sup>4</sup></code></li>
	<li>All the given points are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

<!-- thinking:start -->

> **Thinking**
>
> The smallest area of a (possibly rotated) rectangle, $n\le 50$, allows enumerating three vertices. With a right angle at $p_1$, the fourth corner is the vector sum of the two edges.
>
> The packed key $x \times 40001 + y$ repeats once a coordinate leaves $[0, 4 \times 10^4]$, and the sum of two squared edges exceeds $2^{31}-1$.
>
> Inside that square the key is unique, and those squares fit in a 64-bit integer.
>
> The fourth corner is accepted only when both coordinates lie in range and the key is present. Squared edge lengths are accumulated in 64 bits before the square root.

<!-- thinking:end -->

We use a hash table to store all the points, then enumerate three points $p_1 = (x_1, y_1)$, $p_2 = (x_2, y_2)$, $p_3 = (x_3, y_3)$. If $\overrightarrow{p_1p_2}$ and $\overrightarrow{p_1p_3}$ are perpendicular, the fourth corner is $(x_4, y_4)=(x_2 - x_1 + x_3, y_2 - y_1 + y_3)$. Coordinates lie in $[0, 4 \times 10^4]$, and the packed key $x \times 40001 + y$ is unique only inside that square, so this corner counts only when both coordinates fall in range and the key is present. The squared edge lengths are summed in 64-bit integers, since each sum can exceed $2^{31}-1$, and the area is the square root of their product.

Finally, if a rectangle that satisfies the conditions is found, return the minimum area among them. Otherwise, return $0$.

The time complexity is $O(n^3)$ and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{points}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        s = {(x, y) for x, y in points}
        n = len(points)
        ans = inf
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if j != i:
                    x2, y2 = points[j]
                    for k in range(j + 1, n):
                        if k != i:
                            x3, y3 = points[k]
                            x4 = x2 - x1 + x3
                            y4 = y2 - y1 + y3
                            if 0 <= x4 <= 40000 and 0 <= y4 <= 40000 and (x4, y4) in s:
                                v21 = (x2 - x1, y2 - y1)
                                v31 = (x3 - x1, y3 - y1)
                                if v21[0] * v31[0] + v21[1] * v31[1] == 0:
                                    w = sqrt(v21[0] ** 2 + v21[1] ** 2)
                                    h = sqrt(v31[0] ** 2 + v31[1] ** 2)
                                    ans = min(ans, w * h)
        return 0 if ans == inf else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
