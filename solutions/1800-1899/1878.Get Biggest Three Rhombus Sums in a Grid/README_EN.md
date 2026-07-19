---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1878.Get%20Biggest%20Three%20Rhombus%20Sums%20in%20a%20Grid/README_EN.md
rating: 1897
source: Biweekly Contest 53 Q3
tags:
    - Array
    - Math
    - Matrix
    - Prefix Sum
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1878. Get Biggest Three Rhombus Sums in a Grid](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> integer matrix <code>grid</code>​​​.</p>

<p>A <strong>rhombus sum</strong> is the sum of the elements that form <strong>the</strong> <strong>border</strong> of a regular rhombus shape in <code>grid</code>​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each <strong>rhombus sum</strong>:</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1800-1899/1878.Get%20Biggest%20Three%20Rhombus%20Sums%20in%20a%20Grid/images/pc73-q4-desc-2.png" style="width: 385px; height: 385px;" />
<p>Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.</p>

<p>Return <em>the biggest three <strong>distinct rhombus sums</strong> in the </em><code>grid</code><em> in <strong>descending order</strong></em><em>. If there are less than three distinct values, return all of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1800-1899/1878.Get%20Biggest%20Three%20Rhombus%20Sums%20in%20a%20Grid/images/pc73-q4-ex1.png" style="width: 360px; height: 361px;" />
<pre>
<strong>Input:</strong> grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
<strong>Output:</strong> [228,216,211]
<strong>Explanation:</strong> The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1800-1899/1878.Get%20Biggest%20Three%20Rhombus%20Sums%20in%20a%20Grid/images/pc73-q4-ex2.png" style="width: 217px; height: 217px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [20,9,8]
<strong>Explanation:</strong> The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[7,7,7]]
<strong>Output:</strong> [7]
<strong>Explanation:</strong> All three possible rhombus sums are the same, so return [7].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate Diamond Center + Prefix Sum + Ordered Set

We can preprocess to get two prefix sum arrays $s_1$ and $s_2$, where $s_1[i][j]$ represents the sum of the elements on the upper left diagonal ending at $(i, j)$, and $s_2[i][j]$ represents the sum of the elements on the upper right diagonal ending at $(i, j)$.

Next, we enumerate each position $(i, j)$, first add $grid[i][j]$ to the ordered set $ss$, and then enumerate the length $k$ of the diamond. The sum of the diamond with $(i, j)$ as the center and a side length of $k$ is:

$$
\begin{aligned}
&\quad s_1[i + k][j] - s_1[i][j - k] + s_1[i][j + k] - s_1[i - k][j] \\
&+ s_2[i][j - k] - s_2[i - k][j] + s_2[i + k][j] - s_2[i][j + k] \\
&- grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
\end{aligned}
$$

We add this value to the ordered set $ss$, while ensuring that the size of the ordered set $ss$ does not exceed $3$. Finally, we output the elements in the ordered set $ss$ in reverse order.

The time complexity is $O(m \times n \times \min(m, n))$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        s1 = [[0] * (n + 2) for _ in range(m + 1)]
        s2 = [[0] * (n + 2) for _ in range(m + 1)]
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                s1[i][j] = s1[i - 1][j - 1] + x
                s2[i][j] = s2[i - 1][j + 1] + x
        ss = SortedSet()
        for i, row in enumerate(grid, 1):
            for j, x in enumerate(row, 1):
                l = min(i - 1, m - i, j - 1, n - j)
                ss.add(x)
                for k in range(1, l + 1):
                    a = s1[i + k][j] - s1[i][j - k]
                    b = s1[i][j + k] - s1[i - k][j]
                    c = s2[i][j - k] - s2[i - k][j]
                    d = s2[i + k][j] - s2[i][j + k]
                    ss.add(
                        a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
                    )
                while len(ss) > 3:
                    ss.remove(ss[0])
        return list(ss)[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
