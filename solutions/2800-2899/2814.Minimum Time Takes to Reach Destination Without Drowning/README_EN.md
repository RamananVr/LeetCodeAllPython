---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2814.Minimum%20Time%20Takes%20to%20Reach%20Destination%20Without%20Drowning/README_EN.md
tags:
    - Breadth-First Search
    - Array
    - Matrix
---

<!-- problem:start -->

# [2814. Minimum Time Takes to Reach Destination Without Drowning 🔒](https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning)

## Description

<!-- description:start -->

<p>You are given an <code>n * m</code> <strong>0-indexed</strong> grid of string <code>land</code>. Right now, you are standing at the cell that contains <code>&quot;S&quot;</code>, and you want to get to the cell containing <code>&quot;D&quot;</code>. There are three other types of cells in this land:</p>

<ul>
	<li><code>&quot;.&quot;</code>: These cells are empty.</li>
	<li><code>&quot;X&quot;</code>: These cells are stone.</li>
	<li><code>&quot;*&quot;</code>: These cells are flooded.</li>
</ul>

<p>At each second, you can move to a cell that shares a side with your current cell (if it exists). Also, at each second, every <strong>empty cell</strong> that shares a side with a flooded cell becomes flooded as well.<br />
There are two problems ahead of your journey:</p>

<ul>
	<li>You can&#39;t step on stone cells.</li>
	<li>You can&#39;t step on flooded cells since you will drown (also, you can&#39;t step on a cell that will be flooded at the same time as you step on it).</li>
</ul>

<p>Return<em> the <strong>minimum</strong> time it takes you to reach the destination in seconds, or </em><code>-1</code><em> if it is impossible.</em></p>

<p><strong>Note</strong> that the destination will never be flooded.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> land = [[&quot;D&quot;,&quot;.&quot;,&quot;*&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;S&quot;,&quot;.&quot;]]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The picture below shows the simulation of the land second by second. The blue cells are flooded, and the gray cells are stone.
Picture (0) shows the initial state and picture (3) shows the final state when we reach destination. As you see, it takes us 3 second to reach destination and the answer would be 3.
It can be shown that 3 is the minimum time needed to reach from S to D.
</pre>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2814.Minimum%20Time%20Takes%20to%20Reach%20Destination%20Without%20Drowning/images/ex1.png" style="padding: 5px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 600px; height: 111px;" /></p>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> land = [[&quot;D&quot;,&quot;X&quot;,&quot;*&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;S&quot;]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The picture below shows the simulation of the land second by second. The blue cells are flooded, and the gray cells are stone.
Picture (0) shows the initial state. As you see, no matter which paths we choose, we will drown at the 3<sup>rd</sup>&nbsp;second. Also the minimum path takes us 4 seconds to reach from S to D.
So the answer would be -1.
</pre>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2814.Minimum%20Time%20Takes%20to%20Reach%20Destination%20Without%20Drowning/images/ex2-2.png" style="padding: 7px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 600px; height: 107px;" /></p>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> land = [[&quot;D&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;X&quot;,&quot;.&quot;,&quot;X&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;S&quot;,&quot;.&quot;]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> It can be shown that we can reach destination in 6 seconds. Also it can be shown that 6 is the minimum seconds one need to reach from S to D.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n, m &lt;= 100</code></li>
	<li><code>land</code>&nbsp;consists only of&nbsp;<code>&quot;S&quot;</code>, <code>&quot;D&quot;</code>, <code>&quot;.&quot;</code>, <code>&quot;*&quot;</code> and&nbsp;<code>&quot;X&quot;</code>.</li>
	<li><strong>Exactly</strong> one of the cells is equal to <code>&quot;S&quot;</code>.</li>
	<li><strong>Exactly</strong> one of the cells is equal to <code>&quot;D&quot;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two BFS Traversals

First, we run a BFS (Breadth-First Search) to calculate the shortest distance from each cell to the water, and record it in the array $g$. Then, we run another BFS starting from the cell $(s_i, s_j)$ to find the shortest distance to the target cell $(d_i, d_j)$. During this process, if the adjacent cell $(x, y)$ of the current cell $(i, j)$ satisfies $g[x][y] > t + 1$, then we can move from $(x, y)$ to $(i, j)$.

The time complexity is $O(m \times n)$ and the space complexity is $O(m \times n)$. Where $m$ and $n$ are the number of rows and columns of the array $land$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        m, n = len(land), len(land[0])
        vis = [[False] * n for _ in range(m)]
        g = [[inf] * n for _ in range(m)]
        q = deque()
        si = sj = 0
        for i, row in enumerate(land):
            for j, c in enumerate(row):
                match c:
                    case "*":
                        q.append((i, j))
                    case "S":
                        si, sj = i, j
        dirs = (-1, 0, 1, 0, -1)
        t = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                g[i][j] = t
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if (
                        0 <= x < m
                        and 0 <= y < n
                        and not vis[x][y]
                        and land[x][y] in ".S"
                    ):
                        vis[x][y] = True
                        q.append((x, y))
            t += 1
        t = 0
        q = deque([(si, sj)])
        vis = [[False] * n for _ in range(m)]
        vis[si][sj] = True
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if land[i][j] == "D":
                    return t
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if (
                        0 <= x < m
                        and 0 <= y < n
                        and g[x][y] > t + 1
                        and not vis[x][y]
                        and land[x][y] in ".D"
                    ):
                        vis[x][y] = True
                        q.append((x, y))
            t += 1
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
