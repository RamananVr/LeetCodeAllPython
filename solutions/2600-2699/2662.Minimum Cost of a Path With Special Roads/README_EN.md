---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2662.Minimum%20Cost%20of%20a%20Path%20With%20Special%20Roads/README_EN.md
rating: 2153
source: Weekly Contest 343 Q3
tags:
    - Graph
    - Array
    - Shortest Path
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2662. Minimum Cost of a Path With Special Roads](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads)

## Description

<!-- description:start -->

<p>You are given an array <code>start</code> where <code>start = [startX, startY]</code> represents your initial position <code>(startX, startY)</code> in a 2D space. You are also given the array <code>target</code> where <code>target = [targetX, targetY]</code> represents your target position <code>(targetX, targetY)</code>.</p>

<p>The <strong>cost</strong> of going from a position <code>(x1, y1)</code> to any other position in the space <code>(x2, y2)</code> is <code>|x2 - x1| + |y2 - y1|</code>.</p>

<p>There are also some <strong>special roads</strong>. You are given a 2D array <code>specialRoads</code> where <code>specialRoads[i] = [x1<sub>i</sub>, y1<sub>i</sub>, x2<sub>i</sub>, y2<sub>i</sub>, cost<sub>i</sub>]</code> indicates that the <code>i<sup>th</sup></code> special road goes in <strong>one direction</strong> from <code>(x1<sub>i</sub>, y1<sub>i</sub>)</code> to <code>(x2<sub>i</sub>, y2<sub>i</sub>)</code> with a cost equal to <code>cost<sub>i</sub></code>. You can use each special road any number of times.</p>

<p>Return the <strong>minimum</strong> cost required to go from <code>(startX, startY)</code> to <code>(targetX, targetY)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>(1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.</li>
	<li>(1,2) to (3,3). Use <code><span class="example-io">specialRoads[0]</span></code><span class="example-io"> with</span><span class="example-io"> the cost 2.</span></li>
	<li><span class="example-io">(3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1.</span></li>
	<li><span class="example-io">(3,4) to (4,5). Use </span><code><span class="example-io">specialRoads[1]</span></code><span class="example-io"> with the cost</span><span class="example-io"> 1.</span></li>
</ol>

<p><span class="example-io">So the total cost is 1 + 2 + 1 + 1 = 5.</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.</p>

<p>Note that the <span class="example-io"><code>specialRoads[0]</code> is directed from (5,7) to (3,2).</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>(1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.</li>
	<li>(1,2) to (7,4). Use <code><span class="example-io">specialRoads[1]</span></code><span class="example-io"> with the cost</span><span class="example-io"> 4.</span></li>
	<li>(7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.</li>
</ol>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>start.length == target.length == 2</code></li>
	<li><code>1 &lt;= startX &lt;= targetX &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= startY &lt;= targetY &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= specialRoads.length &lt;= 200</code></li>
	<li><code>specialRoads[i].length == 5</code></li>
	<li><code>startX &lt;= x1<sub>i</sub>, x2<sub>i</sub> &lt;= targetX</code></li>
	<li><code>startY &lt;= y1<sub>i</sub>, y2<sub>i</sub> &lt;= targetY</code></li>
	<li><code>1 &lt;= cost<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dijkstra

We can find that for each coordinate $(x, y)$ we visit, suppose the minimum cost from the start point to $(x, y)$ is $d$. If we choose to move directly to $(targetX, targetY)$, then the total cost is $d + |x - targetX| + |y - targetY|$. If we choose to go through a special path $(x_1, y_1) \rightarrow (x_2, y_2)$, then we need to spend $|x - x_1| + |y - y_1| + cost$ to move from $(x, y)$ to $(x_2, y_2)$.

Therefore, we can use Dijkstra algorithm to find the minimum cost from the start point to all points, and then choose the smallest one from them.

We define a priority queue $q$, each element in the queue is a triple $(d, x, y)$, which means that the minimum cost from the start point to $(x, y)$ is $d$. Initially, we add $(0, startX, startY)$ to the queue.

In each step, we take out the first element $(d, x, y)$ in the queue, at this time we can update the answer, that is $ans = \min(ans, d + dist(x, y, targetX, targetY))$. Then we enumerate all special paths $(x_1, y_1) \rightarrow (x_2, y_2)$ and add $(d + dist(x, y, x_1, y_1) + cost, x_2, y_2)$ to the queue.

Finally, when the queue is empty, we can get the answer.

The time complexity is $O(n^2 \times \log n)$, and the space complexity is $O(n^2)$. Where $n$ is the number of special paths.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        def dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        q = [(0, start[0], start[1])]
        vis = set()
        ans = inf
        while q:
            d, x, y = heappop(q)
            if (x, y) in vis:
                continue
            vis.add((x, y))
            ans = min(ans, d + dist(x, y, *target))
            for x1, y1, x2, y2, cost in specialRoads:
                heappush(q, (d + dist(x, y, x1, y1) + cost, x2, y2))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
