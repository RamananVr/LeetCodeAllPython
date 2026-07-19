---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0464.Can%20I%20Win/README_EN.md
tags:
    - Bit Manipulation
    - Memoization
    - Math
    - Dynamic Programming
    - Bitmask
    - Game Theory
---

<!-- problem:start -->

# [464. Can I Win](https://leetcode.com/problems/can-i-win)

## Description

<!-- description:start -->

<p>In the &quot;100 game&quot; two players take turns adding, to a running total, any integer from <code>1</code> to <code>10</code>. The player who first causes the running total to <strong>reach or exceed</strong> 100 wins.</p>

<p>What if we change the game so that players <strong>cannot</strong> re-use integers?</p>

<p>For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total &gt;= 100.</p>

<p>Given two integers <code>maxChoosableInteger</code> and <code>desiredTotal</code>, return <code>true</code> if the first player to move can force a win, otherwise, return <code>false</code>. Assume both players play <strong>optimally</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> maxChoosableInteger = 10, desiredTotal = 11
<strong>Output:</strong> false
<strong>Explanation:</strong>
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is &gt;= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> maxChoosableInteger = 10, desiredTotal = 0
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> maxChoosableInteger = 10, desiredTotal = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= maxChoosableInteger &lt;= 20</code></li>
	<li><code>0 &lt;= desiredTotal &lt;= 300</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: State Compression + Memoization

First, we check if the sum of all selectable integers is less than the target value. If so, it means that we cannot win no matter what, so we directly return `false`.

Then, we design a function `dfs(mask, s)`, where `mask` represents the current state of the selected integers, and `s` represents the current cumulative sum. The return value of the function is whether the current player can win.

The execution process of the function `dfs(mask, s)` is as follows:

We iterate through each integer `i` from `1` to `maxChoosableInteger`. If `i` has not been selected, we can choose `i`. If the cumulative sum `s + i` after choosing `i` is greater than or equal to the target value `desiredTotal`, or if the result of the opponent choosing `i` is losing, then the current player is winning, return `true`.

If no choice can make the current player win, then the current player is losing, return `false`.

To avoid repeated calculations, we use a hash table `f` to record the calculated states, where the key is `mask`, and the value is whether the current player can win.

The time complexity is $O(2^n)$, and the space complexity is $O(2^n)$. Where $n$ is `maxChoosableInteger`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(mask: int, s: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if mask >> i & 1 ^ 1:
                    if s + i >= desiredTotal or not dfs(mask | 1 << i, s + i):
                        return True
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
