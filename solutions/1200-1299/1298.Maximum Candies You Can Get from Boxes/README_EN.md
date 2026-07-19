---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1298.Maximum%20Candies%20You%20Can%20Get%20from%20Boxes/README_EN.md
rating: 1824
source: Weekly Contest 168 Q4
tags:
    - Breadth-First Search
    - Graph
    - Array
---

<!-- problem:start -->

# [1298. Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes)

## Description

<!-- description:start -->

<p>You have <code>n</code> boxes labeled from <code>0</code> to <code>n - 1</code>. You are given four arrays: <code>status</code>, <code>candies</code>, <code>keys</code>, and <code>containedBoxes</code> where:</p>

<ul>
	<li><code>status[i]</code> is <code>1</code> if the <code>i<sup>th</sup></code> box is open and <code>0</code> if the <code>i<sup>th</sup></code> box is closed,</li>
	<li><code>candies[i]</code> is the number of candies in the <code>i<sup>th</sup></code> box,</li>
	<li><code>keys[i]</code> is a list of the labels of the boxes you can open after opening the <code>i<sup>th</sup></code> box.</li>
	<li><code>containedBoxes[i]</code> is a list of the boxes you found inside the <code>i<sup>th</sup></code> box.</li>
</ul>

<p>You are given an integer array <code>initialBoxes</code> that contains the labels of the boxes you initially have. You can take all the candies in <strong>any open box</strong> and you can use the keys in it to open new boxes and you also can use the boxes you find in it.</p>

<p>Return <em>the maximum number of candies you can get following the rules above</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
<strong>Output:</strong> 16
<strong>Explanation:</strong> You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == status.length == candies.length == keys.length == containedBoxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>status[i]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>1 &lt;= candies[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= keys[i].length &lt;= n</code></li>
	<li><code>0 &lt;= keys[i][j] &lt; n</code></li>
	<li>All values of <code>keys[i]</code> are <strong>unique</strong>.</li>
	<li><code>0 &lt;= containedBoxes[i].length &lt;= n</code></li>
	<li><code>0 &lt;= containedBoxes[i][j] &lt; n</code></li>
	<li>All values of <code>containedBoxes[i]</code> are unique.</li>
	<li>Each box is contained in one box at most.</li>
	<li><code>0 &lt;= initialBoxes.length &lt;= n</code></li>
	<li><code>0 &lt;= initialBoxes[i] &lt; n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS + Hash Set

The problem gives a set of boxes, each of which may have a state (open/closed), candies, keys, and other boxes inside. Our goal is to use the initially given boxes to open as many more boxes as possible and collect the candies inside. We can unlock new boxes by obtaining keys, and get more resources through boxes nested inside other boxes.

We use BFS to simulate the entire exploration process.

We use a queue $q$ to represent the currently accessible and **already opened** boxes; two sets, $\textit{has}$ and $\textit{took}$, are used to record **all boxes we own** and **boxes we have already processed**, to avoid duplicates.

Initially, add all $\textit{initialBoxes}$ to $\textit{has}$. If an initial box is open, immediately add it to the queue $\textit{q}$ and accumulate its candies.

Then perform BFS, taking boxes out of $\textit{q}$ one by one:

- Obtain the keys in the box $\textit{keys[box]}$ and add any boxes that can be unlocked to the queue;
- Collect other boxes contained in the box $\textit{containedBoxes[box]}$. If a contained box is open and has not been processed, process it immediately;

Each box is processed at most once, and candies are accumulated once. Finally, return the total number of candies $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the total number of boxes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        q = deque()
        has, took = set(initialBoxes), set()
        ans = 0

        for box in initialBoxes:
            if status[box]:
                q.append(box)
                took.add(box)
                ans += candies[box]
        while q:
            box = q.popleft()
            for k in keys[box]:
                if not status[k]:
                    status[k] = 1
                    if k in has and k not in took:
                        q.append(k)
                        took.add(k)
                        ans += candies[k]

            for b in containedBoxes[box]:
                has.add(b)
                if status[b] and b not in took:
                    q.append(b)
                    took.add(b)
                    ans += candies[b]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
