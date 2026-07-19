---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2069.Walking%20Robot%20Simulation%20II/README_EN.md
rating: 1918
source: Biweekly Contest 65 Q2
tags:
    - Design
    - Simulation
---

<!-- problem:start -->

# [2069. Walking Robot Simulation II](https://leetcode.com/problems/walking-robot-simulation-ii)

## Description

<!-- description:start -->

<p>A <code>width x height</code> grid is on an XY-plane with the <strong>bottom-left</strong> cell at <code>(0, 0)</code> and the <strong>top-right</strong> cell at <code>(width - 1, height - 1)</code>. The grid is aligned with the four cardinal directions (<code>&quot;North&quot;</code>, <code>&quot;East&quot;</code>, <code>&quot;South&quot;</code>, and <code>&quot;West&quot;</code>). A robot is <strong>initially</strong> at cell <code>(0, 0)</code> facing direction <code>&quot;East&quot;</code>.</p>

<p>The robot can be instructed to move for a specific number of <strong>steps</strong>. For each step, it does the following.</p>

<ol>
	<li>Attempts to move <strong>forward one</strong> cell in the direction it is facing.</li>
	<li>If the cell the robot is <strong>moving to</strong> is <strong>out of bounds</strong>, the robot instead <strong>turns</strong> 90 degrees <strong>counterclockwise</strong> and retries the step.</li>
</ol>

<p>After the robot finishes moving the number of steps required, it stops and awaits the next instruction.</p>

<p>Implement the <code>Robot</code> class:</p>

<ul>
	<li><code>Robot(int width, int height)</code> Initializes the <code>width x height</code> grid with the robot at <code>(0, 0)</code> facing <code>&quot;East&quot;</code>.</li>
	<li><code>void step(int num)</code> Instructs the robot to move forward <code>num</code> steps.</li>
	<li><code>int[] getPos()</code> Returns the current cell the robot is at, as an array of length 2, <code>[x, y]</code>.</li>
	<li><code>String getDir()</code> Returns the current direction of the robot, <code>&quot;North&quot;</code>, <code>&quot;East&quot;</code>, <code>&quot;South&quot;</code>, or <code>&quot;West&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="example-1" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2069.Walking%20Robot%20Simulation%20II/images/example-1.png" style="width: 498px; height: 268px;" />
<pre>
<strong>Input</strong>
[&quot;Robot&quot;, &quot;step&quot;, &quot;step&quot;, &quot;getPos&quot;, &quot;getDir&quot;, &quot;step&quot;, &quot;step&quot;, &quot;step&quot;, &quot;getPos&quot;, &quot;getDir&quot;]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
<strong>Output</strong>
[null, null, null, [4, 0], &quot;East&quot;, null, null, null, [1, 2], &quot;West&quot;]

<strong>Explanation</strong>
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2); // It moves two steps East to (2, 0), and faces East.
robot.step(2); // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return &quot;East&quot;
robot.step(2); // It moves one step East to (5, 0), and faces East.
// Moving the next step East would be out of bounds, so it turns and faces North.
// Then, it moves one step North to (5, 1), and faces North.
robot.step(1); // It moves one step North to (5, 2), and faces <strong>North</strong> (not West).
robot.step(4); // Moving the next step North would be out of bounds, so it turns and faces West.
// Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return &quot;West&quot;

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= width, height &lt;= 100</code></li>
	<li><code>1 &lt;= num &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>step</code>, <code>getPos</code>, and <code>getDir</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Case Analysis

Let $mx = width - 1$ and $my = height - 1$. The robot's trajectory forms the boundary of a rectangle with $(0, 0)$ as the bottom-left corner and $(mx, my)$ as the top-right corner. We can divide the robot's trajectory into four segments:

1. From $(0, 0)$ moving along the positive $x$-axis to $(mx, 0)$, where the robot faces "East".
2. From $(mx, 0)$ moving along the positive $y$-axis to $(mx, my)$, where the robot faces "North".
3. From $(mx, my)$ moving along the negative $x$-axis to $(0, my)$, where the robot faces "West".
4. From $(0, my)$ moving along the negative $y$-axis to $(0, 0)$, where the robot faces "South".

Therefore, the robot's trajectory can be viewed as a cycle of length $p = 2 \cdot mx + 2 \cdot my$. For each call to `step(num)`, we add `num` to the robot's current position and take the result modulo $p$ to get the robot's new position. Based on the new position, we can determine the robot's direction and coordinates.

Note that if the robot has never moved, its direction should be "East". If the robot has moved and its position is $(0, 0)$, then its direction should be "South".

The time complexity is $O(1)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Robot:

    def __init__(self, width: int, height: int):
        self.mx = width - 1
        self.my = height - 1
        self.p = 2 * self.mx + 2 * self.my
        self.cur = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.cur = (self.cur + num) % self.p

    def getPos(self) -> List[int]:
        d = self.cur
        mx, my = self.mx, self.my
        if 0 <= d <= mx:
            return [d, 0]
        if mx < d <= mx + my:
            return [mx, d - mx]
        if mx + my < d <= 2 * mx + my:
            return [mx - (d - (mx + my)), my]
        return [0, my - (d - (2 * mx + my))]

    def getDir(self) -> str:
        d = self.cur
        mx, my = self.mx, self.my
        if not self.moved:
            return "East"
        if 1 <= d <= mx:
            return "East"
        elif mx < d <= mx + my:
            return "North"
        elif mx + my < d <= 2 * mx + my:
            return "West"
        return "South"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
