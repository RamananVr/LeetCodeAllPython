---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1931.Painting%20a%20Grid%20With%20Three%20Different%20Colors/README_EN.md
rating: 2170
source: Weekly Contest 249 Q3
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [1931. Painting a Grid With Three Different Colors](https://leetcode.com/problems/painting-a-grid-with-three-different-colors)

## Description

<!-- description:start -->

<p>You are given two integers <code>m</code> and <code>n</code>. Consider an <code>m x n</code> grid where each cell is initially white. You can paint each cell <strong>red</strong>, <strong>green</strong>, or <strong>blue</strong>. All cells <strong>must</strong> be painted.</p>

<p>Return<em> the number of ways to color the grid with <strong>no two adjacent cells having the same color</strong></em>. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1931.Painting%20a%20Grid%20With%20Three%20Different%20Colors/images/colorthegrid.png" style="width: 200px; height: 50px;" />
<pre>
<strong>Input:</strong> m = 1, n = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The three possible colorings are shown in the image above.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1931.Painting%20a%20Grid%20With%20Three%20Different%20Colors/images/copy-of-colorthegrid.png" style="width: 321px; height: 121px;" />
<pre>
<strong>Input:</strong> m = 1, n = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The six possible colorings are shown in the image above.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> m = 5, n = 5
<strong>Output:</strong> 580986
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m &lt;= 5</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: State Compression + Dynamic Programming

We notice that the number of rows in the grid does not exceed $5$, so there are at most $3^5=243$ different color schemes in a column.

Therefore, we define $f[i][j]$ to represent the number of schemes in the first $i$ columns, where the coloring state of the $i$th column is $j$. The state $f[i][j]$ is transferred from $f[i - 1][k]$, where $k$ is the coloring state of the $i - 1$th column, and $k$ and $j$ meet the requirement of different colors being adjacent. That is:

$$
f[i][j] = \sum_{k \in \textit{valid}(j)} f[i - 1][k]
$$

where $\textit{valid}(j)$ represents all legal predecessor states of state $j$.

The final answer is the sum of $f[n][j]$, where $j$ is any legal state.

We notice that $f[i][j]$ is only related to $f[i - 1][k]$, so we can use a rolling array to optimize the space complexity.

The time complexity is $O((m + n) \times 3^{2m})$, and the space complexity is $O(3^m)$. Here, $m$ and $n$ are the number of rows and columns of the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def f1(x: int) -> bool:
            last = -1
            for _ in range(m):
                if x % 3 == last:
                    return False
                last = x % 3
                x //= 3
            return True

        def f2(x: int, y: int) -> bool:
            for _ in range(m):
                if x % 3 == y % 3:
                    return False
                x, y = x // 3, y // 3
            return True

        mod = 10**9 + 7
        mx = 3**m
        valid = {i for i in range(mx) if f1(i)}
        d = defaultdict(list)
        for x in valid:
            for y in valid:
                if f2(x, y):
                    d[x].append(y)
        f = [int(i in valid) for i in range(mx)]
        for _ in range(n - 1):
            g = [0] * mx
            for i in valid:
                for j in d[i]:
                    g[i] = (g[i] + f[j]) % mod
            f = g
        return sum(f) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
