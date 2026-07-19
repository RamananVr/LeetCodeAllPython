---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3102.Minimize%20Manhattan%20Distances/README_EN.md
rating: 2215
source: Weekly Contest 391 Q4
tags:
    - Geometry
    - Array
    - Math
    - Ordered Set
    - Sorting
---

<!-- problem:start -->

# [3102. Minimize Manhattan Distances](https://leetcode.com/problems/minimize-manhattan-distances)

## Description

<!-- description:start -->

<p>You are given an array <code>points</code> representing integer coordinates of some points on a 2D plane, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.</p>

<p>The distance between two points is defined as their <span data-keyword="manhattan-distance">Manhattan distance</span>.</p>

<p>Return <em>the <strong>minimum</strong> possible value for <strong>maximum</strong> distance between any two points by removing exactly one point</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[3,10],[5,15],[10,2],[4,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum distance after removing each point is the following:</p>

<ul>
	<li>After removing the 0<sup>th</sup> point the maximum distance is between points (5, 15) and (10, 2), which is <code>|5 - 10| + |15 - 2| = 18</code>.</li>
	<li>After removing the 1<sup>st</sup> point the maximum distance is between points (3, 10) and (10, 2), which is <code>|3 - 10| + |10 - 2| = 15</code>.</li>
	<li>After removing the 2<sup>nd</sup> point the maximum distance is between points (5, 15) and (4, 4), which is <code>|5 - 4| + |15 - 4| = 12</code>.</li>
	<li>After removing the 3<sup>rd</sup> point the maximum distance is between points (5, 15) and (10, 2), which is <code>|5 - 10| + |15 - 2| = 18</code>.</li>
</ul>

<p>12 is the minimum possible maximum distance between any two points after removing exactly one point.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[1,1],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing any of the points results in the maximum distance between any two points of 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>1 &lt;= points[i][0], points[i][1] &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Ordered Set

For two points $(x_1, y_1)$ and $(x_2, y_2)$, their Manhattan distance is $|x_1 - x_2| + |y_1 - y_2|$. We can transform it into $\max(x_1 - x_2, x_2 - x_1) + \max(y_1 - y_2, y_2 - y_1)$, which is:

$$
|x_1 - x_2| + |y_1 - y_2| = \max \begin{cases}
x_1 - x_2 + y_1 - y_2 \\
x_2 - x_1 + y_2 - y_1 \\
x_1 - x_2 + y_2 - y_1 \\
x_2 - x_1 + y_1 - y_2
\end{cases}
$$

This can be simplified to:

$$
|x_1 - x_2| + |y_1 - y_2| = \max \begin{cases}
(x_1 + y_1) - (x_2 + y_2) \\
(x_2 + y_2) - (x_1 + y_1) \\
(x_1 - y_1) - (x_2 - y_2) \\
(x_2 - y_2) - (x_1 - y_1)
\end{cases}
$$

Here, the first two cases can be represented as $\max(\max(x_1 + y_1, x_2 + y_2) - \min(x_1 + y_1, x_2 + y_2))$, and the last two cases can be represented as $\max(\max(x_1 - y_1, x_2 - y_2) - \min(x_1 - y_1, x_2 - y_2))$.

Therefore, we can store all points according to the values of $x + y$ and $x - y$ in two ordered sets, respectively. Then, for each point, we remove it, update the values in the ordered sets, calculate the difference between the maximum and minimum values, and take the minimum value.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of points.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        sl1 = SortedList()
        sl2 = SortedList()
        for x, y in points:
            sl1.add(x + y)
            sl2.add(x - y)
        ans = inf
        for x, y in points:
            sl1.remove(x + y)
            sl2.remove(x - y)
            ans = min(ans, max(sl1[-1] - sl1[0], sl2[-1] - sl2[0]))
            sl1.add(x + y)
            sl2.add(x - y)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
