---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1037.Valid%20Boomerang/README_EN.md
rating: 1255
source: Weekly Contest 135 Q1
tags:
    - Geometry
    - Array
    - Math
---

<!-- problem:start -->

# [1037. Valid Boomerang](https://leetcode.com/problems/valid-boomerang)

## Description

<!-- description:start -->

<p>Given an array <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane, return <code>true</code> <em>if these points are a <strong>boomerang</strong></em>.</p>

<p>A <strong>boomerang</strong> is a set of three points that are <strong>all distinct</strong> and <strong>not in a straight line</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> points = [[1,1],[2,3],[3,2]]
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>points.length == 3</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Slope Comparison

Let the three points be $(x_1, y_1)$, $(x_2, y_2)$, and $(x_3, y_3)$. The formula for calculating the slope between two points is $\frac{y_2 - y_1}{x_2 - x_1}$.

To ensure that the three points are not collinear, the condition $\frac{y_2 - y_1}{x_2 - x_1} \neq \frac{y_3 - y_2}{x_3 - x_2}$ must be satisfied. By transforming the equation, we get $(y_2 - y_1) \cdot (x_3 - x_2) \neq (y_3 - y_2) \cdot (x_2 - x_1)$.

Note:

1. When the slope between two points does not exist, i.e., $x_1 = x_2$, the transformed equation still holds.
2. If there are precision issues with division in slope comparison, it can be converted to multiplication.

Time complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
