---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1500-1599/1510.Stone%20Game%20IV/README_EN.md
rating: 1786
source: Biweekly Contest 30 Q4
tags:
    - Math
    - Dynamic Programming
    - Game Theory
---

<!-- problem:start -->

# [1510. Stone Game IV](https://leetcode.com/problems/stone-game-iv)

## Description

<!-- description:start -->

<p>Alice and Bob take turns playing a game, with Alice starting first.</p>

<p>Initially, there are <code>n</code> stones in a pile. On each player&#39;s turn, that player makes a <em>move</em> consisting of removing <strong>any</strong> non-zero <strong>square number</strong> of stones in the pile.</p>

<p>Also, if a player cannot make a move, he/she loses the game.</p>

<p>Given a positive integer <code>n</code>, return <code>true</code> if and only if Alice wins the game otherwise return <code>false</code>, assuming both players play optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>Alice can remove 1 stone winning the game because Bob doesn&#39;t have any moves.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -&gt; 1 -&gt; 0).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> n is already a perfect square, Alice can win with one move, removing 4 stones (4 -&gt; 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization

We design a function $dfs(i)$, which represents whether the current player can win the game when there are $i$ stones in the pile. If the current player can win, it returns $true$; otherwise, it returns $false$. The answer is $dfs(n)$.

The calculation process of the function $dfs(i)$ is as follows:

- If $i \leq 0$, it means the current player cannot make any move, so the current player loses the game, return $false$;
- Otherwise, enumerate the number of stones $j$ that the current player can take away, where $j$ is a square number. If the other player cannot win the game after the current player takes away $j$ stones, then the current player wins the game, return $true$. If all $j$ enumerated cannot satisfy the above condition, then the current player loses the game, return $false$.

To avoid repeated calculations, we can use memoization, i.e., use an array $f$ to record the calculation results of the function $dfs(i)$.

The time complexity is $O(n \times \sqrt{n})$, and the space complexity is $O(n)$. Where $n$ is the number of stones in the pile.

<!-- tabs:start -->

#### Python3

```python
@cache
def dfs(i: int) -> bool:
    if i <= 0:
        return False
    k = isqrt(i)
    return any(not dfs(i - j * j) for j in range(1, k + 1))

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dfs(n)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We can also use dynamic programming to solve this problem.

Define an array $f$, where $f[i]$ represents whether the current player can win the game when there are $i$ stones in the pile. If the current player can win, then $f[i]$ is $true$, otherwise it is $false$. The answer is $f[n]$.

We enumerate $i$ in the range $[1,..n]$, and enumerate $j$ in the range $[1,..i]$, where $j$ is a square number. If the other player cannot win the game after the current player takes away $j$ stones, then the current player wins the game, i.e., $f[i] = true$. If all $j$ enumerated cannot satisfy the above condition, then the current player loses the game, i.e., $f[i] = false$. Therefore, we can get the state transition equation:

$$
f[i]=
\begin{cases}
true, & \textit{if } \exists j \in [1,..i], j^2 \leq i \textit{ and } f[i-j^2] = false\\
false, & \textit{otherwise}
\end{cases}
$$

Finally, we return $f[n]$.

The time complexity is $O(n \times \sqrt{n})$, and the space complexity is $O(n)$. Where $n$ is the number of stones in the pile.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        f = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j <= i // j:
                if not f[i - j * j]:
                    f[i] = True
                    break
                j += 1
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
