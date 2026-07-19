---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1102.Path%20With%20Maximum%20Minimum%20Value/README_EN.md
rating: 2011
source: Biweekly Contest 3 Q4
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Array
    - Binary Search
    - Matrix
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1102. Path With Maximum Minimum Value 🔒](https://leetcode.com/problems/path-with-maximum-minimum-value)

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> integer matrix <code>grid</code>, return <em>the maximum <strong>score</strong> of a path starting at </em><code>(0, 0)</code><em> and ending at </em><code>(m - 1, n - 1)</code> moving in the 4 cardinal directions.</p>

<p>The <strong>score</strong> of a path is the minimum value in that path.</p>

<ul>
	<li>For example, the score of the path <code>8 &rarr; 4 &rarr; 5 &rarr; 9</code> is <code>4</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1102.Path%20With%20Maximum%20Minimum%20Value/images/maxgrid1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> grid = [[5,4,5],[1,2,6],[7,4,6]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The path with the maximum score is highlighted in yellow. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1102.Path%20With%20Maximum%20Minimum%20Value/images/maxgrid2.jpg" style="width: 484px; height: 165px;" />
<pre>
<strong>Input:</strong> grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1102.Path%20With%20Maximum%20Minimum%20Value/images/maxgrid3.jpg" style="width: 404px; height: 485px;" />
<pre>
<strong>Input:</strong> grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Union-Find

First, we construct a triplet $(v, i, j)$ for each element in the matrix, where $v$ represents the element value, and $i$ and $j$ represent the row and column of the element in the matrix, respectively. Then we sort these triplets in descending order by element value and store them in a list $q$.

Next, we take out the triplets from $q$ in order, use the corresponding element value as the score of the path, and mark the position as visited. Then we check the four adjacent positions (up, down, left, and right) of this position. If an adjacent position has been visited, we merge this position with the current position. If we find that the position $(0, 0)$ and the position $(m - 1, n - 1)$ have been merged, we can directly return the score of the current path as the answer.

The time complexity is $O(m \times n \times (\log (m \times n) + \alpha(m \times n)))$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        m, n = len(grid), len(grid[0])
        p = list(range(m * n))
        q = [(v, i, j) for i, row in enumerate(grid) for j, v in enumerate(row)]
        q.sort()
        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        vis = set()
        while find(0) != find(m * n - 1):
            v, i, j = q.pop()
            ans = v
            vis.add((i, j))
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if (x, y) in vis:
                    p[find(i * n + j)] = find(x * n + y)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    __slots__ = ("p", "size")

    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        q = [(v, i, j) for i, row in enumerate(grid) for j, v in enumerate(row)]
        q.sort()
        ans = 0
        vis = set()
        dirs = (-1, 0, 1, 0, -1)
        while uf.find(0) != uf.find(m * n - 1):
            v, i, j = q.pop()
            ans = v
            vis.add((i, j))
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if (x, y) in vis:
                    uf.union(x * n + y, i * n + j)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
