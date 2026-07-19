---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0489.Robot%20Room%20Cleaner/README_EN.md
tags:
    - Backtracking
    - Interactive
---

<!-- problem:start -->

# [489. Robot Room Cleaner 🔒](https://leetcode.com/problems/robot-room-cleaner)

## Description

<!-- description:start -->

<p>You are controlling a robot that is located somewhere in a room. The room is modeled as an <code>m x n</code> binary grid where <code>0</code> represents a wall and <code>1</code> represents an empty slot.</p>

<p>The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API <code>Robot</code>.</p>

<p>You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is <code>90</code> degrees.</p>

<p>When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.</p>

<p>Design an algorithm to clean the entire room using the following APIs:</p>

<pre>
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
</pre>

<p><strong>Note</strong> that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.</p>

<p>&nbsp;</p>

<p><strong>Custom testing:</strong></p>

<p>The input is only given to initialize the room and the robot&#39;s position internally. You must solve this problem &quot;blindfolded&quot;. In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot&#39;s position.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0489.Robot%20Room%20Cleaner/images/lc-grid.jpg" style="width: 500px; height: 314px;" />
<pre>
<strong>Input:</strong> room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
<strong>Output:</strong> Robot cleaned all rooms.
<strong>Explanation:</strong> All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> room = [[1]], row = 0, col = 0
<strong>Output:</strong> Robot cleaned all rooms.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == room.length</code></li>
	<li><code>n == room[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>room[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= row &lt;&nbsp;m</code></li>
	<li><code>0 &lt;= col &lt; n</code></li>
	<li><code>room[row][col] == 1</code></li>
	<li>All the empty cells can be visited from the starting position.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def dfs(i, j, d):
            vis.add((i, j))
            robot.clean()
            for k in range(4):
                nd = (d + k) % 4
                x, y = i + dirs[nd], j + dirs[nd + 1]
                if (x, y) not in vis and robot.move():
                    dfs(x, y, nd)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        dirs = (-1, 0, 1, 0, -1)
        vis = set()
        dfs(0, 0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
