---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3143.Maximum%20Points%20Inside%20the%20Square/README_EN.md
rating: 1696
source: Biweekly Contest 130 Q2
tags:
    - Array
    - Hash Table
    - String
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [3143. Maximum Points Inside the Square](https://leetcode.com/problems/maximum-points-inside-the-square)

## Description

<!-- description:start -->

<p>You are given a 2D<strong> </strong>array <code>points</code> and a string <code>s</code> where, <code>points[i]</code> represents the coordinates of point <code>i</code>, and <code>s[i]</code> represents the <strong>tag</strong> of point <code>i</code>.</p>

<p>A <strong>valid</strong> square is a square centered at the origin <code>(0, 0)</code>, has edges parallel to the axes, and <strong>does not</strong> contain two points with the same tag.</p>

<p>Return the <strong>maximum</strong> number of points contained in a <strong>valid</strong> square.</p>

<p>Note:</p>

<ul>
	<li>A point is considered to be inside the square if it lies on or within the square&#39;s boundaries.</li>
	<li>The side length of the square can be zero.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3100-3199/3143.Maximum%20Points%20Inside%20the%20Square/images/3708-tc1.png" style="width: 303px; height: 303px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = &quot;abdca&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The square of side length 4 covers two points <code>points[0]</code> and <code>points[1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3100-3199/3143.Maximum%20Points%20Inside%20the%20Square/images/3708-tc2.png" style="width: 302px; height: 302px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[-2,-2],[-2,2]], s = &quot;abb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The square of side length 2 covers one point, which is <code>points[0]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[-1,-1],[2,-2]], s = &quot;ccd&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>It&#39;s impossible to make any valid squares centered at the origin such that it covers only one point among <code>points[0]</code> and <code>points[1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>9</sup> &lt;= points[i][0], points[i][1] &lt;= 10<sup>9</sup></code></li>
	<li><code>s.length == points.length</code></li>
	<li><code>points</code> consists of distinct coordinates.</li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

For a point $(x, y)$, we can map it to the first quadrant with the origin as the center, i.e., $(\max(|x|, |y|), \max(|x|, |y|))$. In this way, we can map all points to the first quadrant and then sort them according to the distance from the point to the origin.

We can use a hash table $g$ to store the distance from all points to the origin, and then sort them according to the distance. For each distance $d$, we put all points with a distance of $d$ together, and then traverse these points. If there are two points with the same label, then this square is illegal, and we directly return the answer. Otherwise, we add these points to the answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the number of points.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        g = defaultdict(list)
        for i, (x, y) in enumerate(points):
            g[max(abs(x), abs(y))].append(i)
        vis = set()
        ans = 0
        for d in sorted(g):
            idx = g[d]
            for i in idx:
                if s[i] in vis:
                    return ans
                vis.add(s[i])
            ans += len(idx)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
