---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0920.Number%20of%20Music%20Playlists/README_EN.md
tags:
    - Math
    - Dynamic Programming
    - Combinatorics
---

<!-- problem:start -->

# [920. Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists)

## Description

<!-- description:start -->

<p>Your music player contains <code>n</code> different songs. You want to listen to <code>goal</code> songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:</p>

<ul>
	<li>Every song is played <strong>at least once</strong>.</li>
	<li>A song can only be played again only if <code>k</code> other songs have been played.</li>
</ul>

<p>Given <code>n</code>, <code>goal</code>, and <code>k</code>, return <em>the number of possible playlists that you can create</em>. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, goal = 3, k = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, goal = 3, k = 0
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2, goal = 3, k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= k &lt; n &lt;= goal &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ to be the number of playlists that can be made from $i$ songs with exactly $j$ different songs. We have $f[0][0] = 1$ and the answer is $f[goal][n]$.

For $f[i][j]$, we can choose a song that we have not listened before, so the previous state is $f[i - 1][j - 1]$, and there are $n - (j - 1) = n - j + 1$ options. Thus, $f[i][j] += f[i - 1][j - 1] \times (n - j + 1)$. We can also choose a song that we have listened before, so the previous state is $f[i - 1][j]$, and there are $j - k$ options. Thus, $f[i][j] += f[i - 1][j] \times (j - k)$, where $j \geq k$.

Therefore, we have the transition equation:

$$
f[i][j] = \begin{cases}
1 & i = 0, j = 0 \\
f[i - 1][j - 1] \times (n - j + 1) + f[i - 1][j] \times (j - k) & i \geq 1, j \geq 1
\end{cases}
$$

The final answer is $f[goal][n]$.

The time complexity is $O(goal \times n)$, and the space complexity is $O(goal \times n)$. Here, $goal$ and $n$ are the parameters given in the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        f = [[0] * (n + 1) for _ in range(goal + 1)]
        f[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j - 1] * (n - j + 1)
                if j > k:
                    f[i][j] += f[i - 1][j] * (j - k)
                f[i][j] %= mod
        return f[goal][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming (Space Optimization)

We notice that $f[i][j]$ is only related to $f[i - 1][j - 1]$ and $f[i - 1][j]$. Therefore, we can use a rolling array to optimize the space complexity, reducing the space complexity to $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        f = [0] * (goal + 1)
        f[0] = 1
        for i in range(1, goal + 1):
            g = [0] * (goal + 1)
            for j in range(1, n + 1):
                g[j] = f[j - 1] * (n - j + 1)
                if j > k:
                    g[j] += f[j] * (j - k)
                g[j] %= mod
            f = g
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
