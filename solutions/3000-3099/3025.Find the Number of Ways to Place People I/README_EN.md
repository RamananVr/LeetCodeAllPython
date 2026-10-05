---
comments: true
difficulty: Medium
rating: 1707
source: Biweekly Contest 123 Q2
tags:
    - Geometry
    - Array
    - Math
    - Enumeration
    - Sorting
---

<!-- problem:start -->

# [3025. Find the Number of Ways to Place People I](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i)

## Description

<!-- description:start -->

<p>You are given a 2D array <code>points</code> of size <code>n x 2</code> representing integer coordinates of some points on a 2D plane, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.</p>

<p>Count the number of pairs of points <code>(A, B)</code>, where</p>

<ul>
	<li><code>A</code> is on the <strong>upper left</strong> side of <code>B</code>, and</li>
	<li>there are no other points in the rectangle (or line) they make (<strong>including the border</strong>), except for the points <code>A</code> and <code>B</code>.</li>
</ul>

<p>Return the count.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[2,2],[3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3000-3099/3025.Find%20the%20Number%20of%20Ways%20to%20Place%20People%20I/images/example1alicebob.png" style="width: 427px; height: 350px;" /></p>

<p>There is no way to choose <code>A</code> and <code>B</code> such that&nbsp;<code>A</code> is on the upper left side of <code>B</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[6,2],[4,4],[2,6]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img height="365" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3000-3099/3025.Find%20the%20Number%20of%20Ways%20to%20Place%20People%20I/images/t2.jpg" width="1321" /></p>

<ul>
	<li>The left one is the pair <code>(points[1], points[0])</code>, where <code>points[1]</code> is on the upper left side of <code>points[0]</code> and the rectangle is empty.</li>
	<li>The middle one is the pair <code>(points[2], points[1])</code>, same as the left one it is a valid pair.</li>
	<li>The right one is the pair <code>(points[2], points[0])</code>, where <code>points[2]</code> is on the upper left side of <code>points[0]</code>, but <code>points[1]</code> is inside the rectangle so it&#39;s not a valid pair.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[3,1],[1,3],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3000-3099/3025.Find%20the%20Number%20of%20Ways%20to%20Place%20People%20I/images/t3.jpg" style="width: 1269px; height: 350px;" /></p>

<ul>
	<li>The left one is the pair <code>(points[2], points[0])</code>, where <code>points[2]</code> is on the upper left side of <code>points[0]</code> and there are no other points on the line they form. Note that it is a valid state when the two points form a line.</li>
	<li>The middle one is the pair <code>(points[1], points[2])</code>, it is a valid pair same as the left one.</li>
	<li>The right one is the pair <code>(points[1], points[0])</code>, it is not a valid pair as <code>points[2]</code> is on the border of the rectangle.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 50</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= points[i][0], points[i][1] &lt;= 50</code></li>
	<li>All <code>points[i]</code> are distinct.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting and Enumeration

<!-- thinking:start -->

> **Thinking**
>
> $n \le 50$. Enumerating an upper-left and a lower-right corner and scanning the box is $O(n^3)$ and would pass, but repeats a lot of work.
>
> After sorting by increasing $x$ and, on ties, decreasing $y$, a valid lower-right $y$ must strictly increase as $x$ grows, or the new point would sit inside an earlier rectangle.
>
> For each upper-left point we keep the largest chosen $y_2$ and count a pair only when $\textit{maxY} < y_2 \le y_1$.

<!-- thinking:end -->

Enumerate the upper-left point $(x_1, y_1)$. A later point $(x_2, y_2)$ is a valid lower-right corner only when its $y$ is strictly larger than the $y$ of every lower-right point already accepted; otherwise it lies inside a rectangle that has already been formed.

Sort the points by increasing $x$. When two points share $x$, sort them by decreasing $y$.

For each upper-left point $(x_1, y_1)$, maintain $\textit{maxY}$, the largest $y$ among accepted lower-right points. Scan the following points $(x_2, y_2)$. If $\textit{maxY} < y_2 \le y_1$, the pair is valid: add one to the answer and set $\textit{maxY} = y_2$.

After every upper-left point has been scanned, the answer is complete.

The time complexity is $O(n^2)$, and the space complexity is $O(\log n)$. Here, $n$ is the number of points.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for _, y2 in points[i + 1 :]:
                if max_y < y2 <= y1:
                    max_y = y2
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
