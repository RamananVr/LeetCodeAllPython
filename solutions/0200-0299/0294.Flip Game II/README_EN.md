---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0294.Flip%20Game%20II/README_EN.md
tags:
    - Memoization
    - Math
    - Dynamic Programming
    - Backtracking
    - Game Theory
---

<!-- problem:start -->

# [294. Flip Game II 🔒](https://leetcode.com/problems/flip-game-ii)

## Description

<!-- description:start -->

<p>You are playing a Flip Game with your friend.</p>

<p>You are given a string <code>currentState</code> that contains only <code>&#39;+&#39;</code> and <code>&#39;-&#39;</code>. You and your friend take turns to flip <strong>two consecutive</strong> <code>&quot;++&quot;</code> into <code>&quot;--&quot;</code>. The game ends when a person can no longer make a move, and therefore the other person will be the winner.</p>

<p>Return <code>true</code> <em>if the starting player can <strong>guarantee a win</strong></em>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> currentState = &quot;++++&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The starting player can guarantee a win by flipping the middle &quot;++&quot; to become &quot;+--+&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> currentState = &quot;+&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= currentState.length &lt;= 60</code></li>
	<li><code>currentState[i]</code> is either <code>&#39;+&#39;</code> or <code>&#39;-&#39;</code>.</li>
	<li>There cannot be more than 20 consecutive <code>&#39;+&#39;</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Derive your algorithm&#39;s runtime complexity.

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canWin(self, currentState: str) -> bool:
        @cache
        def dfs(mask):
            for i in range(n - 1):
                if (mask & (1 << i)) == 0 or (mask & (1 << (i + 1)) == 0):
                    continue
                if dfs(mask ^ (1 << i) ^ (1 << (i + 1))):
                    continue
                return True
            return False

        mask, n = 0, len(currentState)
        for i, c in enumerate(currentState):
            if c == '+':
                mask |= 1 << i
        return dfs(mask)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canWin(self, currentState: str) -> bool:
        def win(i):
            if sg[i] != -1:
                return sg[i]
            vis = [False] * n
            for j in range(i - 1):
                vis[win(j) ^ win(i - j - 2)] = True
            for j in range(n):
                if not vis[j]:
                    sg[i] = j
                    return j
            return 0

        n = len(currentState)
        sg = [-1] * (n + 1)
        sg[0] = sg[1] = 0
        ans = i = 0
        while i < n:
            j = i
            while j < n and currentState[j] == '+':
                j += 1
            ans ^= win(j - i)
            i = j + 1
        return ans > 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
