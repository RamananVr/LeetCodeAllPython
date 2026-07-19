---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0473.Matchsticks%20to%20Square/README_EN.md
tags:
    - Bit Manipulation
    - Array
    - Dynamic Programming
    - Backtracking
    - Bitmask
---

<!-- problem:start -->

# [473. Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square)

## Description

<!-- description:start -->

<p>You are given an integer array <code>matchsticks</code> where <code>matchsticks[i]</code> is the length of the <code>i<sup>th</sup></code> matchstick. You want to use <strong>all the matchsticks</strong> to make one square. You <strong>should not break</strong> any stick, but you can link them up, and each matchstick must be used <strong>exactly one time</strong>.</p>

<p>Return <code>true</code> if you can make this square and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0473.Matchsticks%20to%20Square/images/matchsticks1-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> matchsticks = [1,1,2,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can form a square with length 2, one side of the square came two sticks with length 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matchsticks = [3,3,3,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot find a way to form a square with all the matchsticks.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= matchsticks.length &lt;= 15</code></li>
	<li><code>1 &lt;= matchsticks[i] &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(u):
            if u == len(matchsticks):
                return True
            for i in range(4):
                if i > 0 and edges[i - 1] == edges[i]:
                    continue
                edges[i] += matchsticks[u]
                if edges[i] <= x and dfs(u + 1):
                    return True
                edges[i] -= matchsticks[u]
            return False

        x, mod = divmod(sum(matchsticks), 4)
        if mod or x < max(matchsticks):
            return False
        edges = [0] * 4
        matchsticks.sort(reverse=True)
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @cache
        def dfs(state, t):
            if state == (1 << len(matchsticks)) - 1:
                return True
            for i, v in enumerate(matchsticks):
                if state & (1 << i):
                    continue
                if t + v > s:
                    break
                if dfs(state | (1 << i), (t + v) % s):
                    return True
            return False

        s, mod = divmod(sum(matchsticks), 4)
        matchsticks.sort()
        if mod:
            return False
        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
