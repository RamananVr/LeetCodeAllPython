---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1970.Last%20Day%20Where%20You%20Can%20Still%20Cross/README_EN.md
rating: 2123
source: Weekly Contest 254 Q4
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Array
    - Binary Search
    - Matrix
---

<!-- problem:start -->

# [1970. Last Day Where You Can Still Cross](https://leetcode.com/problems/last-day-where-you-can-still-cross)

## Description

<!-- description:start -->

<p>There is a <strong>1-based</strong> binary matrix where <code>0</code> represents land and <code>1</code> represents water. You are given integers <code>row</code> and <code>col</code> representing the number of rows and columns in the matrix, respectively.</p>

<p>Initially on day <code>0</code>, the <strong>entire</strong> matrix is <strong>land</strong>. However, each day a new cell becomes flooded with <strong>water</strong>. You are given a <strong>1-based</strong> 2D array <code>cells</code>, where <code>cells[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> represents that on the <code>i<sup>th</sup></code> day, the cell on the <code>r<sub>i</sub><sup>th</sup></code> row and <code>c<sub>i</sub><sup>th</sup></code> column (<strong>1-based</strong> coordinates) will be covered with <strong>water</strong> (i.e., changed to <code>1</code>).</p>

<p>You want to find the <strong>last</strong> day that it is possible to walk from the <strong>top</strong> to the <strong>bottom</strong> by only walking on land cells. You can start from <strong>any</strong> cell in the top row and end at <strong>any</strong> cell in the bottom row. You can only travel in the<strong> four</strong> cardinal directions (left, right, up, and down).</p>

<p>Return <em>the <strong>last</strong> day where it is possible to walk from the <strong>top</strong> to the <strong>bottom</strong> by only walking on land cells</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1970.Last%20Day%20Where%20You%20Can%20Still%20Cross/images/1.png" style="width: 624px; height: 162px;" />
<pre>
<strong>Input:</strong> row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1970.Last%20Day%20Where%20You%20Can%20Still%20Cross/images/2.png" style="width: 504px; height: 178px;" />
<pre>
<strong>Input:</strong> row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1970.Last%20Day%20Where%20You%20Can%20Still%20Cross/images/3.png" style="width: 666px; height: 167px;" />
<pre>
<strong>Input:</strong> row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= row, col &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>4 &lt;= row * col &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>cells.length == row * col</code></li>
	<li><code>1 &lt;= r<sub>i</sub> &lt;= row</code></li>
	<li><code>1 &lt;= c<sub>i</sub> &lt;= col</code></li>
	<li>All the values of <code>cells</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search + BFS

We note that if we can walk from the top row to the bottom row on day $k$, then for any $0 < k' < k$, we can also walk from the top row to the bottom row on day $k'$. This exhibits monotonicity, so we can use binary search to find the largest $k$ such that we can walk from the top row to the bottom row on day $k$.

We define the left boundary of the binary search as $l = 1$ and the right boundary as $r = |cells|$, where $|cells|$ represents the length of the array $\textit{cells}$. Then, we perform binary search on $k$. For each $k$, we take the first $k$ elements of $\textit{cells}$, turn the corresponding cells into water, and then use breadth-first search (BFS) to try to walk from the top row to the bottom row. If we can reach the bottom row, it means we can walk from the top row to the bottom row on day $k$, so we update the left boundary $l$ to $k$. Otherwise, we update the right boundary $r$ to $k - 1$.

The time complexity is $O(m \times n \times \log (m \times n))$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ represent the number of rows and columns of the matrix, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def check(k: int) -> bool:
            g = [[0] * col for _ in range(row)]
            for i, j in cells[:k]:
                g[i - 1][j - 1] = 1
            q = [(0, j) for j in range(col) if g[0][j] == 0]
            for x, y in q:
                if x == row - 1:
                    return True
                for a, b in pairwise(dirs):
                    nx, ny = x + a, y + b
                    if 0 <= nx < row and 0 <= ny < col and g[nx][ny] == 0:
                        q.append((nx, ny))
                        g[nx][ny] = 1
            return False

        n = row * col
        l, r = 1, n
        dirs = (-1, 0, 1, 0, -1)
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

<!-- solution:start -->

### Solution 2: Union-Find

We can first initialize all land cells as $1$, then traverse the array $\textit{cells}$ in reverse order, turning each corresponding land cell into $0$ and merging it with the adjacent land cells (up, down, left, right). We also need to maintain two virtual nodes $s$ and $t$, representing the virtual nodes for the top row and the bottom row, respectively. If $s$ and $t$ are connected in the union-find set, it means we can walk from the top row to the bottom row on day $i$.

The time complexity is $O(m \times n \times \alpha(m \times n))$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ represent the number of rows and columns of the matrix, respectively, and $\alpha$ represents the inverse Ackermann function.

<!-- tabs:start -->

#### Python3

```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
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
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        mn = len(cells)
        uf = UnionFind(mn + 2)
        s, t = mn, mn + 1
        dirs = (-1, 0, 1, 0, -1)
        g = [[1] * col for _ in range(row)]
        for i in range(mn - 1, -1, -1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            g[x][y] = 0
            for a, b in pairwise(dirs):
                nx, ny = x + a, y + b
                if 0 <= nx < row and 0 <= ny < col and g[nx][ny] == 0:
                    uf.union(x * col + y, nx * col + ny)
            if x == 0:
                uf.union(y, s)
            if x == row - 1:
                uf.union(x * col + y, t)
            if uf.find(s) == uf.find(t):
                return i
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
