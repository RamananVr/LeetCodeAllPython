---
comments: true
difficulty: Medium
tags:
    - Bit Manipulation
    - Brainteaser
    - Array
    - Math
    - Dynamic Programming
    - Game Theory
    - Nim Game
    - 'Sprague–Grundy '
    - Impartial Game
---

<!-- problem:start -->

# [1908. Game of Nim 🔒](https://leetcode.com/problems/game-of-nim)

## Description

<!-- description:start -->

<p>Alice and Bob take turns playing a game with <strong>Alice starting first</strong>.</p>

<p>In this game, there are <code>n</code> piles of stones. On each player&#39;s turn, the player should remove any <strong>positive</strong> number of stones from a non-empty pile <strong>of his or her choice</strong>. The first player who cannot make a move loses, and the other player wins.</p>

<p>Given an integer array <code>piles</code>, where <code>piles[i]</code> is the number of stones in the <code>i<sup>th</sup></code> pile, return <code>true</code><em> if Alice wins, or </em><code>false</code><em> if Bob wins</em>.</p>

<p>Both Alice and Bob play <strong>optimally</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> piles = [1]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is only one possible scenario:
- On the first turn, Alice removes one stone from the first pile. piles = [0].
- On the second turn, there are no stones left for Bob to remove. Alice wins.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> piles = [1,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be proven that Bob will always win. One possible scenario is:
- On the first turn, Alice removes one stone from the first pile. piles = [0,1].
- On the second turn, Bob removes one stone from the second pile. piles = [0,0].
- On the third turn, there are no stones left for Alice to remove. Bob wins.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> piles = [1,2,3]
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be proven that Bob will always win. One possible scenario is:
- On the first turn, Alice removes three stones from the third pile. piles = [1,2,0].
- On the second turn, Bob removes one stone from the second pile. piles = [1,1,0].
- On the third turn, Alice removes one stone from the first pile. piles = [0,1,0].
- On the fourth turn, Bob removes one stone from the second pile. piles = [0,0,0].
- On the fifth turn, there are no stones left for Alice to remove. Bob wins.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == piles.length</code></li>
	<li><code>1 &lt;= n &lt;= 7</code></li>
	<li><code>1 &lt;= piles[i] &lt;= 7</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Could you find a linear time solution? Although the linear time solution may be beyond the scope of an interview, it could be interesting to know.</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Classic Nim uses xor, but here there are at most $7$ piles of size at most $7$, so only $7^7$ states. Searching the game graph is enough.
>
> A position is winning iff some move leaves a losing position. We memoize a tuple of pile sizes and try subtracting $1\ldots x$ from one pile.
>
> If every successor is winning, the state is losing. The answer is that predicate on the input tuple.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(st):
            lst = list(st)
            for i, x in enumerate(lst):
                for j in range(1, x + 1):
                    lst[i] -= j
                    if not dfs(tuple(lst)):
                        return True
                    lst[i] += j
            return False

        return dfs(tuple(piles))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
