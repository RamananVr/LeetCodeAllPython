---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3464.Maximize%20the%20Distance%20Between%20Points%20on%20a%20Square/README_EN.md
rating: 2805
source: Weekly Contest 438 Q4
tags:
    - Geometry
    - Array
    - Math
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [3464. Maximize the Distance Between Points on a Square](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square)

## Description

<!-- description:start -->

<p>You are given an integer <code><font face="monospace">side</font></code>, representing the edge length of a square with corners at <code>(0, 0)</code>, <code>(0, side)</code>, <code>(side, 0)</code>, and <code>(side, side)</code> on a Cartesian plane.</p>

<p>You are also given a <strong>positive</strong> integer <code>k</code> and a 2D integer array <code>points</code>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinate of a point lying on the <strong>boundary</strong> of the square.</p>

<p>You need to select <code>k</code> elements among <code>points</code> such that the <strong>minimum</strong> Manhattan distance between any two points is <strong>maximized</strong>.</p>

<p>Return the <strong>maximum</strong> possible <strong>minimum</strong> Manhattan distance between the selected <code>k</code> points.</p>

<p>The Manhattan Distance between two cells <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and <code>(x<sub>j</sub>, y<sub>j</sub>)</code> is <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3400-3499/3464.Maximize%20the%20Distance%20Between%20Points%20on%20a%20Square/images/4080_example0_revised.png" style="width: 200px; height: 200px;" /></p>

<p>Select all four points.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3400-3499/3464.Maximize%20the%20Distance%20Between%20Points%20on%20a%20Square/images/4080_example1_revised.png" style="width: 211px; height: 200px;" /></p>

<p>Select the points <code>(0, 0)</code>, <code>(2, 0)</code>, <code>(2, 2)</code>, and <code>(2, 1)</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3400-3499/3464.Maximize%20the%20Distance%20Between%20Points%20on%20a%20Square/images/4080_example2_revised.png" style="width: 200px; height: 200px;" /></p>

<p>Select the points <code>(0, 0)</code>, <code>(0, 1)</code>, <code>(0, 2)</code>, <code>(1, 2)</code>, and <code>(2, 2)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= side &lt;= 10<sup>9</sup></code></li>
	<li><code>4 &lt;= points.length &lt;= min(4 * side, 15 * 10<sup>3</sup>)</code></li>
	<li><code>points[i] == [x<sub>i</sub>, y<sub>i</sub>]</code></li>
	<li>The input is generated such that:
	<ul>
		<li><code>points[i]</code> lies on the boundary of the square.</li>
		<li>All <code>points[i]</code> are <strong>unique</strong>.</li>
	</ul>
	</li>
	<li><code>4 &lt;= k &lt;= min(25, points.length)</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search + Coordinate Mapping + Greedy

Since the problem asks to maximize the minimum distance, we can use binary search on the answer to find the optimal solution.

First, to simplify the logic, we map the 2D coordinates $(x, y)$ on the square's boundary to a 1D axis $[0, 4 \times \text{side})$. The mapping rules are as follows:

- If $x = 0$, the mapped value is $y$;
- If $y = \text{side}$, the mapped value is $\text{side} + x$;
- If $x = \text{side}$, the mapped value is $3 \times \text{side} - y$;
- Otherwise, the mapped value is $4 \times \text{side} - x$.

After mapping, sort all the points to obtain the array $\textit{nums}$. Since the points are selected on the perimeter of the square, this is essentially a circular (ring) problem.

During the binary search, for a given minimum distance $\textit{lo}$, we use a $\textit{check}$ function to verify its feasibility:

- Iterate through each point in $\textit{nums}$ as the starting point $\textit{start}$.
- The endpoint for selecting points is $\textit{end} = \textit{start} + 4 \times \text{side} - \textit{lo}$, ensuring that the wrap-around distance from the last selected point back to $\textit{start}$ is at least $\textit{lo}$.
- Then, greedily perform $k-1$ jumps, each time using binary search to quickly locate the next point that is at least $\textit{lo}$ away from the current position.
- If it is possible to select $k$ points within the $\textit{end}$ limit, then the distance $\textit{lo}$ is feasible.

The time complexity is $O(n \log (\text{side}) \cdot n \log n)$ and the space complexity is $O(n)$, where $n$ is the length of the $\textit{points}$ array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        nums = []
        for x, y in points:
            if x == 0:
                nums.append(y)
            elif y == side:
                nums.append(side + x)
            elif x == side:
                nums.append(side * 3 - y)
            else:
                nums.append(side * 4 - x)
        nums.sort()

        def check(lo: int) -> bool:
            for start in nums:
                end = start + side * 4 - lo
                cur = start
                ok = True
                for _ in range(k - 1):
                    j = bisect_left(nums, cur + lo)
                    if j == len(nums) or nums[j] > end:
                        ok = False
                        break
                    cur = nums[j]
                if ok:
                    return True
            return False

        l, r = 1, side
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
