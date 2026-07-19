---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1263.Minimum%20Moves%20to%20Move%20a%20Box%20to%20Their%20Target%20Location/README_EN.md
rating: 2297
source: Weekly Contest 163 Q4
tags:
    - Breadth-First Search
    - Array
    - Matrix
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1263. Minimum Moves to Move a Box to Their Target Location](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location)

## Description

<!-- description:start -->

<p>A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.</p>

<p>The game is represented by an <code>m x n</code> grid of characters <code>grid</code> where each element is a wall, floor, or box.</p>

<p>Your task is to move the box <code>&#39;B&#39;</code> to the target position <code>&#39;T&#39;</code> under the following rules:</p>

<ul>
	<li>The character <code>&#39;S&#39;</code> represents the player. The player can move up, down, left, right in <code>grid</code> if it is a floor (empty cell).</li>
	<li>The character <code>&#39;.&#39;</code> represents the floor which means a free cell to walk.</li>
	<li>The character<font face="monospace">&nbsp;</font><code>&#39;#&#39;</code><font face="monospace">&nbsp;</font>represents the wall which means an obstacle (impossible to walk there).</li>
	<li>There is only one box <code>&#39;B&#39;</code> and one target cell <code>&#39;T&#39;</code> in the <code>grid</code>.</li>
	<li>The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a <strong>push</strong>.</li>
	<li>The player cannot walk through the box.</li>
</ul>

<p>Return <em>the minimum number of <strong>pushes</strong> to move the box to the target</em>. If there is no way to reach the target, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1263.Minimum%20Moves%20to%20Move%20a%20Box%20to%20Their%20Target%20Location/images/sample_1_1620.png" style="width: 500px; height: 335px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;T&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;,&quot;B&quot;,&quot;.&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;S&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We return only the number of times the box is pushed.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;T&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;,&quot;B&quot;,&quot;.&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;S&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;]]
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;T&quot;,&quot;.&quot;,&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;B&quot;,&quot;.&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;S&quot;,&quot;#&quot;],
               [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;#&quot;]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> push the box down, left, left, up and up.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>grid</code> contains only characters <code>&#39;.&#39;</code>, <code>&#39;#&#39;</code>, <code>&#39;S&#39;</code>, <code>&#39;T&#39;</code>, or <code>&#39;B&#39;</code>.</li>
	<li>There is only one character <code>&#39;S&#39;</code>, <code>&#39;B&#39;</code>, and <code>&#39;T&#39;</code> in the <code>grid</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Double-ended Queue + BFS

We consider the player's position and the box's position as a state, i.e., $(s_i, s_j, b_i, b_j)$, where $(s_i, s_j)$ is the player's position, and $(b_i, b_j)$ is the box's position. In the code implementation, we define a function $f(i, j)$, which maps the two-dimensional coordinates $(i, j)$ to a one-dimensional state number, i.e., $f(i, j) = i \times n + j$, where $n$ is the number of columns in the grid. So the player and the box's state is $(f(s_i, s_j), f(b_i, b_j))$.

First, we traverse the grid to find the initial positions of the player and the box, denoted as $(s_i, s_j)$ and $(b_i, b_j)$.

Then, we define a double-ended queue $q$, where each element is a triplet $(f(s_i, s_j), f(b_i, b_j), d)$, indicating that the player is at $(s_i, s_j)$, the box is at $(b_i, b_j)$, and $d$ pushes have been made. Initially, we add $(f(s_i, s_j), f(b_i, b_j), 0)$ to the queue $q$.

Additionally, we use a two-dimensional array $vis$ to record whether each state has been visited. Initially, $vis[f(s_i, s_j), f(b_i, b_j)]$ is marked as visited.

Next, we start the breadth-first search.

In each step of the search, we take out the queue head element $(f(s_i, s_j), f(b_i, b_j), d)$, and check whether $grid[b_i][b_j] = 'T'$ is satisfied. If it is, it means the box has been pushed to the target position, and now $d$ can be returned as the answer.

Otherwise, we enumerate the player's next move direction. The player's new position is denoted as $(s_x, s_y)$. If $(s_x, s_y)$ is a valid position, we judge whether $(s_x, s_y)$ is the same as the box's position $(b_i, b_j)$:

- If they are the same, it means the player has reached the box's position and pushed the box forward by one step. The box's new position is $(b_x, b_y)$. If $(b_x, b_y)$ is a valid position, and the state $(f(s_x, s_y), f(b_x, b_y))$ has not been visited, then we add $(f(s_x, s_y), f(b_x, b_y), d + 1)$ to the end of the queue $q$, and mark $vis[f(s_x, s_y), f(b_x, b_y)]$ as visited.
- If they are different, it means the player has not pushed the box. Then we only need to judge whether the state $(f(s_x, s_y), f(b_i, b_j))$ has been visited. If it has not been visited, then we add $(f(s_x, s_y), f(b_i, b_j), d)$ to the head of the queue $q$, and mark $vis[f(s_x, s_y), f(b_i, b_j)]$ as visited.

We continue the breadth-first search until the queue is empty.

> Note, if the box is pushed, the push count $d$ needs to be incremented by $1$, and the new state is added to the end of the queue $q$. If the box is not pushed, the push count $d$ remains unchanged, and the new state is added to the head of the queue $q$.

Finally, if no valid push scheme is found, then return $-1$.

The time complexity is $O(m^2 \times n^2)$, and the space complexity is $O(m^2 \times n^2)$. Where $m$ and $n$ are the number of rows and columns in the grid, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def f(i: int, j: int) -> int:
            return i * n + j

        def check(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n and grid[i][j] != "#"

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "S":
                    si, sj = i, j
                elif c == "B":
                    bi, bj = i, j
        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        q = deque([(f(si, sj), f(bi, bj), 0)])
        vis = [[False] * (m * n) for _ in range(m * n)]
        vis[f(si, sj)][f(bi, bj)] = True
        while q:
            s, b, d = q.popleft()
            bi, bj = b // n, b % n
            if grid[bi][bj] == "T":
                return d
            si, sj = s // n, s % n
            for a, b in pairwise(dirs):
                sx, sy = si + a, sj + b
                if not check(sx, sy):
                    continue
                if sx == bi and sy == bj:
                    bx, by = bi + a, bj + b
                    if not check(bx, by) or vis[f(sx, sy)][f(bx, by)]:
                        continue
                    vis[f(sx, sy)][f(bx, by)] = True
                    q.append((f(sx, sy), f(bx, by), d + 1))
                elif not vis[f(sx, sy)][f(bi, bj)]:
                    vis[f(sx, sy)][f(bi, bj)] = True
                    q.appendleft((f(sx, sy), f(bi, bj), d))
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
