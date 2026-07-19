---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0874.Walking%20Robot%20Simulation/README_EN.md
tags:
    - Array
    - Hash Table
    - Simulation
---

<!-- problem:start -->

# [874. Walking Robot Simulation](https://leetcode.com/problems/walking-robot-simulation)

## Description

<!-- description:start -->

<p>A robot on an infinite XY-plane starts at point <code>(0, 0)</code> facing north. The robot receives an array of integers <code>commands</code>, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:</p>

<ul>
	<li><code>-2</code>: Turn left <code>90</code> degrees.</li>
	<li><code>-1</code>: Turn right <code>90</code> degrees.</li>
	<li><code>1 &lt;= k &lt;= 9</code>: Move forward <code>k</code> units, one unit at a time.</li>
</ul>

<p>Some of the grid squares are <code>obstacles</code>. The <code>i<sup>th</sup></code> obstacle is at grid point <code>obstacles[i] = (x<sub>i</sub>, y<sub>i</sub>)</code>. If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.</p>

<p>Return the <strong>maximum squared Euclidean distance</strong> that the robot reaches at any point in its path (i.e. if the distance is <code>5</code>, return <code>25</code>).</p>

<p><strong>Note:</strong></p>

<ul>
	<li>There can be an obstacle at <code>(0, 0)</code>. If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to <code>(0, 0)</code> due to the obstacle.</li>
	<li>North means +Y direction.</li>
	<li>East means +X direction.</li>
	<li>South means -Y direction.</li>
	<li>West means -X direction.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">commands = [4,-1,3], obstacles = []</span></p>

<p><strong>Output:</strong> <span class="example-io">25</span></p>

<p><strong>Explanation: </strong></p>

<p>The robot starts at <code>(0, 0)</code>:</p>

<ol>
	<li>Move north 4 units to <code>(0, 4)</code>.</li>
	<li>Turn right.</li>
	<li>Move east 3 units to <code>(3, 4)</code>.</li>
</ol>

<p>The furthest point the robot ever gets from the origin is <code>(3, 4)</code>, which squared is <code>3<sup>2</sup> + 4<sup>2 </sup>= 25</code> units away.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">commands = [4,-1,4,-2,4], obstacles = [[2,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">65</span></p>

<p><strong>Explanation:</strong></p>

<p>The robot starts at <code>(0, 0)</code>:</p>

<ol>
	<li>Move north 4 units to <code>(0, 4)</code>.</li>
	<li>Turn right.</li>
	<li>Move east 1 unit and get blocked by the obstacle at <code>(2, 4)</code>, robot is at <code>(1, 4)</code>.</li>
	<li>Turn left.</li>
	<li>Move north 4 units to <code>(1, 8)</code>.</li>
</ol>

<p>The furthest point the robot ever gets from the origin is <code>(1, 8)</code>, which squared is <code>1<sup>2</sup> + 8<sup>2</sup> = 65</code> units away.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">commands = [6,-1,-1,6], obstacles = [[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">36</span></p>

<p><strong>Explanation:</strong></p>

<p>The robot starts at <code>(0, 0)</code>:</p>

<ol>
	<li>Move north 6 units to <code>(0, 6)</code>.</li>
	<li>Turn right.</li>
	<li>Turn right.</li>
	<li>Move south 5 units and get blocked by the obstacle at <code>(0,0)</code>, robot is at <code>(0, 1)</code>.</li>
</ol>

<p>The furthest point the robot ever gets from the origin is <code>(0, 6)</code>, which squared is <code>6<sup>2</sup> = 36</code> units away.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= commands.length &lt;= 10<sup>4</sup></code></li>
	<li><code>commands[i]</code> is either <code>-2</code>, <code>-1</code>, or an integer in the range <code>[1, 9]</code>.</li>
	<li><code>0 &lt;= obstacles.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 3 * 10<sup>4</sup></code></li>
	<li>The answer is guaranteed to be less than <code>2<sup>31</sup></code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Simulation

We define a direction array $dirs = [0, 1, 0, -1, 0]$ of length $5$, where each pair of adjacent elements represents a direction. That is, $(dirs[0], dirs[1])$ represents north, $(dirs[1], dirs[2])$ represents east, and so on.

We use a hash table $s$ to store the coordinates of all obstacles, so we can determine in $O(1)$ time whether the next step will encounter an obstacle.

Additionally, we use two variables $x$ and $y$ to represent the robot's current coordinates, initially $x = y = 0$. The variable $k$ represents the robot's current direction, and the answer variable $ans$ represents the maximum squared Euclidean distance from the origin.

Next, we iterate over each element $c$ in the array $commands$:

- If $c = -2$, the robot turns left $90$ degrees, i.e., $k = (k + 3) \bmod 4$;
- If $c = -1$, the robot turns right $90$ degrees, i.e., $k = (k + 1) \bmod 4$;
- Otherwise, the robot moves forward $c$ units. We combine the robot's current direction $k$ with the direction array $dirs$ to obtain the increments along the $x$-axis and $y$-axis. We accumulate the increments step by step onto $x$ and $y$, and check whether each new coordinate $(nx, ny)$ is in the obstacle set. If not, we update the answer $ans$; otherwise, we stop the simulation and proceed to the next command.

Finally, return the answer $ans$.

The time complexity is $O(C \times n + m)$ and the space complexity is $O(m)$, where $C$ is the maximum number of steps per move, and $n$ and $m$ are the lengths of the arrays $commands$ and $obstacles$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = (0, 1, 0, -1, 0)
        s = {(x, y) for x, y in obstacles}
        ans = k = 0
        x = y = 0
        for c in commands:
            if c == -2:
                k = (k + 3) % 4
            elif c == -1:
                k = (k + 1) % 4
            else:
                for _ in range(c):
                    nx, ny = x + dirs[k], y + dirs[k + 1]
                    if (nx, ny) in s:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
