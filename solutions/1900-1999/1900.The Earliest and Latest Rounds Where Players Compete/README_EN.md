---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1900.The%20Earliest%20and%20Latest%20Rounds%20Where%20Players%20Compete/README_EN.md
rating: 2454
source: Weekly Contest 245 Q4
tags:
    - Memoization
    - Dynamic Programming
---

<!-- problem:start -->

# [1900. The Earliest and Latest Rounds Where Players Compete](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete)

## Description

<!-- description:start -->

<p>There is a tournament where <code>n</code> players are participating. The players are standing in a single row and are numbered from <code>1</code> to <code>n</code> based on their <strong>initial</strong> standing position (player <code>1</code> is the first player in the row, player <code>2</code> is the second player in the row, etc.).</p>

<p>The tournament consists of multiple rounds (starting from round number <code>1</code>). In each round, the <code>i<sup>th</sup></code> player from the front of the row competes against the <code>i<sup>th</sup></code> player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.</p>

<ul>
	<li>For example, if the row consists of players <code>1, 2, 4, 6, 7</code>

    <ul>
    	<li>Player <code>1</code> competes against player <code>7</code>.</li>
    	<li>Player <code>2</code> competes against player <code>6</code>.</li>
    	<li>Player <code>4</code> automatically advances to the next round.</li>
    </ul>
    </li>

</ul>

<p>After each round is over, the winners are lined back up in the row based on the <strong>original ordering</strong> assigned to them initially (ascending order).</p>

<p>The players numbered <code>firstPlayer</code> and <code>secondPlayer</code> are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may <strong>choose</strong> the outcome of this round.</p>

<p>Given the integers <code>n</code>, <code>firstPlayer</code>, and <code>secondPlayer</code>, return <em>an integer array containing two values, the <strong>earliest</strong> possible round number and the&nbsp;<strong>latest</strong> possible round number in which these two players will compete against each other, respectively</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 11, firstPlayer = 2, secondPlayer = 4
<strong>Output:</strong> [3,4]
<strong>Explanation:</strong>
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, firstPlayer = 1, secondPlayer = 5
<strong>Output:</strong> [1,1]
<strong>Explanation:</strong> The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 28</code></li>
	<li><code>1 &lt;= firstPlayer &lt; secondPlayer &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization + Binary Enumeration

We define a function $\text{dfs}(l, r, n)$, which represents the earliest and latest rounds where players numbered $l$ and $r$ compete among $n$ players in the current round.

The execution logic of function $\text{dfs}(l, r, n)$ is as follows:

1. If $l + r = n - 1$, it means the two players compete in the current round, return $[1, 1]$.
2. If $f[l][r][n] \neq 0$, it means this state has been calculated before, directly return the result.
3. Initialize the earliest round number as positive infinity and the latest round number as negative infinity.
4. Calculate the number of players in the first half of the current round $m = n / 2$.
5. Enumerate all possible winner combinations of the first half (using binary enumeration), for each combination:
    - Determine which players win based on the current combination.
    - Determine the positions of players numbered $l$ and $r$ in the current round.
    - Count the positions of players numbered $l$ and $r$ among the remaining players, denoted as $a$ and $b$, and the total number of remaining players $c$.
    - Recursively call $\text{dfs}(a, b, c)$ to get the earliest and latest round numbers for the current state.
    - Update the earliest and latest round numbers.
6. Store the calculation result in $f[l][r][n]$ and return the earliest and latest round numbers.

The answer is $\text{dfs}(\text{firstPlayer} - 1, \text{secondPlayer} - 1, n)$.

<!-- tabs:start -->

#### Python3

```python
@cache
def dfs(l: int, r: int, n: int):
    if l + r == n - 1:
        return [1, 1]
    res = [inf, -inf]
    m = n >> 1
    for i in range(1 << m):
        win = [False] * n
        for j in range(m):
            if i >> j & 1:
                win[j] = True
            else:
                win[n - 1 - j] = True
        if n & 1:
            win[m] = True
        win[n - 1 - l] = win[n - 1 - r] = False
        win[l] = win[r] = True
        a = b = c = 0
        for j in range(n):
            if j == l:
                a = c
            if j == r:
                b = c
            if win[j]:
                c += 1
        x, y = dfs(a, b, c)
        res[0] = min(res[0], x + 1)
        res[1] = max(res[1], y + 1)
    return res

class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        return dfs(firstPlayer - 1, secondPlayer - 1, n)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
