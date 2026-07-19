---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2613.Beautiful%20Pairs/README_EN.md
tags:
    - Geometry
    - Array
    - Math
    - Divide and Conquer
    - Ordered Set
    - Sorting
---

<!-- problem:start -->

# [2613. Beautiful Pairs 🔒](https://leetcode.com/problems/beautiful-pairs)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code> of the same length. A pair of indices <code>(i,j)</code> is called <strong>beautiful</strong> if<code>|nums1[i] - nums1[j]| + |nums2[i] - nums2[j]|</code> is the smallest amongst all possible indices pairs where <code>i &lt; j</code>.</p>

<p>Return <em>the beautiful pair. In the case that there are multiple beautiful pairs, return the lexicographically smallest pair.</em></p>

<p>Note that</p>

<ul>
	<li><code>|x|</code> denotes the absolute value of <code>x</code>.</li>
	<li>A pair of indices <code>(i<sub>1</sub>, j<sub>1</sub>)</code> is lexicographically smaller than <code>(i<sub>2</sub>, j<sub>2</sub>)</code> if <code>i<sub>1</sub> &lt; i<sub>2</sub></code> or <code>i<sub>1</sub> == i<sub>2</sub></code> and <code>j<sub>1</sub> &lt; j<sub>2</sub></code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,2,4], nums2 = [2,3,1,2,3]
<strong>Output:</strong> [0,3]
<strong>Explanation:</strong> Consider index 0 and index 3. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,4,3,2,5], nums2 = [1,4,2,3,5,1]
<strong>Output:</strong> [1,4]
<strong>Explanation:</strong> Consider index 1 and index 4. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums1.length == nums2.length</code></li>
	<li><code>0 &lt;= nums1<sub>i</sub><sub>&nbsp;</sub>&lt;= nums1.length</code></li>
	<li><code>0 &lt;= nums2<sub>i</sub>&nbsp;&lt;= nums2.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Divide and Conquer

This problem is equivalent to finding two points in the plane, such that the Manhattan distance between them is the smallest. If there are multiple points satisfying the condition, return the one with the smallest index.

First, we handle the case where there are duplicate points. For each point, we record the corresponding indices in a list. If the length of the index list is greater than $1$, then the first two indices in the index list can be used as candidates, and we find the smallest index pair.

If there are no duplicate points, we sort all the points by $x$ coordinates, and then use the divide and conquer to solve the problem.

For each interval $[l, r]$, we first calculate the median of the $x$ coordinates $m$, and then recursively solve the left and right intervals, and get $d_1, (pi_1, pj_1)$ and $d_2, (pi_2, pj_2)$ respectively, where $d_1$ and $d_2$ are the minimum Manhattan distances of the left and right intervals respectively, and $(pi_1, pj_1)$ and $(pi_2, pj_2)$ are the index pairs of the two points of the minimum Manhattan distance of the left and right intervals respectively. We take the smaller one of $d_1$ and $d_2$ as the minimum Manhattan distance of the current interval, and if $d_1 = d_2$, we take the one with the smaller index as the answer. The corresponding two points of the index are taken as the answer.

The above considers the case where the two points are on the same side. If the two points are on different sides, we take the middle point, i.e. the point with the index of $m = \lfloor (l + r) / 2 \rfloor$ as the standard, and divide a new region. The range of this region is to expand the range of $d_1$ from the middle point to the left and right sides respectively. Then we sort these points in the range by $y$ coordinates, and then traverse each point pair in the sorted order. If the difference of the $y$ coordinates of the two points is greater than the current minimum Manhattan distance, then the following point pairs do not need to be considered, because their $y$ coordinate differences are larger, so the Manhattan distance is larger, and it will not be smaller than the current minimum Manhattan distance. Otherwise, we update the minimum Manhattan distance, and update the answer.

Finally, we return the answer.

Time complexity: $O(n \times \log n)$, where $n$ is the length of the array.

Space complexity: $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        def dfs(l: int, r: int):
            if l >= r:
                return inf, -1, -1
            m = (l + r) >> 1
            x = points[m][0]
            d1, pi1, pj1 = dfs(l, m)
            d2, pi2, pj2 = dfs(m + 1, r)
            if d1 > d2 or (d1 == d2 and (pi1 > pi2 or (pi1 == pi2 and pj1 > pj2))):
                d1, pi1, pj1 = d2, pi2, pj2
            t = [p for p in points[l : r + 1] if abs(p[0] - x) <= d1]
            t.sort(key=lambda x: x[1])
            for i in range(len(t)):
                for j in range(i + 1, len(t)):
                    if t[j][1] - t[i][1] > d1:
                        break
                    pi, pj = sorted([t[i][2], t[j][2]])
                    d = dist(t[i][0], t[i][1], t[j][0], t[j][1])
                    if d < d1 or (d == d1 and (pi < pi1 or (pi == pi1 and pj < pj1))):
                        d1, pi1, pj1 = d, pi, pj
            return d1, pi1, pj1

        pl = defaultdict(list)
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            pl[(x, y)].append(i)
        points = []
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if len(pl[(x, y)]) > 1:
                return [i, pl[(x, y)][1]]
            points.append((x, y, i))
        points.sort()
        _, pi, pj = dfs(0, len(points) - 1)
        return [pi, pj]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
