---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0353.Design%20Snake%20Game/README_EN.md
tags:
    - Design
    - Queue
    - Array
    - Hash Table
    - Simulation
---

<!-- problem:start -->

# [353. Design Snake Game 🔒](https://leetcode.com/problems/design-snake-game)

## Description

<!-- description:start -->

<p>Design a <a href="https://en.wikipedia.org/wiki/Snake_(video_game)" target="_blank">Snake game</a> that is played on a device with screen size <code>height x width</code>. <a href="http://patorjk.com/games/snake/" target="_blank">Play the game online</a> if you are not familiar with the game.</p>

<p>The snake is initially positioned at the top left corner <code>(0, 0)</code> with a length of <code>1</code> unit.</p>

<p>You are given an array <code>food</code> where <code>food[i] = (r<sub>i</sub>, c<sub>i</sub>)</code> is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game&#39;s score both increase by <code>1</code>.</p>

<p>Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.</p>

<p>When a piece of food appears on the screen, it is <strong>guaranteed</strong> that it will not appear on a block occupied by the snake.</p>

<p>The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies <strong>after</strong> moving (i.e. a snake of length 4 cannot run into itself).</p>

<p>Implement the <code>SnakeGame</code> class:</p>

<ul>
	<li><code>SnakeGame(int width, int height, int[][] food)</code> Initializes the object with a screen of size <code>height x width</code> and the positions of the <code>food</code>.</li>
	<li><code>int move(String direction)</code> Returns the score of the game after applying one <code>direction</code> move by the snake. If the game is over, return <code>-1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0353.Design%20Snake%20Game/images/snake.jpg" style="width: 800px; height: 302px;" />
<pre>
<strong>Input</strong>
[&quot;SnakeGame&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;, &quot;move&quot;]
[[3, 2, [[1, 2], [0, 1]]], [&quot;R&quot;], [&quot;D&quot;], [&quot;R&quot;], [&quot;U&quot;], [&quot;L&quot;], [&quot;U&quot;]]
<strong>Output</strong>
[null, 0, 0, 1, 1, 2, -1]

<strong>Explanation</strong>
SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
snakeGame.move(&quot;R&quot;); // return 0
snakeGame.move(&quot;D&quot;); // return 0
snakeGame.move(&quot;R&quot;); // return 1, snake eats the first piece of food. The second piece of food appears at (0, 1).
snakeGame.move(&quot;U&quot;); // return 1
snakeGame.move(&quot;L&quot;); // return 2, snake eats the second food. No more food appears.
snakeGame.move(&quot;U&quot;); // return -1, game over because snake collides with border

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= width, height &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= food.length &lt;= 50</code></li>
	<li><code>food[i].length == 2</code></li>
	<li><code>0 &lt;= r<sub>i</sub> &lt; height</code></li>
	<li><code>0 &lt;= c<sub>i</sub> &lt; width</code></li>
	<li><code>direction.length == 1</code></li>
	<li><code>direction</code> is <code>&#39;U&#39;</code>, <code>&#39;D&#39;</code>, <code>&#39;L&#39;</code>, or <code>&#39;R&#39;</code>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>move</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.m = height
        self.n = width
        self.food = food
        self.score = 0
        self.idx = 0
        self.q = deque([(0, 0)])
        self.vis = {(0, 0)}

    def move(self, direction: str) -> int:
        i, j = self.q[0]
        x, y = i, j
        match direction:
            case "U":
                x -= 1
            case "D":
                x += 1
            case "L":
                y -= 1
            case "R":
                y += 1
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return -1
        if (
            self.idx < len(self.food)
            and x == self.food[self.idx][0]
            and y == self.food[self.idx][1]
        ):
            self.score += 1
            self.idx += 1
        else:
            self.vis.remove(self.q.pop())
        if (x, y) in self.vis:
            return -1
        self.q.appendleft((x, y))
        self.vis.add((x, y))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
