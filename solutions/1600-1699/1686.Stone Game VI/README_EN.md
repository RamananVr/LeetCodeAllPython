---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1686.Stone%20Game%20VI/README_EN.md
rating: 2000
source: Biweekly Contest 41 Q3
tags:
    - Greedy
    - Array
    - Math
    - Game Theory
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1686. Stone Game VI](https://leetcode.com/problems/stone-game-vi)

## Description

<!-- description:start -->

<p>Alice and Bob take turns playing a game, with Alice starting first.</p>

<p>There are <code>n</code> stones in a pile. On each player&#39;s turn, they can <strong>remove</strong> a stone from the pile and receive points based on the stone&#39;s value. Alice and Bob may <strong>value the stones differently</strong>.</p>

<p>You are given two integer arrays of length <code>n</code>, <code>aliceValues</code> and <code>bobValues</code>. Each <code>aliceValues[i]</code> and <code>bobValues[i]</code> represents how Alice and Bob, respectively, value the <code>i<sup>th</sup></code> stone.</p>

<p>The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play <strong>optimally</strong>.&nbsp;Both players know the other&#39;s values.</p>

<p>Determine the result of the game, and:</p>

<ul>
	<li>If Alice wins, return <code>1</code>.</li>
	<li>If Bob wins, return <code>-1</code>.</li>
	<li>If the game results in a draw, return <code>0</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> aliceValues = [1,3], bobValues = [2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> aliceValues = [1,2], bobValues = [3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> aliceValues = [2,4,3], bobValues = [1,6,7]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob&#39;s 7.
Bob wins.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == aliceValues.length == bobValues.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= aliceValues[i], bobValues[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Sorting

The optimal strategy for picking stones is to maximize one's own score while making the opponent lose as much as possible. Therefore, we create an array $vals$, where $vals[i] = (aliceValues[i] + bobValues[i], i)$ represents the total value and index of the $i$-th stone. Then we sort $vals$ in descending order by total value.

Next, we let Alice and Bob pick stones alternately according to the order of $vals$. Alice picks the stones at even positions in $vals$, and Bob picks the stones at odd positions in $vals$. Finally, we compare the scores of Alice and Bob and return the corresponding result.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the arrays `aliceValues` and `bobValues`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        vals = [(a + b, i) for i, (a, b) in enumerate(zip(aliceValues, bobValues))]
        vals.sort(reverse=True)
        a = sum(aliceValues[i] for _, i in vals[::2])
        b = sum(bobValues[i] for _, i in vals[1::2])
        if a > b:
            return 1
        if a < b:
            return -1
        return 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
